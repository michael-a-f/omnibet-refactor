from flask import Flask, request, jsonify
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


@app.errorhandler(500)
@app.errorhandler(Exception)
def unhandled_exception_handler(error):
    """Unhandled exception handler."""
    return jsonify({
        'error': 'An unexpected internal server error occurred. Please try again.'
    }), 500


@app.errorhandler(404)
@app.errorhandler(405)
def route_not_found_handler(error):
    """Route not found handler."""
    return jsonify({
        'error': 'Route not found: {0} {1}'.format(request.method, request.path)
    }), 404


# Endpoint
@app.route("/api/odds/<sport_league>", methods=['GET'])
def get_odds_for_sport(sport_league):
    """Endpoint to scrape oddsshark.com and return sports gambling info in JSON.

    The sportsbooks offering odds sit in their own container.
    Matchup data (team names, game date and time) sits in its own container.
    Odds data sits in its own container.
    
    For simplicity, this scrapes each container independently and then
    'weaves' all 3 pieces of information together to get the final output.
    
    Args:
        sport_league (string): The name of the sports league to scrape info for.
    
    Returns:
        List: JSON object holding information for each matchup.
    """
    selectors = scraper.SELECTORS
   
    # Request URL and create BS4 object. Proxy IP address used to bypass
    # content restriction due to state legislation. Proxy address found 
    # using https://hidemy.name/en/proxy-list/
    url = f'https://www.oddsshark.com/{sport_league}/odds'
    proxies = {
        "http": "http://51.81.155.78:3128", # Hillsboro, Oregon
        "https": "http://51.81.155.78:3128", # Hillsboro, Oregon
    }
    http_response = requests.get(url, proxies=proxies)
    
    try:
        http_response.raise_for_status()
        page_html = BeautifulSoup(http_response.content, 'html.parser')
    except:
        return jsonify(bc.get_fake_data(sport_league))

    # The sportsbook names are held in the 'alt' attribute of their images.
    sportsbook_images = page_html.select(selectors["sportsbooks"])
    sportsbooks = [image['alt'].lower().strip() for image in sportsbook_images]
    
    # Find all containers holding matchup info and create matchup dict for each one.
    matchup_containers = page_html.find_all('div', class_= selectors["matchups"])
    matchups = scraper.scrape_matchups(sport_league, matchup_containers, selectors)

    # Find all the game odds containers and create odds dict for each one.
    odds_containers = page_html.select(selectors["odds"])
    odds = [scraper.scrape_odds(odds_container, sportsbooks, selectors) for odds_container in odds_containers]
    
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
            return jsonify(matchups)
        except:
            return jsonify(bc.get_fake_data(sport_league))
    else:
        return jsonify(bc.get_fake_data(sport_league))