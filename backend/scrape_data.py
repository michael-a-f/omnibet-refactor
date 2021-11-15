import requests
from bs4 import BeautifulSoup
import json
import betting_calculations as bc
import sys

# CSS class selectors for use by BS4.
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


def scrape_matchups(sport, matchup_containers, selectors):
    """Creates list of JSON object for each matchup in the container.

    Args:
        sport (string): The sport on oddsshark.com to scrape odds for.
        matchup_containers (list): Holds the matchup containers on webpage.
        selectors (dict): CSS class selectors for use by BS4.

    Returns:
        List: JSON object for each matchup.
    """
    matchups = []
    for matchup_container in matchup_containers:
        container_above = matchup_container.previous_sibling
        is_date_new = selectors["gamedates"] in container_above['class']
        if is_date_new:
            date = json.loads(container_above['data-op-date'])["full_date"]
        matchup = create_matchup_dict(matchup_container, sport, date, selectors)
        matchups.append(matchup)
    return matchups


def create_matchup_dict(matchup_container, sport, date, selectors):
    """Creates a dictionary for a match's information.

    Args:
        matchup_container (NavigableString): The HTML for a single matchup.
        sport (string): The sport on oddsshark.com to scrape odds for.
        date (string): The date of the matchup.
        selectors (dict): CSS class selectors for use by BS4.

    Returns:
        Dict: The sport, date, time, and team information for the matchup.
    """
    # Get team 1's data from data attribute and add logo.
    team_1_container = matchup_container.find('div', class_= selectors["team_1_info"])
    team_1 = json.loads(team_1_container['data-op-name'])
    team_1["logo"] = f"../../../img/{sport}-logos/{team_1['full_name']}.png"

    # Get team 2's data from data attribute and add logo.
    team_2_container = matchup_container.find('div', class_= selectors["team_2_info"])
    team_2 = json.loads(team_2_container['data-op-name'])
    team_2["logo"] = f"../../../img/{sport}-logos/{team_2['full_name']}.png"

    # Get the time of the matchup
    time = matchup_container.find('div', class_= selectors["gametimes"]).get_text()

    # Create the object to return
    match_data = {
        "sport": sport,
        "date": date,
        "time": time,
        "team_1": team_1,
        "team_2": team_2
    }

    return match_data


def scrape_odds(odds_container, sportsbooks, selectors):
    """List of dicts with key, value pairs of sportsbooks, odds @ that sportsbook.

    Args:
        odds_container (NavigableString): Holds odds information for both teams.
        sportsbooks (list): Name for each sportsbook offering odds.
        selectors (dict): CSS class selectors for use by BS4.

    Returns:
        List: JSON objects for each matchup's odds.
    """
    matchup_odds = {}
    
    # There is specific HTML container for a game without any odds.
    matchup_has_no_odds = 'no-odds-wrapper' in odds_container['class']
    if matchup_has_no_odds:
        empty_odds = {sportsbooks[i]: None for i in range(len(sportsbooks))}
        matchup_odds["team_1"] = matchup_odds["team_2"] = empty_odds
    else:
        # Scrape team 1's odds
        t1_containers = odds_container.select(selectors["team_1_odds"])
        t1_odds = [scrape_odds_from_container(container) for container in t1_containers]
        matchup_odds["team_1"] = {sportsbooks[i]: t1_odds[i] for i in range(len(sportsbooks))}
        
        # Scrape team 2's odds
        t2_containers = odds_container.select(selectors["team_2_odds"])
        t2_odds = [scrape_odds_from_container(container) for container in t2_containers]
        matchup_odds["team_2"] = {sportsbooks[i]: t2_odds[i] for i in range(len(sportsbooks))}
    
    return matchup_odds


def scrape_odds_from_container(odds_container):
    """Get the odds value from a single container holding an odd.

    Args:
        odds_container (NavigableString): The HTML container for an odd value.

    Returns:
        Integer or None: Integer odd value if it exists, otherwise None.
    """
    odds = json.loads(odds_container['data-op-moneyline'])
    if odds['fullgame'] != "":
        return int(odds['fullgame'])
    else:
        return None


# This code is identical to the code that runs on the endpoint in server.py.
# I've includes this here so that I can test from cmd without starting the
# Flask server.
def scrape_from_command_line(sport_league):
    """Scrape oddshark.com for sports gambling information and formats in JSON.
    
    Args:
        sport_league (string): The name of the sport league to scrape info for.
    
    Returns:
        List: JSON objects holding matchup info and odds for each match.
    """
    # Request URL and create BS4 object.
    url = f'https://www.oddsshark.com/{sport_league}/odds'
    http_response = requests.get(url)
    
    try:
        http_response.raise_for_status()
        page_html = BeautifulSoup(http_response.content, 'html.parser')
    except:
        return bc.get_fake_data(sport_league)

    # The sportsbook names are held in the 'alt' attribute of their images.
    sportsbook_images = page_html.select(SELECTORS["sportsbooks"])
    sportsbooks = [image['alt'].lower().strip() for image in sportsbook_images]
    
    # Find all containers holding matchup info and create matchup dict for each one.
    matchup_containers = page_html.find_all('div', class_= SELECTORS["matchups"])
    matchups = scrape_matchups(sport_league, matchup_containers, SELECTORS)

    # Find all the game odds containers and create odds dict for each one.
    odds_containers = page_html.select(SELECTORS["odds"])
    odds = [scrape_odds(odds_container, sportsbooks, SELECTORS) for odds_container in odds_containers]
    
    # Check that every matchup has a corresponding odds dict.
    is_scraped_correctly = len(matchups) == len(odds)

    # Add info from odds dict to the matchup dict to create desired output.
    if is_scraped_correctly:
        try:
            current_matchup = 0
            for matchup in matchups:
                for team in ["team_1", "team_2"]:
                    # Add each team's odds dict to the matchup dict.
                    team_odds = odds[current_matchup][team]
                    matchup[team]["odds"] = team_odds

                    # Add betting metrics to the matchup dict.
                    max_profit_odd = bc.optimal_odd_to_bet(team_odds)
                    matchup[team]["money_multiplier"] = bc.money_multiplier(max_profit_odd)
                    matchup[team]["win_probability"] = bc.win_probability_from_odds(team_odds)
                
                # Maintain correct matchup dict to odds dict pairing.
                current_matchup += 1
            return matchups
        except:
            return bc.get_fake_data(sport_league)
    else:
        return bc.get_fake_data(sport_league)


# Scrape for given sport by running 'python scrape_data.py sport' in cmd.
if __name__ == '__main__':
    valid_sport = sys.argv[1] in {'nba', 'nhl', 'ufc', 'ncaab', 'ncaaf',
    'nfl', 'boxing'}
    
    if valid_sport:
        print(json.dumps(scrape_from_command_line(sys.argv[1]), indent=4))
    else:
        print(f'{sys.argv[1]} is not a supported argument. Try another.')