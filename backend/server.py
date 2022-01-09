from requests.exceptions import HTTPError, ProxyError, Timeout
from flask import Flask, request, jsonify, abort
from flask_cors import CORS
import scrape_data as scraper
import requests
from bs4 import BeautifulSoup
import betting_calculations as bc
import json

# Initialize the Flask application.
app = Flask(__name__)

# Configure indentation for JSON response.
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Add support for cross-origin requests.
CORS(app)

# Error handling
@app.errorhandler(HTTPError)
@app.errorhandler(404)
@app.errorhandler(405)
def route_not_found_handler(error):
    """Handle errors due to invalid routes.

    Handles errors due to if user tries to navigate to anything besides
    /api/odds/ or enters an invalid sport i.e. /api/sports/foosball.
    """
    return jsonify({
        'error': 'Route not found: {0} {1}'.format(request.method, request.path)
    }), 404


@app.errorhandler(ProxyError)
def proxy_exception_handler(error):
    """Handle errors due to sending HTTP request through Proxy IP
    
    Because sports gambling legislation differs across states, oddsshark.com 
    might restrict content based on IP address location. To get around this, we
    send the HTTP request through Proxy IP addresses found on sites like 
    free-proxy-list.net or hidemy.name. These services are not very reliable,
    so errors are quite common.

    In the event of an error with the Proxy being used, our solution is to
    simply return the data from the most recent, successful response for the 
    given sport. The sport causing the error is passed into the description 
    parameter (second positional argument) in the abort() method.
    """
    sport_causing_err = error.description
    placeholder_response = bc.get_fake_data(sport_causing_err)
    return jsonify(placeholder_response), 500


@app.errorhandler(Exception)
def unhandled_exception_handler(error):
    """Handle errors unhandled elsewhere.
    
    Just to be safe and to preserve site functionality, any unhandled
    exceptions will return the most recent, successful request
    """
    sport_causing_err = error.description
    placeholder_response = bc.get_fake_data(sport_causing_err)
    return jsonify(placeholder_response), 500


# Endpoint
@app.route("/api/odds/<sport>", methods=['GET'])
def get_odds_for_sport(sport):
    """Endpoint to scrape oddsshark.com and return sports gambling info in JSON.

    The sportsbooks offering odds sit in their own container.
    Matchup data (team names, game date and time) sits in its own container.
    Odds data sits in its own container.
    
    For simplicity, this scrapes each container independently and then
    'weaves' all 3 pieces of information together to get the final output.
    
    Args:
        sport (string): The name of the sport to scrape info for.
    
    Returns:
        List: JSON object holding information for each matchup.
    """
    selectors = scraper.SELECTORS
    
    # Catch invalid sport argument before even sending request.
    if sport not in scraper.SPORTS:
        abort(404, sport)

    # Send request using Proxy to bypass content restriction due to IP location. 
    url = f'https://www.oddsshark.com/{sport}/odds'
    proxies = {
        "http": "http://51.81.155.78:3128", # Florida
        "https": "http://51.81.155.78:3128", # Florida
    }
    
    # Catch various exceptions and handle using functions above. Otherwise,
    # instantiate BS4 object to continue scraping.
    try:
        http_response = requests.get(url, proxies=proxies)
        http_response.raise_for_status()  
    except (requests.exceptions.ConnectionError, requests.exceptions.ProxyError, 
    requests.exceptions.Timeout) as err_proxy:
        abort(500, sport) # invoke proxy_error_handler
    except (requests.exceptions.HTTPError) as err_http:
        abort(404, sport) # invoke route_not_found_handler
    except:
        abort(500, sport) # invoke unhandled_exception_handler
    else:
        page_bs4 = BeautifulSoup(http_response.content, 'html.parser')
    
    # Scrape sportsbook names
    sportsbook_names = scraper.scrape_sportsbook_names(page_bs4, selectors)
    
    # Scrape the left-hand containers holding matchup info only.
    matchup_containers = page_bs4.find_all('div', class_= selectors["matchups"])
    matchups = scraper.scrape_matchups(sport, matchup_containers, selectors)

    # Find all the game odds containers and create odds dict for each one.
    odds_containers = page_bs4.select(selectors["odds"])
    odds = []
    for container in odds_containers:
        odds.append(scraper.scrape_odds(container, sportsbook_names, selectors))
    
    # Scraping correct if every matchup has a corresponding odds dict.
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
            return jsonify(matchups)
        except:
            # Error in "zipping" matchups and odds.
            abort(500, sport)
    else:
        # Scraping of odds was done incorrectly.
        abort(500, sport)