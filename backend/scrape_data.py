import requests
from bs4 import BeautifulSoup
import json
import betting_calculations as bc

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
        # if odds_array[i] == "":
        #     odds_at[book] = None
        # else:
        #     odds_at[book] = int(odds_array[i])
        i += 1
    return odds_at


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
    all_odds = []
    try:
        for match in page.select(selectors["odds"]):
            t1_odds_list = []
            t2_odds_list = []
            
            if 'no-odds-wrapper' in match["class"]:
                t1_odds_list = [""] * len(books)
                t2_odds_list = [""] * len(books)
                t1_odds = create_odds_object(books, t1_odds_list)
                t2_odds = create_odds_object(books, t2_odds_list)
            else:
                for odd in match.select(selectors["team_1_odds"]):
                    moneyline = json.loads(odd['data-op-moneyline'])["fullgame"]
                    t1_odds_list.append(moneyline.strip())
                t2_odds_list = []
                for odd in match.select(selectors["team_2_odds"]):
                    moneyline = json.loads(odd['data-op-moneyline'])["fullgame"]
                    t2_odds_list.append(moneyline.strip())
                t1_odds = create_odds_object(books, t1_odds_list)
                t2_odds = create_odds_object(books, t2_odds_list)
            
            all_odds.append([t1_odds, t2_odds])
        print('Odds scraped successfully.')
        return all_odds
    except:
        print('Error scraping odds.  Returned fake data.')
        return bc.get_fake_data()


def get_matchup_data(page, selectors):
    """Return JSON for the team and game date/time for each matchup.
        
        Arguments:
        page (object): BS4 object for the requested page HTML
        matchups_css_selector: The HTML class name for each matchup container
        
        Returns:
        List of JSON objects
        """
    all_matchups = []
    try:
        for matchup in page.find_all('div', class_= selectors["matchups"]):
            if selectors["gamedates"] in matchup.previous_sibling['class']:
                gamedate = json.loads(matchup.previous_sibling['data-op-date'])["full_date"]
            gametime = matchup.find('div', class_= selectors["gametimes"]).get_text() + 'm'
            team_1_info = matchup.find('div', class_= selectors["team_1_info"])
            team_1 = json.loads(team_1_info['data-op-name'])
            team_2_info = matchup.find('div', class_= selectors["team_2_info"])
            team_2 = json.loads(team_2_info['data-op-name'])
            match_data = {
                "date": gamedate,
                "time": gametime,
                "team_1": team_1,
                "team_2": team_2
            }
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
    match_data = get_matchup_data(page_html, SELECTORS)

    # Get list of sportsbooks to scrape odds from.
    scraped_book_names = []
    try:
        books_on_page = page_html.select(SELECTORS["sportsbooks"])
        for sportsbook_img in books_on_page:
            name = sportsbook_img['alt'].lower().strip()
            scraped_book_names.append(name)
        print('Sportsbook names scraped successfully.')
    except:
        print('Error in scraping sportsbook names.  Returned fake data.')
        return bc.get_fake_data() 
    
    # Get list of JSON objects for each game's odds.
    match_odds = get_odds(page_html, scraped_book_names, SELECTORS)
    
    # Every game object needs a corresponding odds object.
    scraping_error = len(match_odds) != len(match_data)
    
    if scraping_error:
        print('Error formatting final JSON data.  Returned fake data.')
        return bc.get_fake_data() 
    else:
        game_counter = 0
        for match in match_data:
            # Attach odds objects to their game object.
            team_1_odds = match_odds[game_counter][0]
            team_2_odds = match_odds[game_counter][1]
            
            # Calculate and add dict entries for team 1
            match['team_1']['odds'] = team_1_odds
            match["team_1"]["win_probability"] = bc.win_probability_from_odds(team_1_odds)
            optimal_t1_bet = bc.optimal_odd_to_bet(team_1_odds)
            match["team_1"]["money_multiplier"] = bc.money_multiplier(optimal_t1_bet)
            
            # Calculate and add dict entries for team 2
            match['team_2']['odds'] = team_2_odds
            match["team_2"]["win_probability"] = bc.win_probability_from_odds(team_2_odds)
            optimal_t2_bet = bc.optimal_odd_to_bet(team_2_odds)
            match["team_2"]["money_multiplier"] = bc.money_multiplier(optimal_t2_bet)
            
            game_counter += 1
        print('Final JSON data formatted successfully.')
        return match_data

# print(json.dumps(get_scraped_json('mlb'), indent=4))
# get_scraped_json('nba')