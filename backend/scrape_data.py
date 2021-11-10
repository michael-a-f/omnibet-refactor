import requests
from bs4 import BeautifulSoup
import json
import betting_calculations as bc
import sys

SELECTORS = {
    "sportsbooks": '.op-book-header img',
    "matchups": 'op-matchup-wrapper',
    "gamedates": 'op-separator-bar',
    "gametimes": 'op-matchup-time op-matchup-text',
    "team_1_info": 'op-matchup-team op-matchup-text op-team-top',
    "team_2_info": 'op-matchup-team op-matchup-text op-team-bottom',
    "odds": '.op-item-row-wrapper.not-futures',
    "team_1_odds": '.op-first-row .op-item.op-spread',
    "team_2_odds": '.op-second-row .op-item.op-spread'
}


def get_page_html(sport):
    """Return BS4 object from HTTP response to URL
    
    Arguments:
    URL (string): The destination of the request
    
    Returns:
    BS4 response object
    """
    url = 'https://www.oddsshark.com/' + sport + '/odds'
    try:
        res = requests.get(url)
        res.raise_for_status()
        return BeautifulSoup(res.content, 'html.parser')
    except requests.exceptions.HTTPError as http_err:
        return http_err
    except requests.exceptions.ConnectionError as conn_err:
       return conn_err
    except requests.exceptions.Timeout as timeout_err:
        return timeout_err
    except requests.exceptions.RequestException as other_err:
       return other_err
    
    


def get_sportsbook_names(page, selectors):
    """Return a list of the sportsbooks providing odds
    
    Arguments:
    page (object): BS4 object for the requested page HTML
    sportsbooks_css_selector: The HTML class name used on the sportsboooks
    
    Returns:
    list of strings for the names of the sportsbooks
    """
    sportsbook_names = []
    for book in page.select(selectors["sportsbooks"]):
        sportsbook_names.append(book['alt'].lower())
    return sportsbook_names


def create_odds_object(books, odds_array):
    """Create a dict with keys for sportsbook and values for the odds
    at that sportsbook.

    Arguments:
    odds_array (list): the row of odds from left to right for a particular team.
    """
    i = 0
    odds_at = {}
    for book in books:
        if book == "":
            return odds_at
        try:
            odds_at[book] = int(odds_array[i])
        except:
            odds_at[book] = None
        i += 1
    return odds_at


def scrape_odds_from_container(container):
    odds = json.loads(container['data-op-moneyline'])
    fullgame_odds = odds['fullgame']
    if fullgame_odds != "":
        return int(fullgame_odds)
    else:
        return None
    

def get_odds(page, books, selectors):
    """Return the odds for a given page
    
    Arguments:
    page (object): BS4 object for the requested page HTML
    odds_css_selector (string): the HTML class name for all match odds
    t1_css_selector (string): the HTML class name for team 1 odds
    t2_css_selector (string): the HTML class name for team 2 odds

    Returns:
    List of lists in format [t1 odds, t2 odds] for each matchup.
    """
    json_odds = []
    try:
        game_odds_containers = page.select(selectors["odds"])

        # Iterate over every game
        for game_odds_container in game_odds_containers:
            game_odds = {}

            # If no odds, create an empty odds JSON object.
            game_has_no_odds = 'no-odds-wrapper' in game_odds_container['class']
            if game_has_no_odds:
                game_odds["team1"] = game_odds["team2"] = {books[i]: None for i in range(len(books))}
            
            # If odds exist, scrape them and create odds JSON object for team 1 and team 2
            else:
                t1_containers = game_odds_container.select(selectors["team_1_odds"])
                t1_odds = [scrape_odds_from_container(container) for container in t1_containers]
                game_odds["team1"] = {books[i]: t1_odds[i] for i in range(len(books))}
                
                t2_containers = game_odds_container.select(selectors["team_2_odds"])
                t2_odds = [scrape_odds_from_container(container) for container in t2_containers]
                game_odds["team2"] = {books[i]: t2_odds[i] for i in range(len(books))}
                # print(json.dumps(game_odds, indent=4))
                
            # Add the odds JSON object to the list
            json_odds.append(game_odds)
        print('Odds scraped successfully.')
        return json_odds
    except:
        print('Error scraping odds.  Returned fake data.')
        return bc.get_fake_data()


def get_matchup_data(page_html, sport, selectors):
    """Return JSON for the team and game date/time for each matchup.
        
        Arguments:
        page (object): BS4 object for the requested page HTML
        matchups_css_selector: The HTML class name for each matchup container
        
        Returns:
        List of JSON objects
        """
    all_matchups = []
    try:
        matchup_containers = page_html.find_all('div', class_= selectors["matchups"])
        for matchup_container in matchup_containers:

            # Get the date to use for the matchup
            container_above = matchup_container.previous_sibling
            classlist_of_container_above = container_above['class']
            is_date_new = selectors["gamedates"] in classlist_of_container_above
            if is_date_new:
                date_json = json.loads(container_above['data-op-date'])
                gamedate = date_json["full_date"]

            # Get the time to use for the matchup
            gametime = matchup_container.find('div', class_= selectors["gametimes"]).get_text()

            # Get team 1 info
            team_1_container = matchup_container.find('div', class_= selectors["team_1_info"])
            team_1_data = json.loads(team_1_container['data-op-name'])
            team_1_logo = f"../../../img/{sport}-logos/{team_1_data['full_name']}.png"
            team_1_data["logo"] = team_1_logo
            # Get team 2 info
            team_2_container = matchup_container.find('div', class_= selectors["team_2_info"])
            team_2_data = json.loads(team_2_container["data-op-name"])
            team_2_logo = f"../../../img/{sport}-logos/{team_2_data['full_name']}.png"
            team_2_data["logo"] = team_2_logo

            # Create the JSON object
            match_data = {
                "sport": sport,
                "date": gamedate,
                "time": gametime,
                "team_1": team_1_data,
                "team_2": team_2_data
            }

            # Append to list
            all_matchups.append(match_data)

        print('Matchups scraped successfully.')
        return all_matchups
    except:
        print('Error scraping matchups.  Returned fake data.')
        return bc.get_fake_data()


def get_scraped_json(sport_league):
    """Return list of formatted JSON objects per API specs.
    Content to scrape for sportsbook_names, match_data, and match_odds all 
    sit in independent HTML containers, so scrape them each independently
    and then weave together.
    
    Arguments:
    sport (string): the sport to scrape oddsshark.com odds for.
    
    Returns:
    List of JSON objects
    """
    url_to_scrape = 'https://www.oddsshark.com/' + sport_league + '/odds'
    
    # Send the request and if exception, use fake API data.
    http_response = requests.get(url_to_scrape)
    
    try:
        http_response.raise_for_status()
        page_html = BeautifulSoup(http_response.content, 'html.parser')
        print('Response received successfully.')
    except:
        print('Error in http request/response.  Returned fake data.')
        return bc.get_fake_data() 
    
    # Get list of JSON objects for each game's info.
    match_data = get_matchup_data(page_html, sport_league, SELECTORS)

    # Get list of sportsbooks to scrape odds from.
    scraped_book_names = []
    try:
        sportsbook_images = page_html.select(SELECTORS["sportsbooks"])
        for image in sportsbook_images:
            name = image['alt'].lower().strip()
            scraped_book_names.append(name)
        print('Sportsbook names scraped successfully.')
    except:
        print('Error in scraping sportsbook names.  Returned fake data.')
        return bc.get_fake_data() 
    
    # Get list of JSON objects for each game's odds.
    match_odds = get_odds(page_html, scraped_book_names, SELECTORS)
    
    # Every game object needs a corresponding odds object.
    is_scraped_correctly = len(match_odds) == len(match_data)
    
    if is_scraped_correctly:
        game_counter = 0
        for match in match_data:
            # Get odds objects for that match.
            team_1_odds = match_odds[game_counter]["team1"]
            team_2_odds = match_odds[game_counter]["team2"]
            
            # Attach odds object to its match object
            match['team_1']['odds'] = team_1_odds
            match['team_2']['odds'] = team_2_odds
            
            # Add entries for teams' win probabilities
            match["team_1"]["win_probability"] = bc.win_probability_from_odds(team_1_odds)
            match["team_2"]["win_probability"] = bc.win_probability_from_odds(team_2_odds)
            
            # Calculate teams' best bet
            optimal_t1_bet = bc.optimal_odd_to_bet(team_1_odds)
            optimal_t2_bet = bc.optimal_odd_to_bet(team_2_odds)
            
            # Add entries for teams' best money multipliier
            match["team_1"]["money_multiplier"] = bc.money_multiplier(optimal_t1_bet)
            match["team_2"]["money_multiplier"] = bc.money_multiplier(optimal_t2_bet)
            
            # Go to next game
            game_counter += 1
        
        print('Final JSON data formatted successfully.')
        return match_data
    else:
        print('Error formatting final JSON data.  Returned fake data.')
        return bc.get_fake_data() 


# Output scraped data in JSON format using 'python scrape_data.py sport'
# where sport is the sport/league to scrape for.
if __name__ == '__main__':
    valid_argument = sys.argv[1] in {'nba', 'nhl', 'ufc', 'ncaab', 'ncaaf',
    'nfl', 'boxing', 'tennis/atp', 'tennis/wta'}
    
    if valid_argument:
        print(json.dumps(get_scraped_json(sys.argv[1]), indent=4))
    else:
        print(f'{sys.argv[1]} is not a supported argument. Try another.')

# CURRENTLY WORKING:
# nba
# nhl
# ufc
# ncaab
# ncaaf
# nfl
# boxing
# tennis/atp
# tennis/wta

# WORKS BUT OUT OF SEASON:
# mlb
# wnba

# WORKS BUT MINIMAL MATCHES
# esports/dota-2
# esports/overwatch
# esports/league-of-legends

# DOESNT WORK:
# soccer (not two outcome format)
# politics (not head to head format)
# golf (not head to head format)
# cfl (different formatting throws off scraping)