import requests
from bs4 import BeautifulSoup
import json
import betting_calculations as bc
import sys
from datetime import datetime

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

# The sports available to scrape for.
SPORTS = ["nba", "nhl", "ufc", "ncaab", "ncaaf", "nfl", "boxing",]

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
            # date
            raw_date = json.loads(container_above['data-op-date'])["full_date"].split()
            month_string = raw_date[1]
            day_string = raw_date[2]
            month_to_integer = {
            "January": 1,
            "February": 2,
            "March": 3, 
            "April": 4,
            "May": 5,
            "June": 6,
            "July": 7,
            "August": 8,
            "September": 9,
            "October": 10,
            "November": 11,
            "December": 12,
            }
            month = month_to_integer[month_string]
            day = int(day_string)
            year = datetime.today().year
            
            date = [year, month, day]

            

        matchup = create_matchup_dict(matchup_container, sport, date, selectors)
        matchups.append(matchup)
    return matchups


def create_matchup_dict(matchup_container, sport, date, selectors):
    """Creates a dictionary for a match's information.

    Args:
        matchup_container (NavigableString): The HTML for a single matchup.
        sport (string): The sport on oddsshark.com to scrape odds for.
        date (list): [year, month, day] where elements are integers.
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

    # Get the time
    raw_time = matchup_container.find('div', class_= selectors["gametimes"]).get_text()
    is_pm = raw_time[-1] == "p"
    time = raw_time[:-1].split(":")
    hour = int(time[0])
    if is_pm:
        hour = hour + 12
    minute = int(time[1])
   
    # Create datetime object using date and time
    date_time = datetime(date[0], date[1], date[2], hour, minute)

    # Create the object to return
    match_data = {
        "sport": sport,
        "datetime": str(date_time),
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
        matchup_odds["team_1"] = empty_odds
        matchup_odds["team_2"] = empty_odds
    else:
        
        # Scrape team 1's odds
        t1_containers = odds_container.select(selectors["team_1_odds"])
        # print(t1_containers)
        t1_odds = [scrape_odds_from_container(container) for container in t1_containers]
        # print(t1_odds)
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


def scrape_sportsbook_names(page_bs4, selectors):
    sportsbook_images = page_bs4.select(selectors["sportsbooks"])
    names = [image["alt"].lower().strip() for image in sportsbook_images]
    return names


def scrape_data_for(sport):
    # Send request using Proxy to bypass content restriction due to IP location. 
    # Handle exceptions by returning "fake" i.e. old data.
    url = f'https://www.oddsshark.com/{sport}/odds'
    proxies = {
        "http": "http://51.81.155.78:3128", # Florida
        "https": "http://51.81.155.78:3128", # Florida
    }
    try:
        http_response = requests.get(url, proxies=proxies)
        http_response.raise_for_status()  
    except requests.exceptions.HTTPError as err_http:
        return bc.get_fake_data(sport)
    except requests.exceptions.ConnectionError as err_conn:
        return bc.get_fake_data(sport)
    except requests.exceptions.Timeout as err_time:
        return bc.get_fake_data(sport)
    except requests.exceptions.ProxyError as err_proxy:
        return bc.get_fake_data(sport)
    else:
        page_bs4 =  BeautifulSoup(http_response.content, 'html.parser')
    
    # Scrape sportsbook names
    sportsbook_names = scrape_sportsbook_names(page_bs4, SELECTORS)

    # Scrape the left-hand containers holding matchup info only.
    matchup_containers = page_bs4.find_all('div', class_= SELECTORS["matchups"])
    matchups = scrape_matchups(sport, matchup_containers, SELECTORS)

    # Find all the game odds containers and create odds dict for each one.
    odds_containers = page_bs4.select(SELECTORS["odds"])
    odds = []
    for container in odds_containers:
        odds.append(scrape_odds(container, sportsbook_names, SELECTORS))
    
    # Check that every matchup has a corresponding odds dict.
    is_scraped_correctly = len(matchups) == len(odds)

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
            
                current_matchup += 1
            return matchups
        except:
            return bc.get_fake_data(sport)
    else:
        return bc.get_fake_data(sport)


# Scrape for given sport by running 'python scrape_data.py sport' in cmd.
if __name__ == '__main__':
    valid_sport = sys.argv[1] in {'nba', 'nhl', 'ufc', 'ncaab', 'ncaaf',
    'nfl', 'boxing'}
    
    if valid_sport:
        print(json.dumps(scrape_data_for(sys.argv[1]), indent=4))
    else:
        print(f'{sys.argv[1]} is not a supported argument. Try another.')