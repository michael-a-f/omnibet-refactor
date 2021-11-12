from flask import Flask, jsonify
from flask_cors import CORS
import scrape_data as scraper

# Initialize the Flask application.
app = Flask(__name__)

# Configure indentation for JSON response.
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Add support for cross-origin requests.
CORS(app)

# Endpoint
@app.route("/api/odds/<sport_league>")
def get_odds_for_sport(sport_league):
    response = scraper.get_scraped_json(sport_league)
    return jsonify(response)