def implied_probability(odd):
    """Return the probability of a win from a given integer odd value.

    Odds can be thought of as representations of how likely/unlikely a team 
    is to win. Very negative odds imply the team is very likely to win. 
    Very positive odds imply the team is very likely to lose.
    """
    if odd >= 0:
        implied_prob = 100 / (odd + 100)
    else:
        implied_prob = abs(odd) / (abs(odd) + 100)
    return implied_prob


def win_probability_from_odds(odds_dict):
    """Returns a team's estimated winning probability based on their odds
    across the market.

    A single sportsbook might be inaccurate when setting odds, so an average
    across the implied probabilities from all sportsbooks is likely a better 
    proxy. Wisdom of the crowds.
    
    Parameters: 
    odds_dict (dict): (key, value) of (sportsbook, odds @ that sportsbook)
    
    Returns:
    float: Decimal between 0 and 1
    """
    odds = [implied_probability(odd) for odd in odds_dict.values() if odd]
    if len(odds) == 0:
        return None
    else:
        return sum(odds) / len(odds)


def optimal_odd_to_bet(odds_dict):
    """Returns the best odd to bet on for a team.

    You want to place a $5 bet on the Knicks. If they win, Book_A will
    payout $30 while Book_B will payout $50.  Book_B is clearly the better
    sportsbook to place your $5 bet. The best bet for a given team in a game
    is going to be the largest odd i.e. the odd that thinks they are most 
    likely to lose.
    """
    odds = [odd for odd in odds_dict.values() if odd]
    if len(odds) == 0:
        return None
    else:
        return max(odds)


def money_multiplier(odd):
    """Returns the factor by which a bet amount gets multiplied if it wins.
    """
    if not odd or odd == 0:
        return 0

    if odd > 0:
        money_multiplier = (100 + odd) / 100
    else:
        money_multiplier = (100 + abs(odd)) / abs(odd)

    return money_multiplier


def get_fake_data(sport_league):
    """Returns placeholder JSON data for the sport provided when web scraping 
    fails.  It is real data, just from previous dates.

    Args:
        sport_league (string): The name of the sport league to scrape info for.

    Returns:
        Dict: JSON objects holding information for each matchup in that sport.
    """
    fake = {
        "nba": [
  {
    "datetime": "2022-01-09 00:00:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "San Antonio", 
      "logo": "../../../img/nba-logos/San Antonio.png", 
      "money_multiplier": 5.5, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": 450
      }, 
      "short_name": "SAN", 
      "win_probability": 0.18181818181818182
    }, 
    "team_2": {
      "full_name": "Brooklyn", 
      "logo": "../../../img/nba-logos/Brooklyn.png", 
      "money_multiplier": 1.1538461538461537, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": -650
      }, 
      "short_name": "BKN", 
      "win_probability": 0.8666666666666667
    }
  }, 
  {
    "datetime": "2022-01-09 15:30:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Atlanta", 
      "logo": "../../../img/nba-logos/Atlanta.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "ATL", 
      "win_probability": None
    }, 
    "team_2": {
      "full_name": "LA Clippers", 
      "logo": "../../../img/nba-logos/LA Clippers.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "LAC", 
      "win_probability": None
    }
  }, 
  {
    "datetime": "2022-01-09 18:00:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Washington", 
      "logo": "../../../img/nba-logos/Washington.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "WAS", 
      "win_probability": None
    }, 
    "team_2": {
      "full_name": "Orlando", 
      "logo": "../../../img/nba-logos/Orlando.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "ORL", 
      "win_probability": None
    }
  }, 
  {
    "datetime": "2022-01-09 18:00:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "New Orleans", 
      "logo": "../../../img/nba-logos/New Orleans.png", 
      "money_multiplier": 3.4, 
      "odds": {
        "betonline": None, 
        "mirage": 240, 
        "opening": 240
      }, 
      "short_name": "NOP", 
      "win_probability": 0.29411764705882354
    }, 
    "team_2": {
      "full_name": "Toronto", 
      "logo": "../../../img/nba-logos/Toronto.png", 
      "money_multiplier": 1.3333333333333333, 
      "odds": {
        "betonline": None, 
        "mirage": -300, 
        "opening": -300
      }, 
      "short_name": "TOR", 
      "win_probability": 0.75
    }
  }, 
  {
    "datetime": "2022-01-09 19:00:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Minnesota", 
      "logo": "../../../img/nba-logos/Minnesota.png", 
      "money_multiplier": 1.4807692307692308, 
      "odds": {
        "betonline": None, 
        "mirage": -225, 
        "opening": -208
      }, 
      "short_name": "MIN", 
      "win_probability": 0.6838161838161838
    }, 
    "team_2": {
      "full_name": "Houston", 
      "logo": "../../../img/nba-logos/Houston.png", 
      "money_multiplier": 2.85, 
      "odds": {
        "betonline": None, 
        "mirage": 185, 
        "opening": 170
      }, 
      "short_name": "HOU", 
      "win_probability": 0.36062378167641324
    }
  }, 
  {
    "datetime": "2022-01-09 19:00:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Denver", 
      "logo": "../../../img/nba-logos/Denver.png", 
      "money_multiplier": 1.3333333333333333, 
      "odds": {
        "betonline": None, 
        "mirage": -300, 
        "opening": -300
      }, 
      "short_name": "DEN", 
      "win_probability": 0.75
    }, 
    "team_2": {
      "full_name": "Oklahoma City", 
      "logo": "../../../img/nba-logos/Oklahoma City.png", 
      "money_multiplier": 3.4, 
      "odds": {
        "betonline": None, 
        "mirage": 240, 
        "opening": 240
      }, 
      "short_name": "OKC", 
      "win_probability": 0.29411764705882354
    }
  }, 
  {
    "datetime": "2022-01-09 19:30:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Chicago", 
      "logo": "../../../img/nba-logos/Chicago.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "CHI", 
      "win_probability": None
    }, 
    "team_2": {
      "full_name": "Dallas", 
      "logo": "../../../img/nba-logos/Dallas.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "DAL", 
      "win_probability": None
    }
  }, 
  {
    "datetime": "2022-01-09 20:30:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Cleveland", 
      "logo": "../../../img/nba-logos/Cleveland.png", 
      "money_multiplier": 4.75, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": 375
      }, 
      "short_name": "CLE", 
      "win_probability": 0.21052631578947367
    }, 
    "team_2": {
      "full_name": "Golden State", 
      "logo": "../../../img/nba-logos/Golden State.png", 
      "money_multiplier": 1.2, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": -500
      }, 
      "short_name": "GS", 
      "win_probability": 0.8333333333333334
    }
  }, 
  {
    "datetime": "2022-01-09 21:00:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Sacramento", 
      "logo": "../../../img/nba-logos/Sacramento.png", 
      "money_multiplier": 1.8333333333333333, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": -120
      }, 
      "short_name": "SAC", 
      "win_probability": 0.5454545454545454
    }, 
    "team_2": {
      "full_name": "Portland", 
      "logo": "../../../img/nba-logos/Portland.png", 
      "money_multiplier": 2.0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": 100
      }, 
      "short_name": "POR", 
      "win_probability": 0.5
    }
  }, 
  {
    "datetime": "2022-01-09 21:30:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Memphis", 
      "logo": "../../../img/nba-logos/Memphis.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "MEM", 
      "win_probability": None
    }, 
    "team_2": {
      "full_name": "LA Lakers", 
      "logo": "../../../img/nba-logos/LA Lakers.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "LAL", 
      "win_probability": None
    }
  }, 
  {
    "datetime": "2022-01-10 19:00:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Milwaukee", 
      "logo": "../../../img/nba-logos/Milwaukee.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "MIL", 
      "win_probability": None
    }, 
    "team_2": {
      "full_name": "Charlotte", 
      "logo": "../../../img/nba-logos/Charlotte.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "CHR", 
      "win_probability": None
    }
  }, 
  {
    "datetime": "2022-01-10 19:00:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Utah", 
      "logo": "../../../img/nba-logos/Utah.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "UTA", 
      "win_probability": None
    }, 
    "team_2": {
      "full_name": "Detroit", 
      "logo": "../../../img/nba-logos/Detroit.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "DET", 
      "win_probability": None
    }
  }, 
  {
    "datetime": "2022-01-10 19:30:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Indiana", 
      "logo": "../../../img/nba-logos/Indiana.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "IND", 
      "win_probability": None
    }, 
    "team_2": {
      "full_name": "Boston", 
      "logo": "../../../img/nba-logos/Boston.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "BOS", 
      "win_probability": None
    }
  }, 
  {
    "datetime": "2022-01-10 19:30:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "San Antonio", 
      "logo": "../../../img/nba-logos/San Antonio.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "SAN", 
      "win_probability": None
    }, 
    "team_2": {
      "full_name": "New York", 
      "logo": "../../../img/nba-logos/New York.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "NY", 
      "win_probability": None
    }
  }, 
  {
    "datetime": "2022-01-10 20:00:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Philadelphia", 
      "logo": "../../../img/nba-logos/Philadelphia.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "PHI", 
      "win_probability": None
    }, 
    "team_2": {
      "full_name": "Houston", 
      "logo": "../../../img/nba-logos/Houston.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "HOU", 
      "win_probability": None
    }
  }, 
  {
    "datetime": "2022-01-10 22:00:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Cleveland", 
      "logo": "../../../img/nba-logos/Cleveland.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "CLE", 
      "win_probability": None
    }, 
    "team_2": {
      "full_name": "Sacramento", 
      "logo": "../../../img/nba-logos/Sacramento.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "SAC", 
      "win_probability": None
    }
  }, 
  {
    "datetime": "2022-01-10 22:00:00", 
    "sport": "nba", 
    "team_1": {
      "full_name": "Brooklyn", 
      "logo": "../../../img/nba-logos/Brooklyn.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "BKN", 
      "win_probability": None
    }, 
    "team_2": {
      "full_name": "Portland", 
      "logo": "../../../img/nba-logos/Portland.png", 
      "money_multiplier": 0, 
      "odds": {
        "betonline": None, 
        "mirage": None, 
        "opening": None
      }, 
      "short_name": "POR", 
      "win_probability": None
    }
  }
],
            
        "nhl": [
  {
    "datetime": "2022-01-08 14:00:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "Pittsburgh", 
      "logo": "../../../img/nhl-logos/Pittsburgh.png", 
      "money_multiplier": 1.970873786407767, 
      "odds": {
        "betonline": -109, 
        "bodog": -115, 
        "bumbet": -115, 
        "caesars": -115, 
        "intertops": -115, 
        "mirage": -115, 
        "mybookie": -130, 
        "opening": -103, 
        "station": -115, 
        "westgate": -110, 
        "wynn": -115
      }, 
      "short_name": "PIT", 
      "win_probability": 0.5329212022423223
    }, 
    "team_2": {
      "full_name": "Dallas", 
      "logo": "../../../img/nhl-logos/Dallas.png", 
      "money_multiplier": 2.1, 
      "odds": {
        "betonline": -101, 
        "bodog": -105, 
        "bumbet": -105, 
        "caesars": -105, 
        "intertops": -105, 
        "mirage": -105, 
        "mybookie": 110, 
        "opening": -119, 
        "station": -105, 
        "westgate": 100, 
        "wynn": -105
      }, 
      "short_name": "DAL", 
      "win_probability": 0.5097657170428961
    }
  }, 
  {
    "datetime": "2022-01-08 19:00:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "Toronto", 
      "logo": "../../../img/nhl-logos/Toronto.png", 
      "money_multiplier": 2.45, 
      "odds": {
        "betonline": 144, 
        "bodog": 140, 
        "bumbet": 140, 
        "caesars": 140, 
        "intertops": 145, 
        "mirage": 135, 
        "mybookie": 140, 
        "opening": 108, 
        "station": 135, 
        "westgate": 145, 
        "wynn": 135
      }, 
      "short_name": "TOR", 
      "win_probability": 0.42274493075479674
    }, 
    "team_2": {
      "full_name": "Colorado", 
      "logo": "../../../img/nhl-logos/Colorado.png", 
      "money_multiplier": 1.7518796992481203, 
      "odds": {
        "betonline": -160, 
        "bodog": -165, 
        "bumbet": -165, 
        "caesars": -160, 
        "intertops": -165, 
        "mirage": -165, 
        "mybookie": -160, 
        "opening": -133, 
        "station": -155, 
        "westgate": -160, 
        "wynn": -155
      }, 
      "short_name": "COL", 
      "win_probability": 0.6126005658570809
    }
  }, 
  {
    "datetime": "2022-01-08 19:00:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "Florida", 
      "logo": "../../../img/nhl-logos/Florida.png", 
      "money_multiplier": 2.08, 
      "odds": {
        "betonline": -113, 
        "bodog": -115, 
        "bumbet": -115, 
        "caesars": -120, 
        "intertops": -105, 
        "mirage": -110, 
        "mybookie": -115, 
        "opening": 108, 
        "station": -115, 
        "westgate": -114, 
        "wynn": -110
      }, 
      "short_name": "FLA", 
      "win_probability": 0.5262545038012443
    }, 
    "team_2": {
      "full_name": "Carolina", 
      "logo": "../../../img/nhl-logos/Carolina.png", 
      "money_multiplier": 2.04, 
      "odds": {
        "betonline": 102, 
        "bodog": -105, 
        "bumbet": -105, 
        "caesars": 100, 
        "intertops": -115, 
        "mirage": -110, 
        "mybookie": -105, 
        "opening": -133, 
        "station": -105, 
        "westgate": 104, 
        "wynn": -110
      }, 
      "short_name": "CAR", 
      "win_probability": 0.5170312991254367
    }
  }, 
  {
    "datetime": "2022-01-08 19:00:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "New Jersey", 
      "logo": "../../../img/nhl-logos/New Jersey.png", 
      "money_multiplier": 2.25, 
      "odds": {
        "betonline": 114, 
        "bodog": 115, 
        "bumbet": 115, 
        "caesars": 115, 
        "intertops": 110, 
        "mirage": 115, 
        "mybookie": 115, 
        "opening": 125, 
        "station": 110, 
        "westgate": 120, 
        "wynn": 115
      }, 
      "short_name": "NJ", 
      "win_probability": 0.4644871132196022
    }, 
    "team_2": {
      "full_name": "Columbus", 
      "logo": "../../../img/nhl-logos/Columbus.png", 
      "money_multiplier": 1.7936507936507937, 
      "odds": {
        "betonline": -126, 
        "bodog": -135, 
        "bumbet": -135, 
        "caesars": -135, 
        "intertops": -130, 
        "mirage": -135, 
        "mybookie": -135, 
        "opening": -163, 
        "station": -130, 
        "westgate": -130, 
        "wynn": -135
      }, 
      "short_name": "CLB", 
      "win_probability": 0.5745231519602743
    }
  }, 
  {
    "datetime": "2022-01-08 19:00:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "San Jose", 
      "logo": "../../../img/nhl-logos/San Jose.png", 
      "money_multiplier": 2.08, 
      "odds": {
        "betonline": -114, 
        "bodog": -120, 
        "bumbet": -120, 
        "caesars": -120, 
        "intertops": -115, 
        "mirage": -115, 
        "mybookie": -115, 
        "opening": 108, 
        "station": -120, 
        "westgate": -115, 
        "wynn": -115
      }, 
      "short_name": "SJ", 
      "win_probability": 0.5336105725102188
    }, 
    "team_2": {
      "full_name": "Philadelphia", 
      "logo": "../../../img/nhl-logos/Philadelphia.png", 
      "money_multiplier": 2.05, 
      "odds": {
        "betonline": 103, 
        "bodog": 100, 
        "bumbet": 100, 
        "caesars": 100, 
        "intertops": -105, 
        "mirage": -105, 
        "mybookie": -105, 
        "opening": -133, 
        "station": 100, 
        "westgate": 105, 
        "wynn": -105
      }, 
      "short_name": "PHI", 
      "win_probability": 0.5090919685396235
    }
  }, 
  {
    "datetime": "2022-01-08 19:00:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "Boston", 
      "logo": "../../../img/nhl-logos/Boston.png", 
      "money_multiplier": 2.74, 
      "odds": {
        "betonline": 174, 
        "bodog": 165, 
        "bumbet": 165, 
        "caesars": 165, 
        "intertops": 165, 
        "mirage": 160, 
        "mybookie": 160, 
        "opening": 106, 
        "station": 155, 
        "westgate": 160, 
        "wynn": 165
      }, 
      "short_name": "BOS", 
      "win_probability": 0.38938144238863265
    }, 
    "team_2": {
      "full_name": "Tampa Bay", 
      "logo": "../../../img/nhl-logos/Tampa Bay.png", 
      "money_multiplier": 1.7692307692307692, 
      "odds": {
        "betonline": -194, 
        "bodog": -195, 
        "bumbet": -195, 
        "caesars": -185, 
        "intertops": -190, 
        "mirage": -195, 
        "mybookie": -185, 
        "opening": -130, 
        "station": -175, 
        "westgate": -180, 
        "wynn": -185
      }, 
      "short_name": "TB", 
      "win_probability": 0.6445357998551564
    }
  }, 
  {
    "datetime": "2022-01-08 20:00:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "Washington", 
      "logo": "../../../img/nhl-logos/Washington.png", 
      "money_multiplier": 1.8695652173913044, 
      "odds": {
        "betonline": -120, 
        "bodog": -120, 
        "bumbet": -120, 
        "caesars": -120, 
        "intertops": -120, 
        "mirage": -115, 
        "mybookie": -120, 
        "opening": -145, 
        "station": -120, 
        "westgate": -118, 
        "wynn": -120
      }, 
      "short_name": "WAS", 
      "win_probability": 0.5483310202663816
    }, 
    "team_2": {
      "full_name": "Minnesota", 
      "logo": "../../../img/nhl-logos/Minnesota.png", 
      "money_multiplier": 2.18, 
      "odds": {
        "betonline": 109, 
        "bodog": 100, 
        "bumbet": 100, 
        "caesars": 100, 
        "intertops": 100, 
        "mirage": -105, 
        "mybookie": 100, 
        "opening": 118, 
        "station": 100, 
        "westgate": 108, 
        "wynn": 100
      }, 
      "short_name": "MIN", 
      "win_probability": 0.4936498953247506
    }
  }, 
  {
    "datetime": "2022-01-08 20:00:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "Nashville", 
      "logo": "../../../img/nhl-logos/Nashville.png", 
      "money_multiplier": 1.5208333333333333, 
      "odds": {
        "betonline": -192, 
        "bodog": -210, 
        "bumbet": -210, 
        "caesars": -200, 
        "intertops": -200, 
        "mirage": -210, 
        "mybookie": -200, 
        "opening": -233, 
        "station": -230, 
        "westgate": -196, 
        "wynn": -210
      }, 
      "short_name": "NAS", 
      "win_probability": 0.6750948386147038
    }, 
    "team_2": {
      "full_name": "Arizona", 
      "logo": "../../../img/nhl-logos/Arizona.png", 
      "money_multiplier": 2.95, 
      "odds": {
        "betonline": 173, 
        "bodog": 175, 
        "bumbet": 175, 
        "caesars": 175, 
        "intertops": 170, 
        "mirage": 170, 
        "mybookie": 170, 
        "opening": 185, 
        "station": 195, 
        "westgate": 176, 
        "wynn": 175
      }, 
      "short_name": "ARI", 
      "win_probability": 0.3621941833060505
    }
  }, 
  {
    "datetime": "2022-01-08 22:00:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "NY Rangers", 
      "logo": "../../../img/nhl-logos/NY Rangers.png", 
      "money_multiplier": 2.5, 
      "odds": {
        "betonline": -105, 
        "bodog": -105, 
        "bumbet": -105, 
        "caesars": -105, 
        "intertops": -110, 
        "mirage": -115, 
        "mybookie": -110, 
        "opening": 150, 
        "station": -110, 
        "westgate": 101, 
        "wynn": -110
      }, 
      "short_name": "NYR", 
      "win_probability": 0.50694679470765
    }, 
    "team_2": {
      "full_name": "Anaheim", 
      "logo": "../../../img/nhl-logos/Anaheim.png", 
      "money_multiplier": 2.5, 
      "odds": {
        "betonline": -105, 
        "bodog": -115, 
        "bumbet": -115, 
        "caesars": -115, 
        "intertops": -110, 
        "mirage": -105, 
        "mybookie": -110, 
        "opening": 150, 
        "station": -110, 
        "westgate": -111, 
        "wynn": -110
      }, 
      "short_name": "ANA", 
      "win_probability": 0.5136678047856484
    }
  }, 
  {
    "datetime": "2022-01-08 22:00:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "Chicago", 
      "logo": "../../../img/nhl-logos/Chicago.png", 
      "money_multiplier": 3.25, 
      "odds": {
        "betonline": 209, 
        "bodog": 210, 
        "bumbet": 210, 
        "caesars": 205, 
        "intertops": 200, 
        "mirage": 200, 
        "mybookie": 215, 
        "opening": 169, 
        "station": 225, 
        "westgate": 210, 
        "wynn": 210
      }, 
      "short_name": "CHI", 
      "win_probability": 0.327762048389876
    }, 
    "team_2": {
      "full_name": "Vegas", 
      "logo": "../../../img/nhl-logos/Vegas.png", 
      "money_multiplier": 1.5319148936170213, 
      "odds": {
        "betonline": -234, 
        "bodog": -250, 
        "bumbet": -250, 
        "caesars": -235, 
        "intertops": -240, 
        "mirage": -250, 
        "mybookie": -255, 
        "opening": -188, 
        "station": -265, 
        "westgate": -240, 
        "wynn": -250
      }, 
      "short_name": "VGK", 
      "win_probability": 0.7061921760842577
    }
  }, 
  {
    "datetime": "2022-01-08 22:30:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "Detroit", 
      "logo": "../../../img/nhl-logos/Detroit.png", 
      "money_multiplier": 2.24, 
      "odds": {
        "betonline": 124, 
        "bodog": 115, 
        "bumbet": 115, 
        "caesars": 115, 
        "intertops": 115, 
        "mirage": 115, 
        "mybookie": 120, 
        "opening": 122, 
        "station": 110, 
        "westgate": 122, 
        "wynn": 115
      }, 
      "short_name": "DET", 
      "win_probability": 0.46079664340763704
    }, 
    "team_2": {
      "full_name": "Los Angeles", 
      "logo": "../../../img/nhl-logos/Los Angeles.png", 
      "money_multiplier": 1.7692307692307692, 
      "odds": {
        "betonline": -137, 
        "bodog": -135, 
        "bumbet": -135, 
        "caesars": -135, 
        "intertops": -135, 
        "mirage": -135, 
        "mybookie": -140, 
        "opening": -135, 
        "station": -130, 
        "westgate": -132, 
        "wynn": -135
      }, 
      "short_name": "LA", 
      "win_probability": 0.5742592644866998
    }
  }, 
  {
    "datetime": "2022-01-09 14:00:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "Dallas", 
      "logo": "../../../img/nhl-logos/Dallas.png", 
      "money_multiplier": 2.15, 
      "odds": {
        "betonline": None, 
        "bodog": None, 
        "bumbet": None, 
        "caesars": None, 
        "intertops": None, 
        "mirage": None, 
        "mybookie": None, 
        "opening": 115, 
        "station": None, 
        "westgate": None, 
        "wynn": None
      }, 
      "short_name": "DAL", 
      "win_probability": 0.46511627906976744
    }, 
    "team_2": {
      "full_name": "St. Louis", 
      "logo": "../../../img/nhl-logos/St. Louis.png", 
      "money_multiplier": 1.7092198581560283, 
      "odds": {
        "betonline": None, 
        "bodog": None, 
        "bumbet": None, 
        "caesars": None, 
        "intertops": None, 
        "mirage": None, 
        "mybookie": None, 
        "opening": -141, 
        "station": None, 
        "westgate": None, 
        "wynn": None
      }, 
      "short_name": "STL", 
      "win_probability": 0.5850622406639004
    }
  }, 
  {
    "datetime": "2022-01-09 20:00:00", 
    "sport": "nhl", 
    "team_1": {
      "full_name": "Detroit", 
      "logo": "../../../img/nhl-logos/Detroit.png", 
      "money_multiplier": 2.15, 
      "odds": {
        "betonline": None, 
        "bodog": None, 
        "bumbet": None, 
        "caesars": None, 
        "intertops": None, 
        "mirage": None, 
        "mybookie": None, 
        "opening": 115, 
        "station": None, 
        "westgate": None, 
        "wynn": None
      }, 
      "short_name": "DET", 
      "win_probability": 0.46511627906976744
    }, 
    "team_2": {
      "full_name": "Anaheim", 
      "logo": "../../../img/nhl-logos/Anaheim.png", 
      "money_multiplier": 1.6802721088435375, 
      "odds": {
        "betonline": None, 
        "bodog": None, 
        "bumbet": None, 
        "caesars": None, 
        "intertops": None, 
        "mirage": None, 
        "mybookie": None, 
        "opening": -147, 
        "station": None, 
        "westgate": None, 
        "wynn": None
      }, 
      "short_name": "ANA", 
      "win_probability": 0.5951417004048583
    }
  }
],
		
        "ufc": [
  {
    "datetime": "2022-01-15 19:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Calvin Kattar", 
      "logo": "../../../img/ufc-logos/Calvin Kattar.png", 
      "money_multiplier": 3.05, 
      "odds": {
        "betonline": 198, 
        "bodog": 195, 
        "bumbet": 195, 
        "intertops": 180, 
        "mybookie": 205, 
        "opening": 182
      }, 
      "short_name": "", 
      "win_probability": 0.34219303502891013
    }, 
    "team_2": {
      "full_name": "Giga Chikadze", 
      "logo": "../../../img/ufc-logos/Giga Chikadze.png", 
      "money_multiplier": 1.4587155963302751, 
      "odds": {
        "betonline": -233, 
        "bodog": -250, 
        "bumbet": -250, 
        "intertops": -240, 
        "mybookie": -245, 
        "opening": -218
      }, 
      "short_name": "", 
      "win_probability": 0.7049721666572509
    }
  }, 
  {
    "datetime": "2022-01-15 19:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Michel Pereira", 
      "logo": "../../../img/ufc-logos/Michel Pereira.png", 
      "money_multiplier": 2.2, 
      "odds": {
        "betonline": -123, 
        "bodog": -115, 
        "bumbet": -115, 
        "intertops": -125, 
        "mybookie": -125, 
        "opening": 120
      }, 
      "short_name": "", 
      "win_probability": 0.531165585707248
    }, 
    "team_2": {
      "full_name": "Muslim Salikhov", 
      "logo": "../../../img/ufc-logos/Muslim Salikhov.png", 
      "money_multiplier": 2.03, 
      "odds": {
        "betonline": 103, 
        "bodog": -105, 
        "bumbet": -105, 
        "intertops": -105, 
        "mybookie": -105, 
        "opening": -140
      }, 
      "short_name": "", 
      "win_probability": 0.5207874430961058
    }
  }, 
  {
    "datetime": "2022-01-15 19:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Katlyn Chookagian", 
      "logo": "../../../img/ufc-logos/Katlyn Chookagian.png", 
      "money_multiplier": 1.6896551724137931, 
      "odds": {
        "betonline": -170, 
        "bodog": -175, 
        "bumbet": -175, 
        "intertops": -180, 
        "mybookie": -180, 
        "opening": -145
      }, 
      "short_name": "", 
      "win_probability": 0.6299846537941776
    }, 
    "team_2": {
      "full_name": "Jennifer Maia", 
      "logo": "../../../img/ufc-logos/Jennifer Maia.png", 
      "money_multiplier": 2.5, 
      "odds": {
        "betonline": 145, 
        "bodog": 145, 
        "bumbet": 145, 
        "intertops": 140, 
        "mybookie": 150, 
        "opening": 125
      }, 
      "short_name": "", 
      "win_probability": 0.4142668178382464
    }
  }, 
  {
    "datetime": "2022-01-15 19:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Rogerio Bontorin", 
      "logo": "../../../img/ufc-logos/Rogerio Bontorin.png", 
      "money_multiplier": 2.4, 
      "odds": {
        "betonline": 135, 
        "bodog": 136, 
        "bumbet": 136, 
        "intertops": 130, 
        "mybookie": 140, 
        "opening": -110
      }, 
      "short_name": "", 
      "win_probability": 0.4413747235306839
    }, 
    "team_2": {
      "full_name": "Brandon Royval", 
      "logo": "../../../img/ufc-logos/Brandon Royval.png", 
      "money_multiplier": 1.9090909090909092, 
      "odds": {
        "betonline": -155, 
        "bodog": -170, 
        "bumbet": -170, 
        "intertops": -165, 
        "mybookie": -170, 
        "opening": -110
      }, 
      "short_name": "", 
      "win_probability": 0.6071971765645462
    }
  }, 
  {
    "datetime": "2022-01-15 19:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Jake Collier", 
      "logo": "../../../img/ufc-logos/Jake Collier.png", 
      "money_multiplier": 1.9523809523809523, 
      "odds": {
        "betonline": -125, 
        "bodog": -130, 
        "bumbet": -130, 
        "intertops": -130, 
        "mybookie": -125, 
        "opening": -105
      }, 
      "short_name": "", 
      "win_probability": 0.5531597344958956
    }, 
    "team_2": {
      "full_name": "Chase Sherman", 
      "logo": "../../../img/ufc-logos/Chase Sherman.png", 
      "money_multiplier": 2.1, 
      "odds": {
        "betonline": 105, 
        "bodog": 110, 
        "bumbet": 110, 
        "intertops": 100, 
        "mybookie": -105, 
        "opening": -115
      }, 
      "short_name": "", 
      "win_probability": 0.49787744555186414
    }
  }, 
  {
    "datetime": "2022-01-15 19:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Bill Algeo", 
      "logo": "../../../img/ufc-logos/Bill Algeo.png", 
      "money_multiplier": 2.1, 
      "odds": {
        "betonline": 110, 
        "bodog": 109, 
        "bumbet": 109, 
        "intertops": 100, 
        "mybookie": 100, 
        "opening": 105
      }, 
      "short_name": "", 
      "win_probability": 0.48682219221371986
    }, 
    "team_2": {
      "full_name": "Joanderson Brito", 
      "logo": "../../../img/ufc-logos/Joanderson Brito.png", 
      "money_multiplier": 1.7692307692307692, 
      "odds": {
        "betonline": -130, 
        "bodog": -130, 
        "bumbet": -130, 
        "intertops": -130, 
        "mybookie": -130, 
        "opening": -133
      }, 
      "short_name": "", 
      "win_probability": 0.5661504011942525
    }
  }, 
  {
    "datetime": "2022-01-15 16:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Joseph Holmes", 
      "logo": "../../../img/ufc-logos/Joseph Holmes.png", 
      "money_multiplier": 1.6451612903225807, 
      "odds": {
        "betonline": -156, 
        "bodog": -155, 
        "bumbet": -155, 
        "intertops": -160, 
        "mybookie": -160, 
        "opening": -175
      }, 
      "short_name": "", 
      "win_probability": 0.6153656902737785
    }, 
    "team_2": {
      "full_name": "Jamie Pickett", 
      "logo": "../../../img/ufc-logos/Jamie Pickett.png", 
      "money_multiplier": 2.5, 
      "odds": {
        "betonline": 136, 
        "bodog": 130, 
        "bumbet": 130, 
        "intertops": 125, 
        "mybookie": 130, 
        "opening": 150
      }, 
      "short_name": "", 
      "win_probability": 0.42875351401512046
    }
  }, 
  {
    "datetime": "2022-01-15 16:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Ramiz Brahimaj", 
      "logo": "../../../img/ufc-logos/Ramiz Brahimaj.png", 
      "money_multiplier": 2.05, 
      "odds": {
        "betonline": -102, 
        "bodog": 105, 
        "bumbet": 105, 
        "intertops": -110, 
        "mybookie": -110, 
        "opening": 100
      }, 
      "short_name": "", 
      "win_probability": 0.5046965497943522
    }, 
    "team_2": {
      "full_name": "Court Mcgee", 
      "logo": "../../../img/ufc-logos/Court Mcgee.png", 
      "money_multiplier": 1.847457627118644, 
      "odds": {
        "betonline": -118, 
        "bodog": -125, 
        "bumbet": -125, 
        "intertops": -120, 
        "mybookie": -120, 
        "opening": -120
      }, 
      "short_name": "", 
      "win_probability": 0.5481265251907453
    }
  }, 
  {
    "datetime": "2022-01-15 16:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Gabriel Benitez", 
      "logo": "../../../img/ufc-logos/Gabriel Benitez.png", 
      "money_multiplier": 1.6896551724137931, 
      "odds": {
        "betonline": -177, 
        "bodog": -185, 
        "bumbet": -185, 
        "intertops": -190, 
        "mybookie": -190, 
        "opening": -145
      }, 
      "short_name": "", 
      "win_probability": 0.6399027243317104
    }, 
    "team_2": {
      "full_name": "TJ Brown", 
      "logo": "../../../img/ufc-logos/TJ Brown.png", 
      "money_multiplier": 2.55, 
      "odds": {
        "betonline": 152, 
        "bodog": 150, 
        "bumbet": 150, 
        "intertops": 150, 
        "mybookie": 155, 
        "opening": 125
      }, 
      "short_name": "", 
      "win_probability": 0.4055711173358232
    }
  }, 
  {
    "datetime": "2022-01-15 16:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Viacheslav Borshchev", 
      "logo": "../../../img/ufc-logos/Viacheslav Borshchev.png", 
      "money_multiplier": 1.5555555555555556, 
      "odds": {
        "betonline": -180, 
        "bodog": -200, 
        "bumbet": -200, 
        "intertops": -180, 
        "mybookie": -185, 
        "opening": -200
      }, 
      "short_name": "", 
      "win_probability": 0.6558061821219715
    }, 
    "team_2": {
      "full_name": "Dakota Bush", 
      "logo": "../../../img/ufc-logos/Dakota Bush.png", 
      "money_multiplier": 2.7, 
      "odds": {
        "betonline": 155, 
        "bodog": 160, 
        "bumbet": 160, 
        "intertops": 140, 
        "mybookie": 155, 
        "opening": 170
      }, 
      "short_name": "", 
      "win_probability": 0.39009692195966705
    }
  }, 
  {
    "datetime": "2022-01-15 16:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Saidyokub Kakhramonov", 
      "logo": "../../../img/ufc-logos/Saidyokub Kakhramonov.png", 
      "money_multiplier": 1.6369426751592357, 
      "odds": {
        "betonline": -157, 
        "bodog": -165, 
        "bumbet": -165, 
        "intertops": -160, 
        "mybookie": -165, 
        "opening": -170
      }, 
      "short_name": "", 
      "win_probability": 0.6206389524917288
    }, 
    "team_2": {
      "full_name": "Brian Kelleher", 
      "logo": "../../../img/ufc-logos/Brian Kelleher.png", 
      "money_multiplier": 2.45, 
      "odds": {
        "betonline": 137, 
        "bodog": 135, 
        "bumbet": 135, 
        "intertops": 125, 
        "mybookie": 135, 
        "opening": 145
      }, 
      "short_name": "", 
      "win_probability": 0.42519073045024336
    }
  }, 
  {
    "datetime": "2022-01-15 16:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Vanessa Demopoulos", 
      "logo": "../../../img/ufc-logos/Vanessa Demopoulos.png", 
      "money_multiplier": 2.0, 
      "odds": {
        "betonline": -130, 
        "bodog": -130, 
        "bumbet": -130, 
        "intertops": -115, 
        "mybookie": -130, 
        "opening": 100
      }, 
      "short_name": "", 
      "win_probability": 0.5492922143579372
    }, 
    "team_2": {
      "full_name": "Silvana Gomez Juarez", 
      "logo": "../../../img/ufc-logos/Silvana Gomez Juarez.png", 
      "money_multiplier": 2.1, 
      "odds": {
        "betonline": 110, 
        "bodog": 110, 
        "bumbet": 110, 
        "intertops": -115, 
        "mybookie": 100, 
        "opening": -125
      }, 
      "short_name": "", 
      "win_probability": 0.5031684508428694
    }
  }, 
  {
    "datetime": "2022-01-22 22:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Francis Ngannou", 
      "logo": "../../../img/ufc-logos/Francis Ngannou.png", 
      "money_multiplier": 1.9615384615384615, 
      "odds": {
        "betonline": -104, 
        "bodog": -105, 
        "bumbet": -105, 
        "intertops": -115, 
        "mybookie": None, 
        "opening": -125
      }, 
      "short_name": "", 
      "win_probability": 0.5249266883913709
    }, 
    "team_2": {
      "full_name": "Ciryl Gane", 
      "logo": "../../../img/ufc-logos/Ciryl Gane.png", 
      "money_multiplier": 2.0, 
      "odds": {
        "betonline": -116, 
        "bodog": -115, 
        "bumbet": -115, 
        "intertops": -115, 
        "mybookie": None, 
        "opening": 100
      }, 
      "short_name": "", 
      "win_probability": 0.5283376399655471
    }
  }, 
  {
    "datetime": "2022-01-22 22:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Deiveson Figueiredo", 
      "logo": "../../../img/ufc-logos/Deiveson Figueiredo.png", 
      "money_multiplier": 2.46, 
      "odds": {
        "betonline": 146, 
        "bodog": 145, 
        "bumbet": 145, 
        "intertops": 135, 
        "mybookie": None, 
        "opening": 140
      }, 
      "short_name": "", 
      "win_probability": 0.41300583544263586
    }, 
    "team_2": {
      "full_name": "Brandon Moreno", 
      "logo": "../../../img/ufc-logos/Brandon Moreno.png", 
      "money_multiplier": 1.5847953216374269, 
      "odds": {
        "betonline": -171, 
        "bodog": -175, 
        "bumbet": -175, 
        "intertops": -175, 
        "mybookie": None, 
        "opening": -175
      }, 
      "short_name": "", 
      "win_probability": 0.635290171083529
    }
  }, 
  {
    "datetime": "2022-01-22 22:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Movsar Evloev", 
      "logo": "../../../img/ufc-logos/Movsar Evloev.png", 
      "money_multiplier": 2.5, 
      "odds": {
        "betonline": -110, 
        "bodog": -104, 
        "bumbet": -104, 
        "intertops": -115, 
        "mybookie": None, 
        "opening": 150
      }, 
      "short_name": "", 
      "win_probability": 0.49566021757540224
    }, 
    "team_2": {
      "full_name": "Ilia Topuria", 
      "logo": "../../../img/ufc-logos/Ilia Topuria.png", 
      "money_multiplier": 1.9090909090909092, 
      "odds": {
        "betonline": -110, 
        "bodog": -120, 
        "bumbet": -120, 
        "intertops": -115, 
        "mybookie": None, 
        "opening": -175
      }, 
      "short_name": "", 
      "win_probability": 0.5571931944024967
    }
  }, 
  {
    "datetime": "2022-01-22 22:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Aleksei Oleinik", 
      "logo": "../../../img/ufc-logos/Aleksei Oleinik.png", 
      "money_multiplier": 2.5, 
      "odds": {
        "betonline": 150, 
        "bodog": 140, 
        "bumbet": 140, 
        "intertops": 135, 
        "mybookie": None, 
        "opening": -140
      }, 
      "short_name": "", 
      "win_probability": 0.4484397163120568
    }, 
    "team_2": {
      "full_name": "Greg Hardy", 
      "logo": "../../../img/ufc-logos/Greg Hardy.png", 
      "money_multiplier": 2.2, 
      "odds": {
        "betonline": -175, 
        "bodog": -170, 
        "bumbet": -170, 
        "intertops": -175, 
        "mybookie": None, 
        "opening": 120
      }, 
      "short_name": "", 
      "win_probability": 0.5973063973063972
    }
  }, 
  {
    "datetime": "2022-01-22 22:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Cody Stamann", 
      "logo": "../../../img/ufc-logos/Cody Stamann.png", 
      "money_multiplier": 3.1, 
      "odds": {
        "betonline": 170, 
        "bodog": 165, 
        "bumbet": 165, 
        "intertops": 160, 
        "mybookie": None, 
        "opening": 210
      }, 
      "short_name": "", 
      "win_probability": 0.3664566762558241
    }, 
    "team_2": {
      "full_name": "Said Nurmagomedov", 
      "logo": "../../../img/ufc-logos/Said Nurmagomedov.png", 
      "money_multiplier": 1.5, 
      "odds": {
        "betonline": -200, 
        "bodog": -200, 
        "bumbet": -200, 
        "intertops": -200, 
        "mybookie": None, 
        "opening": -245
      }, 
      "short_name": "", 
      "win_probability": 0.6753623188405796
    }
  }, 
  {
    "datetime": "2022-01-22 20:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Alexa Grasso", 
      "logo": "../../../img/ufc-logos/Alexa Grasso.png", 
      "money_multiplier": 1.6451612903225807, 
      "odds": {
        "betonline": -185, 
        "bodog": -175, 
        "bumbet": -175, 
        "intertops": -175, 
        "mybookie": None, 
        "opening": -155
      }, 
      "short_name": "", 
      "win_probability": 0.633211370672671
    }, 
    "team_2": {
      "full_name": "Viviane Araujo", 
      "logo": "../../../img/ufc-logos/Viviane Araujo.png", 
      "money_multiplier": 2.6, 
      "odds": {
        "betonline": 160, 
        "bodog": 145, 
        "bumbet": 145, 
        "intertops": 135, 
        "mybookie": None, 
        "opening": 135
      }, 
      "short_name": "", 
      "win_probability": 0.4104011490029727
    }
  }, 
  {
    "datetime": "2022-01-22 20:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Wellington Turman", 
      "logo": "../../../img/ufc-logos/Wellington Turman.png", 
      "money_multiplier": 3.85, 
      "odds": {
        "betonline": 225, 
        "bodog": 220, 
        "bumbet": 220, 
        "intertops": 220, 
        "mybookie": None, 
        "opening": 285
      }, 
      "short_name": "", 
      "win_probability": 0.30098651348651345
    }, 
    "team_2": {
      "full_name": "Rodolfo Vieira", 
      "logo": "../../../img/ufc-logos/Rodolfo Vieira.png", 
      "money_multiplier": 1.3773584905660377, 
      "odds": {
        "betonline": -265, 
        "bodog": -275, 
        "bumbet": -275, 
        "intertops": -290, 
        "mybookie": None, 
        "opening": -350
      }, 
      "short_name": "", 
      "win_probability": 0.7428123170588924
    }
  }, 
  {
    "datetime": "2022-01-22 20:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Tony Gravely", 
      "logo": "../../../img/ufc-logos/Tony Gravely.png", 
      "money_multiplier": 1.4166666666666667, 
      "odds": {
        "betonline": -250, 
        "bodog": -250, 
        "bumbet": -250, 
        "intertops": -240, 
        "mybookie": None, 
        "opening": -250
      }, 
      "short_name": "", 
      "win_probability": 0.7126050420168067
    }, 
    "team_2": {
      "full_name": "Saimon Oliveira", 
      "logo": "../../../img/ufc-logos/Saimon Oliveira.png", 
      "money_multiplier": 3.1, 
      "odds": {
        "betonline": 210, 
        "bodog": 200, 
        "bumbet": 200, 
        "intertops": 180, 
        "mybookie": None, 
        "opening": 185
      }, 
      "short_name": "", 
      "win_probability": 0.33945347239065404
    }
  }, 
  {
    "datetime": "2022-01-22 20:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Warlley Alves", 
      "logo": "../../../img/ufc-logos/Warlley Alves.png", 
      "money_multiplier": 2.65, 
      "odds": {
        "betonline": 165, 
        "bodog": 150, 
        "bumbet": 150, 
        "intertops": 160, 
        "mybookie": None, 
        "opening": 155
      }, 
      "short_name": "", 
      "win_probability": 0.3908261475853041
    }, 
    "team_2": {
      "full_name": "Jack Della Maddalena", 
      "logo": "../../../img/ufc-logos/Jack Della Maddalena.png", 
      "money_multiplier": 1.5555555555555556, 
      "odds": {
        "betonline": -190, 
        "bodog": -185, 
        "bumbet": -185, 
        "intertops": -200, 
        "mybookie": None, 
        "opening": -180
      }, 
      "short_name": "", 
      "win_probability": 0.6525883674704002
    }
  }, 
  {
    "datetime": "2022-01-22 18:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Poliana Botelho", 
      "logo": "../../../img/ufc-logos/Poliana Botelho.png", 
      "money_multiplier": 2.4, 
      "odds": {
        "betonline": 115, 
        "bodog": 115, 
        "bumbet": 115, 
        "intertops": 105, 
        "mybookie": None, 
        "opening": 140
      }, 
      "short_name": "", 
      "win_probability": 0.45996407638494985
    }, 
    "team_2": {
      "full_name": "Kim Ji Yeon", 
      "logo": "../../../img/ufc-logos/Kim Ji Yeon.png", 
      "money_multiplier": 1.7407407407407407, 
      "odds": {
        "betonline": -135, 
        "bodog": -140, 
        "bumbet": -140, 
        "intertops": -135, 
        "mybookie": None, 
        "opening": -160
      }, 
      "short_name": "", 
      "win_probability": 0.5861974904528097
    }
  }, 
  
  {
    "datetime": "2022-01-22 18:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Trevin Giles", 
      "logo": "../../../img/ufc-logos/Trevin Giles.png", 
      "money_multiplier": 2.35, 
      "odds": {
        "betonline": 119, 
        "bodog": 119, 
        "bumbet": 119, 
        "intertops": 110, 
        "mybookie": None, 
        "opening": 135
      }, 
      "short_name": "", 
      "win_probability": 0.45431708095654466
    }, 
    "team_2": {
      "full_name": "Michael Morales", 
      "logo": "../../../img/ufc-logos/Michael Morales.png", 
      "money_multiplier": 1.7194244604316546, 
      "odds": {
        "betonline": -139, 
        "bodog": -148, 
        "bumbet": -148, 
        "intertops": -140, 
        "mybookie": None, 
        "opening": -155
      }, 
      "short_name": "", 
      "win_probability": 0.5932629631688011
    }
  }, 
  {
    "datetime": "2022-01-22 18:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Matt Frevola", 
      "logo": "../../../img/ufc-logos/Matt Frevola.png", 
      "money_multiplier": 2.1, 
      "odds": {
        "betonline": -225, 
        "bodog": -220, 
        "bumbet": -220, 
        "intertops": -220, 
        "mybookie": None, 
        "opening": 110
      }, 
      "short_name": "", 
      "win_probability": 0.6461996336996337
    }, 
    "team_2": {
      "full_name": "Genaro Valdez", 
      "logo": "../../../img/ufc-logos/Genaro Valdez.png", 
      "money_multiplier": 2.9, 
      "odds": {
        "betonline": 190, 
        "bodog": 175, 
        "bumbet": 175, 
        "intertops": 170, 
        "mybookie": None, 
        "opening": -130
      }, 
      "short_name": "", 
      "win_probability": 0.40153761503086843
    }
  }, 
  {
    "datetime": "2022-01-22 18:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Kay Hansen", 
      "logo": "../../../img/ufc-logos/Kay Hansen.png", 
      "money_multiplier": 1.8695652173913044, 
      "odds": {
        "betonline": -260, 
        "bodog": -230, 
        "bumbet": -230, 
        "intertops": -250, 
        "mybookie": None, 
        "opening": -115
      }, 
      "short_name": "", 
      "win_probability": 0.6730662102755126
    }, 
    "team_2": {
      "full_name": "Jasmine Jasudavicius", 
      "logo": "../../../img/ufc-logos/Jasmine Jasudavicius.png", 
      "money_multiplier": 3.2, 
      "odds": {
        "betonline": 220, 
        "bodog": 185, 
        "bumbet": 185, 
        "intertops": 190, 
        "mybookie": None, 
        "opening": -105
      }, 
      "short_name": "", 
      "win_probability": 0.37425541882460567
    }
  }, 
  {
    "datetime": "2022-02-05 22:00:00", 
    "sport": "ufc", 
    "team_1": {
      "full_name": "Jack Hermansson", 
      "logo": "../../../img/ufc-logos/Jack Hermansson.png", 
      "money_multiplier": 2.75, 
      "odds": {
        "betonline": 175, 
        "bodog": 160, 
        "bumbet": 160, 
        "intertops": 165, 
        "mybookie": None, 
        "opening": 170
      }, 
      "short_name": "", 
      "win_probability": 0.37611919876070815
    }, 
    "team_2": {
      "full_name": "Sean Strickland", 
      "logo": "../../../img/ufc-logos/Sean Strickland.png", 
      "money_multiplier": 1.5128205128205128, 
      "odds": {
        "betonline": -205, 
        "bodog": -200, 
        "bumbet": -200, 
        "intertops": -210, 
        "mybookie": None, 
        "opening": -195
      }, 
      "short_name": "", 
      "win_probability": 0.6687801569731138
    }
  }
  ],

		"ncaab": [
  {
    "datetime": "2022-01-08 00:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Purdue", 
      "logo": "../../../img/ncaab-logos/Purdue.png", 
      "money_multiplier": 1.2, 
      "odds": {
        "betonline": -525, 
        "bovada": -500, 
        "mybookie": -525, 
        "opening": -500, 
        "sportsbetting": -525
      }, 
      "short_name": "PUR", 
      "win_probability": 0.8373333333333333
    }, 
    "team_2": {
      "full_name": "Penn State", 
      "logo": "../../../img/ncaab-logos/Penn State.png", 
      "money_multiplier": 5.2, 
      "odds": {
        "betonline": 420, 
        "bovada": 360, 
        "mybookie": 350, 
        "opening": 350, 
        "sportsbetting": 420
      }, 
      "short_name": "PSU", 
      "win_probability": 0.209290226681531
    }
  }, 
  {
    "datetime": "2022-01-08 00:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Clemson", 
      "logo": "../../../img/ncaab-logos/Clemson.png", 
      "money_multiplier": 2.1, 
      "odds": {
        "betonline": 103, 
        "bovada": 110, 
        "mybookie": 105, 
        "opening": -118, 
        "sportsbetting": 103
      }, 
      "short_name": "CLEM", 
      "win_probability": 0.4981002865571657
    }, 
    "team_2": {
      "full_name": "North Carolina State", 
      "logo": "../../../img/ncaab-logos/North Carolina State.png", 
      "money_multiplier": 1.8130081300813008, 
      "odds": {
        "betonline": -123, 
        "bovada": -130, 
        "mybookie": -125, 
        "opening": -125, 
        "sportsbetting": -123
      }, 
      "short_name": "NCSU", 
      "win_probability": 0.5558935031736748
    }
  }, 
  {
    "datetime": "2022-01-08 00:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "St. John's", 
      "logo": "../../../img/ncaab-logos/St. John's.png", 
      "money_multiplier": 2.45, 
      "odds": {
        "betonline": 144, 
        "bovada": 140, 
        "mybookie": 145, 
        "opening": 140, 
        "sportsbetting": 144
      }, 
      "short_name": "SJU", 
      "win_probability": 0.4122337459573993
    }, 
    "team_2": {
      "full_name": "Providence", 
      "logo": "../../../img/ncaab-logos/Providence.png", 
      "money_multiplier": 1.6097560975609757, 
      "odds": {
        "betonline": -164, 
        "bovada": -165, 
        "mybookie": -175, 
        "opening": -200, 
        "sportsbetting": -164
      }, 
      "short_name": "PROV", 
      "win_probability": 0.6336192109777015
    }
  }, 
  {
    "datetime": "2022-01-08 00:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Connecticut", 
      "logo": "../../../img/ncaab-logos/Connecticut.png", 
      "money_multiplier": 2.65, 
      "odds": {
        "betonline": 151, 
        "bovada": 155, 
        "mybookie": 165, 
        "opening": 130, 
        "sportsbetting": 151
      }, 
      "short_name": "UCONN", 
      "win_probability": 0.40022214220215435
    }, 
    "team_2": {
      "full_name": "Seton Hall", 
      "logo": "../../../img/ncaab-logos/Seton Hall.png", 
      "money_multiplier": 1.5847953216374269, 
      "odds": {
        "betonline": -171, 
        "bovada": -180, 
        "mybookie": -195, 
        "opening": -182, 
        "sportsbetting": -171
      }, 
      "short_name": "SETON", 
      "win_probability": 0.6422513565715742
    }
  }, 
  {
    "datetime": "2022-01-08 00:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Dayton", 
      "logo": "../../../img/ncaab-logos/Dayton.png", 
      "money_multiplier": 1.2941176470588236, 
      "odds": {
        "betonline": -360, 
        "bovada": -340, 
        "mybookie": -355, 
        "opening": -400, 
        "sportsbetting": -360
      }, 
      "short_name": "DAY", 
      "win_probability": 0.7836328888502802
    }, 
    "team_2": {
      "full_name": "George Washington", 
      "logo": "../../../img/ncaab-logos/George Washington.png", 
      "money_multiplier": 3.95, 
      "odds": {
        "betonline": 290, 
        "bovada": 270, 
        "mybookie": 295, 
        "opening": 250, 
        "sportsbetting": 290
      }, 
      "short_name": "GWU", 
      "win_probability": 0.2643939251534188
    }
  }, 
  {
    "datetime": "2022-01-08 00:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Duquesne", 
      "logo": "../../../img/ncaab-logos/Duquesne.png", 
      "money_multiplier": 2.64, 
      "odds": {
        "betonline": 164, 
        "bovada": 150, 
        "mybookie": 155, 
        "opening": 150, 
        "sportsbetting": 164
      }, 
      "short_name": "DUQ", 
      "win_probability": 0.38994652406417113
    }, 
    "team_2": {
      "full_name": "UMass", 
      "logo": "../../../img/ncaab-logos/UMass.png", 
      "money_multiplier": 1.5714285714285714, 
      "odds": {
        "betonline": -184, 
        "bovada": -175, 
        "mybookie": -185, 
        "opening": -200, 
        "sportsbetting": -184
      }, 
      "short_name": "UMASS", 
      "win_probability": 0.6495855515870341
    }
  }, 
  {
    "datetime": "2022-01-08 00:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "South Carolina", 
      "logo": "../../../img/ncaab-logos/South Carolina.png", 
      "money_multiplier": 3.8, 
      "odds": {
        "betonline": 275, 
        "bovada": 255, 
        "mybookie": 280, 
        "opening": 180, 
        "sportsbetting": 275
      }, 
      "short_name": "SCAR", 
      "win_probability": 0.28706484521162057
    }, 
    "team_2": {
      "full_name": "Vanderbilt", 
      "logo": "../../../img/ncaab-logos/Vanderbilt.png", 
      "money_multiplier": 1.3496503496503496, 
      "odds": {
        "betonline": -330, 
        "bovada": -310, 
        "mybookie": -330, 
        "opening": -286, 
        "sportsbetting": -330
      }, 
      "short_name": "VANDY", 
      "win_probability": 0.7598711569716011
    }
  }, 
  {
    "datetime": "2022-01-08 00:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Wichita State", 
      "logo": "../../../img/ncaab-logos/Wichita State.png", 
      "money_multiplier": 8.5, 
      "odds": {
        "betonline": 545, 
        "bovada": 525, 
        "mybookie": 535, 
        "opening": 750, 
        "sportsbetting": 545
      }, 
      "short_name": "WICH", 
      "win_probability": 0.14904097863280086
    }, 
    "team_2": {
      "full_name": "Houston", 
      "logo": "../../../img/ncaab-logos/Houston.png", 
      "money_multiplier": 1.1379310344827587, 
      "odds": {
        "betonline": -725, 
        "bovada": -800, 
        "mybookie": -750, 
        "opening": -1429, 
        "sportsbetting": -725
      }, 
      "short_name": "HOU", 
      "win_probability": 0.8926830727931024
    }
  }, 
  {
    "datetime": "2022-01-08 13:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "North Dakota State", 
      "logo": "../../../img/ncaab-logos/North Dakota State.png", 
      "money_multiplier": 1.2, 
      "odds": {
        "betonline": -500, 
        "bovada": -530, 
        "mybookie": -535, 
        "opening": -500, 
        "sportsbetting": -500
      }, 
      "short_name": "NDST", 
      "win_probability": 0.8367579052618422
    }, 
    "team_2": {
      "full_name": "Nebraska-Omaha", 
      "logo": "../../../img/ncaab-logos/Nebraska-Omaha.png", 
      "money_multiplier": 4.95, 
      "odds": {
        "betonline": 395, 
        "bovada": 380, 
        "mybookie": 360, 
        "opening": 325, 
        "sportsbetting": 395
      }, 
      "short_name": "OMAHA", 
      "win_probability": 0.21301183187372447
    }
  }, 
  {
    "datetime": "2022-01-08 13:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Cal Baptist", 
      "logo": "../../../img/ncaab-logos/Cal Baptist.png", 
      "money_multiplier": 1.2, 
      "odds": {
        "betonline": -635, 
        "bovada": -655, 
        "mybookie": -690, 
        "opening": -500, 
        "sportsbetting": -635
      }, 
      "short_name": "CALBAP", 
      "win_probability": 0.8604383760378156
    }, 
    "team_2": {
      "full_name": "Chicago State", 
      "logo": "../../../img/ncaab-logos/Chicago State.png", 
      "money_multiplier": 5.95, 
      "odds": {
        "betonline": 495, 
        "bovada": 445, 
        "mybookie": 440, 
        "opening": 325, 
        "sportsbetting": 495
      }, 
      "short_name": "CHIST", 
      "win_probability": 0.18801999902917332
    }
  }, 
  {
    "datetime": "2022-01-08 13:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Arkansas", 
      "logo": "../../../img/ncaab-logos/Arkansas.png", 
      "money_multiplier": 1.847457627118644, 
      "odds": {
        "betonline": -133, 
        "bovada": -130, 
        "mybookie": -125, 
        "opening": -118, 
        "sportsbetting": -133
      }, 
      "short_name": "ARK", 
      "win_probability": 0.5607376503634363
    }, 
    "team_2": {
      "full_name": "Texas A&M", 
      "logo": "../../../img/ncaab-logos/Texas A&M.png", 
      "money_multiplier": 2.13, 
      "odds": {
        "betonline": 113, 
        "bovada": 110, 
        "mybookie": 105, 
        "opening": -125, 
        "sportsbetting": 113
      }, 
      "short_name": "TEXAM", 
      "win_probability": 0.4917036091890094
    }
  }, 
  {
    "datetime": "2022-01-08 13:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "UNC Greensboro", 
      "logo": "../../../img/ncaab-logos/UNC Greensboro.png", 
      "money_multiplier": 2.65, 
      "odds": {
        "betonline": 158, 
        "bovada": 165, 
        "mybookie": 165, 
        "opening": 160, 
        "sportsbetting": 158
      }, 
      "short_name": "UNCG", 
      "win_probability": 0.3829052328394146
    }, 
    "team_2": {
      "full_name": "VMI", 
      "logo": "../../../img/ncaab-logos/VMI.png", 
      "money_multiplier": 1.5617977528089888, 
      "odds": {
        "betonline": -178, 
        "bovada": -195, 
        "mybookie": -195, 
        "opening": -222, 
        "sportsbetting": -178
      }, 
      "short_name": "VMI", 
      "win_probability": 0.65841008633245
    }
  }, 
  {
    "datetime": "2022-01-08 13:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Virginia", 
      "logo": "../../../img/ncaab-logos/Virginia.png", 
      "money_multiplier": 2.8, 
      "odds": {
        "betonline": 180, 
        "bovada": 180, 
        "mybookie": 180, 
        "opening": 180, 
        "sportsbetting": 180
      }, 
      "short_name": "UVA", 
      "win_probability": 0.35714285714285715
    }, 
    "team_2": {
      "full_name": "North Carolina", 
      "logo": "../../../img/ncaab-logos/North Carolina.png", 
      "money_multiplier": 1.4761904761904763, 
      "odds": {
        "betonline": -210, 
        "bovada": -220, 
        "mybookie": -210, 
        "opening": -286, 
        "sportsbetting": -210
      }, 
      "short_name": "UNC", 
      "win_probability": 0.692138141400635
    }
  }, 
  {
    "datetime": "2022-01-08 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Nebraska", 
      "logo": "../../../img/ncaab-logos/Nebraska.png", 
      "money_multiplier": 4.0, 
      "odds": {
        "betonline": 280, 
        "bovada": 275, 
        "mybookie": 290, 
        "opening": 300, 
        "sportsbetting": 280
      }, 
      "short_name": "NEB", 
      "win_probability": 0.25987854251012144
    }, 
    "team_2": {
      "full_name": "Rutgers", 
      "logo": "../../../img/ncaab-logos/Rutgers.png", 
      "money_multiplier": 1.2941176470588236, 
      "odds": {
        "betonline": -350, 
        "bovada": -350, 
        "mybookie": -340, 
        "opening": -400, 
        "sportsbetting": -350
      }, 
      "short_name": "RUT", 
      "win_probability": 0.7812121212121212
    }
  }, 
  {
    "datetime": "2022-01-08 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Northern Illinois", 
      "logo": "../../../img/ncaab-logos/Northern Illinois.png", 
      "money_multiplier": 16.0, 
      "odds": {
        "betonline": 1500, 
        "bovada": 1225, 
        "mybookie": 840, 
        "opening": 1400, 
        "sportsbetting": 1500
      }, 
      "short_name": "NIU", 
      "win_probability": 0.07470426870065569
    }, 
    "team_2": {
      "full_name": "Toledo", 
      "logo": "../../../img/ncaab-logos/Toledo.png", 
      "money_multiplier": 1.029940119760479, 
      "odds": {
        "betonline": -4000, 
        "bovada": -4100, 
        "mybookie": -3340, 
        "opening": -10000, 
        "sportsbetting": -4000
      }, 
      "short_name": "TOL", 
      "win_probability": 0.9776878461689457
    }
  }, 
  {
    "datetime": "2022-01-08 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Kansas State", 
      "logo": "../../../img/ncaab-logos/Kansas State.png", 
      "money_multiplier": 4.15, 
      "odds": {
        "betonline": 315, 
        "bovada": 290, 
        "mybookie": 310, 
        "opening": 275, 
        "sportsbetting": 315
      }, 
      "short_name": "KANST", 
      "win_probability": 0.24978141458893735
    }, 
    "team_2": {
      "full_name": "West Virginia", 
      "logo": "../../../img/ncaab-logos/West Virginia.png", 
      "money_multiplier": 1.263157894736842, 
      "odds": {
        "betonline": -385, 
        "bovada": -380, 
        "mybookie": -380, 
        "opening": -400, 
        "sportsbetting": -385
      }, 
      "short_name": "WVU", 
      "win_probability": 0.7941924398625428
    }
  }, 
  {
    "datetime": "2022-01-08 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Rhode Island", 
      "logo": "../../../img/ncaab-logos/Rhode Island.png", 
      "money_multiplier": 3.8, 
      "odds": {
        "betonline": 280, 
        "bovada": 260, 
        "mybookie": 270, 
        "opening": 190, 
        "sportsbetting": 280
      }, 
      "short_name": "RHODE", 
      "win_probability": 0.28383828474572576
    }, 
    "team_2": {
      "full_name": "Davidson", 
      "logo": "../../../img/ncaab-logos/Davidson.png", 
      "money_multiplier": 1.4, 
      "odds": {
        "betonline": -350, 
        "bovada": -320, 
        "mybookie": -320, 
        "opening": -250, 
        "sportsbetting": -350
      }, 
      "short_name": "DAVID", 
      "win_probability": 0.7587301587301587
    }
  }, 
  {
    "datetime": "2022-01-08 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "IUPUI-Indiana Purdue", 
      "logo": "../../../img/ncaab-logos/IUPUI-Indiana Purdue.png", 
      "money_multiplier": 19.0, 
      "odds": {
        "betonline": 1600, 
        "bovada": 1275, 
        "mybookie": None, 
        "opening": 1800, 
        "sportsbetting": 1600
      }, 
      "short_name": "IUPUI", 
      "win_probability": 0.06075147762454264
    }, 
    "team_2": {
      "full_name": "Wright State", 
      "logo": "../../../img/ncaab-logos/Wright State.png", 
      "money_multiplier": 1.04, 
      "odds": {
        "betonline": -6000, 
        "bovada": -5000, 
        "mybookie": None, 
        "opening": -2500, 
        "sportsbetting": -6000
      }, 
      "short_name": "WRIGH", 
      "win_probability": 0.9772859332888262
    }
  }, 
  {
    "datetime": "2022-01-08 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Texas", 
      "logo": "../../../img/ncaab-logos/Texas.png", 
      "money_multiplier": 1.6896551724137931, 
      "odds": {
        "betonline": -155, 
        "bovada": -145, 
        "mybookie": -145, 
        "opening": -222, 
        "sportsbetting": -155
      }, 
      "short_name": "TEXAS", 
      "win_probability": 0.6177601475372758
    }, 
    "team_2": {
      "full_name": "Oklahoma State", 
      "logo": "../../../img/ncaab-logos/Oklahoma State.png", 
      "money_multiplier": 2.5, 
      "odds": {
        "betonline": 135, 
        "bovada": 125, 
        "mybookie": 125, 
        "opening": 150, 
        "sportsbetting": 135
      }, 
      "short_name": "OKST", 
      "win_probability": 0.4279905437352246
    }
  }, 
  {
    "datetime": "2022-01-08 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Villanova", 
      "logo": "../../../img/ncaab-logos/Villanova.png", 
      "money_multiplier": 1.25, 
      "odds": {
        "betonline": -425, 
        "bovada": -420, 
        "mybookie": -410, 
        "opening": -400, 
        "sportsbetting": -425
      }, 
      "short_name": "NOVA", 
      "win_probability": 0.8061322990734755
    }, 
    "team_2": {
      "full_name": "DePaul", 
      "logo": "../../../img/ncaab-logos/DePaul.png", 
      "money_multiplier": 4.45, 
      "odds": {
        "betonline": 345, 
        "bovada": 315, 
        "mybookie": 330, 
        "opening": 250, 
        "sportsbetting": 345
      }, 
      "short_name": "DPU", 
      "win_probability": 0.24173489658360942
    }
  }, 
  {
    "datetime": "2022-01-08 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Syracuse", 
      "logo": "../../../img/ncaab-logos/Syracuse.png", 
      "money_multiplier": 2.65, 
      "odds": {
        "betonline": 165, 
        "bovada": 150, 
        "mybookie": 160, 
        "opening": 140, 
        "sportsbetting": 165
      }, 
      "short_name": "CUSE", 
      "win_probability": 0.3911998064828254
    }, 
    "team_2": {
      "full_name": "Wake Forest", 
      "logo": "../../../img/ncaab-logos/Wake Forest.png", 
      "money_multiplier": 1.5714285714285714, 
      "odds": {
        "betonline": -190, 
        "bovada": -175, 
        "mybookie": -190, 
        "opening": -200, 
        "sportsbetting": -190
      }, 
      "short_name": "WAKE", 
      "win_probability": 0.6537095088819227
    }
  }, 
  {
    "datetime": "2022-01-08 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "VCU", 
      "logo": "../../../img/ncaab-logos/VCU.png", 
      "money_multiplier": 1.263157894736842, 
      "odds": {
        "betonline": -385, 
        "bovada": -415, 
        "mybookie": -380, 
        "opening": -444, 
        "sportsbetting": -385
      }, 
      "short_name": "VCU", 
      "win_probability": 0.8002594491905459
    }, 
    "team_2": {
      "full_name": "La Salle", 
      "logo": "../../../img/ncaab-logos/La Salle.png", 
      "money_multiplier": 4.15, 
      "odds": {
        "betonline": 315, 
        "bovada": 310, 
        "mybookie": 310, 
        "opening": 300, 
        "sportsbetting": 315
      }, 
      "short_name": "LASAL", 
      "win_probability": 0.2439465177784308
    }
  }, 
  {
    "datetime": "2022-01-08 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "East Carolina", 
      "logo": "../../../img/ncaab-logos/East Carolina.png", 
      "money_multiplier": 2.64, 
      "odds": {
        "betonline": 164, 
        "bovada": 160, 
        "mybookie": 155, 
        "opening": 140, 
        "sportsbetting": 164
      }, 
      "short_name": "ECU", 
      "win_probability": 0.3902029343205814
    }, 
    "team_2": {
      "full_name": "Temple", 
      "logo": "../../../img/ncaab-logos/Temple.png", 
      "money_multiplier": 1.5434782608695652, 
      "odds": {
        "betonline": -184, 
        "bovada": -185, 
        "mybookie": -185, 
        "opening": -200, 
        "sportsbetting": -184
      }, 
      "short_name": "TEMP", 
      "win_probability": 0.6521373857178157
    }
  }, 
  {
    "datetime": "2022-01-08 15:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Texas-Arlington", 
      "logo": "../../../img/ncaab-logos/Texas-Arlington.png", 
      "money_multiplier": 2.3, 
      "odds": {
        "betonline": 122, 
        "bovada": 130, 
        "mybookie": 125, 
        "opening": 130, 
        "sportsbetting": 122
      }, 
      "short_name": "TEX-AR", 
      "win_probability": 0.44298211254733
    }, 
    "team_2": {
      "full_name": "Georgia Southern", 
      "logo": "../../../img/ncaab-logos/Georgia Southern.png", 
      "money_multiplier": 1.704225352112676, 
      "odds": {
        "betonline": -142, 
        "bovada": -150, 
        "mybookie": -145, 
        "opening": -167, 
        "sportsbetting": -142
      }, 
      "short_name": "GASO", 
      "win_probability": 0.5981717236992299
    }
  }, 
  {
    "datetime": "2022-01-08 15:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Arkansas State", 
      "logo": "../../../img/ncaab-logos/Arkansas State.png", 
      "money_multiplier": 1.847457627118644, 
      "odds": {
        "betonline": -125, 
        "bovada": -120, 
        "mybookie": None, 
        "opening": -118, 
        "sportsbetting": -125
      }, 
      "short_name": "ARKST", 
      "win_probability": 0.5494625150588454
    }, 
    "team_2": {
      "full_name": "Louisiana-Monroe", 
      "logo": "../../../img/ncaab-logos/Louisiana-Monroe.png", 
      "money_multiplier": 2.05, 
      "odds": {
        "betonline": 105, 
        "bovada": 100, 
        "mybookie": None, 
        "opening": -125, 
        "sportsbetting": 105
      }, 
      "short_name": "ULM", 
      "win_probability": 0.5077913279132791
    }
  }, 
  {
    "datetime": "2022-01-08 15:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Florida International", 
      "logo": "../../../img/ncaab-logos/Florida International.png", 
      "money_multiplier": 6.2, 
      "odds": {
        "betonline": 520, 
        "bovada": 475, 
        "mybookie": 475, 
        "opening": 325, 
        "sportsbetting": 520
      }, 
      "short_name": "FIU", 
      "win_probability": 0.18114016995297416
    }, 
    "team_2": {
      "full_name": "Western Kentucky", 
      "logo": "../../../img/ncaab-logos/Western Kentucky.png", 
      "money_multiplier": 1.2, 
      "odds": {
        "betonline": -700, 
        "bovada": -700, 
        "mybookie": -650, 
        "opening": -500, 
        "sportsbetting": -700
      }, 
      "short_name": "WKU", 
      "win_probability": 0.865
    }
  }, 
  {
    "datetime": "2022-01-08 15:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Oral Roberts", 
      "logo": "../../../img/ncaab-logos/Oral Roberts.png", 
      "money_multiplier": 1.6666666666666667, 
      "odds": {
        "betonline": -150, 
        "bovada": -160, 
        "mybookie": -160, 
        "opening": -154, 
        "sportsbetting": -150
      }, 
      "short_name": "ORAL", 
      "win_probability": 0.6074136886735312
    }, 
    "team_2": {
      "full_name": "Western Illinois", 
      "logo": "../../../img/ncaab-logos/Western Illinois.png", 
      "money_multiplier": 2.35, 
      "odds": {
        "betonline": 130, 
        "bovada": 135, 
        "mybookie": 130, 
        "opening": 115, 
        "sportsbetting": 130
      }, 
      "short_name": "WILL", 
      "win_probability": 0.4389992040100682
    }
  }, 
  {
    "datetime": "2022-01-08 15:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Western Carolina", 
      "logo": "../../../img/ncaab-logos/Western Carolina.png", 
      "money_multiplier": 3.5, 
      "odds": {
        "betonline": 245, 
        "bovada": 250, 
        "mybookie": 240, 
        "opening": 225, 
        "sportsbetting": 245
      }, 
      "short_name": "WCAR", 
      "win_probability": 0.29344687707859063
    }, 
    "team_2": {
      "full_name": "Samford", 
      "logo": "../../../img/ncaab-logos/Samford.png", 
      "money_multiplier": 1.3448275862068966, 
      "odds": {
        "betonline": -290, 
        "bovada": -300, 
        "mybookie": -305, 
        "opening": -333, 
        "sportsbetting": -290
      }, 
      "short_name": "SAM", 
      "win_probability": 0.7518638049430967
    }
  }, 
  {
    "datetime": "2022-01-08 15:30:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Ball State", 
      "logo": "../../../img/ncaab-logos/Ball State.png", 
      "money_multiplier": 2.15, 
      "odds": {
        "betonline": -105, 
        "bovada": 100, 
        "mybookie": None, 
        "opening": 115, 
        "sportsbetting": -105
      }, 
      "short_name": "BALL", 
      "win_probability": 0.4973766307430516
    }, 
    "team_2": {
      "full_name": "Eastern Michigan", 
      "logo": "../../../img/ncaab-logos/Eastern Michigan.png", 
      "money_multiplier": 1.8695652173913044, 
      "odds": {
        "betonline": -115, 
        "bovada": -120, 
        "mybookie": None, 
        "opening": -154, 
        "sportsbetting": -115
      }, 
      "short_name": "EMU", 
      "win_probability": 0.5553802999783589
    }
  }, 
  {
    "datetime": "2022-01-08 15:30:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Alabama", 
      "logo": "../../../img/ncaab-logos/Alabama.png", 
      "money_multiplier": 1.1, 
      "odds": {
        "betonline": -1200, 
        "bovada": -1300, 
        "mybookie": -1200, 
        "opening": -1000, 
        "sportsbetting": -1200
      }, 
      "short_name": "BAMA", 
      "win_probability": 0.9213786213786215
    }, 
    "team_2": {
      "full_name": "Missouri", 
      "logo": "../../../img/ncaab-logos/Missouri.png", 
      "money_multiplier": 8.5, 
      "odds": {
        "betonline": 750, 
        "bovada": 725, 
        "mybookie": 700, 
        "opening": 550, 
        "sportsbetting": 750
      }, 
      "short_name": "MIZZU", 
      "win_probability": 0.1270704785410668
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "The Citadel", 
      "logo": "../../../img/ncaab-logos/The Citadel.png", 
      "money_multiplier": 9.25, 
      "odds": {
        "betonline": 825, 
        "bovada": 775, 
        "mybookie": 750, 
        "opening": 650, 
        "sportsbetting": 825
      }, 
      "short_name": "CITAD", 
      "win_probability": 0.11629646453175865
    }, 
    "team_2": {
      "full_name": "Chattanooga", 
      "logo": "../../../img/ncaab-logos/Chattanooga.png", 
      "money_multiplier": 1.0714285714285714, 
      "odds": {
        "betonline": -1400, 
        "bovada": -1500, 
        "mybookie": -1400, 
        "opening": -1429, 
        "sportsbetting": -1400
      }, 
      "short_name": "CHATT", 
      "win_probability": 0.9344195552648792
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Wofford", 
      "logo": "../../../img/ncaab-logos/Wofford.png", 
      "money_multiplier": 1.7407407407407407, 
      "odds": {
        "betonline": -145, 
        "bovada": -135, 
        "mybookie": -135, 
        "opening": -154, 
        "sportsbetting": -145
      }, 
      "short_name": "WOFF", 
      "win_probability": 0.5877817704397893
    }, 
    "team_2": {
      "full_name": "East Tennessee State", 
      "logo": "../../../img/ncaab-logos/East Tennessee State.png", 
      "money_multiplier": 2.25, 
      "odds": {
        "betonline": 125, 
        "bovada": 115, 
        "mybookie": 115, 
        "opening": 115, 
        "sportsbetting": 125
      }, 
      "short_name": "ETEN", 
      "win_probability": 0.4568475452196383
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Mercer", 
      "logo": "../../../img/ncaab-logos/Mercer.png", 
      "money_multiplier": 5.5, 
      "odds": {
        "betonline": 435, 
        "bovada": 420, 
        "mybookie": 450, 
        "opening": 400, 
        "sportsbetting": 435
      }, 
      "short_name": "MERC", 
      "win_probability": 0.18959152996536174
    }, 
    "team_2": {
      "full_name": "Furman", 
      "logo": "../../../img/ncaab-logos/Furman.png", 
      "money_multiplier": 1.1801801801801801, 
      "odds": {
        "betonline": -555, 
        "bovada": -605, 
        "mybookie": -600, 
        "opening": -714, 
        "sportsbetting": -555
      }, 
      "short_name": "FUR", 
      "win_probability": 0.8574210502422293
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "UAB", 
      "logo": "../../../img/ncaab-logos/UAB.png", 
      "money_multiplier": 1.2252252252252251, 
      "odds": {
        "betonline": -500, 
        "bovada": -520, 
        "mybookie": -500, 
        "opening": -444, 
        "sportsbetting": -500
      }, 
      "short_name": "UAB", 
      "win_probability": 0.8309772296015181
    }, 
    "team_2": {
      "full_name": "Rice", 
      "logo": "../../../img/ncaab-logos/Rice.png", 
      "money_multiplier": 5.0, 
      "odds": {
        "betonline": 395, 
        "bovada": 375, 
        "mybookie": 400, 
        "opening": 300, 
        "sportsbetting": 395
      }, 
      "short_name": "RICE", 
      "win_probability": 0.21291334396597553
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Louisiana Tech", 
      "logo": "../../../img/ncaab-logos/Louisiana Tech.png", 
      "money_multiplier": 1.1200480192076832, 
      "odds": {
        "betonline": -900, 
        "bovada": -950, 
        "mybookie": -1000, 
        "opening": -833, 
        "sportsbetting": -900
      }, 
      "short_name": "LTECH", 
      "win_probability": 0.9013343355465542
    }, 
    "team_2": {
      "full_name": "UTSA", 
      "logo": "../../../img/ncaab-logos/UTSA.png", 
      "money_multiplier": 7.4, 
      "odds": {
        "betonline": 640, 
        "bovada": 600, 
        "mybookie": 600, 
        "opening": 450, 
        "sportsbetting": 640
      }, 
      "short_name": "UTSA", 
      "win_probability": 0.14756054756054757
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Kansas", 
      "logo": "../../../img/ncaab-logos/Kansas.png", 
      "money_multiplier": 1.4, 
      "odds": {
        "betonline": -280, 
        "bovada": -290, 
        "mybookie": -290, 
        "opening": -250, 
        "sportsbetting": -280
      }, 
      "short_name": "KU", 
      "win_probability": 0.7350298823983035
    }, 
    "team_2": {
      "full_name": "Texas Tech", 
      "logo": "../../../img/ncaab-logos/Texas Tech.png", 
      "money_multiplier": 3.4, 
      "odds": {
        "betonline": 235, 
        "bovada": 240, 
        "mybookie": 240, 
        "opening": 180, 
        "sportsbetting": 235
      }, 
      "short_name": "TTECH", 
      "win_probability": 0.3084786153267277
    }
  }, 
  
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Sacramento State", 
      "logo": "../../../img/ncaab-logos/Sacramento State.png", 
      "money_multiplier": 6.15, 
      "odds": {
        "betonline": 515, 
        "bovada": 450, 
        "mybookie": 480, 
        "opening": 425, 
        "sportsbetting": 515
      }, 
      "short_name": "SAC", 
      "win_probability": 0.1739822834860682
    }, 
    "team_2": {
      "full_name": "Northern Colorado", 
      "logo": "../../../img/ncaab-logos/Northern Colorado.png", 
      "money_multiplier": 1.16, 
      "odds": {
        "betonline": -665, 
        "bovada": -665, 
        "mybookie": -780, 
        "opening": -625, 
        "sportsbetting": -665
      }, 
      "short_name": "UNCO", 
      "win_probability": 0.8712551478271559
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Hawaii", 
      "logo": "../../../img/ncaab-logos/Hawaii.png", 
      "money_multiplier": 2.1, 
      "odds": {
        "betonline": -103, 
        "bovada": 110, 
        "mybookie": 110, 
        "opening": 100, 
        "sportsbetting": -103
      }, 
      "short_name": "HAW", 
      "win_probability": 0.493431855500821
    }, 
    "team_2": {
      "full_name": "Long Beach State", 
      "logo": "../../../img/ncaab-logos/Long Beach State.png", 
      "money_multiplier": 1.8547008547008548, 
      "odds": {
        "betonline": -117, 
        "bovada": -130, 
        "mybookie": -130, 
        "opening": -133, 
        "sportsbetting": -117
      }, 
      "short_name": "LBST", 
      "win_probability": 0.5559182494154714
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "North Dakota", 
      "logo": "../../../img/ncaab-logos/North Dakota.png", 
      "money_multiplier": 3.5, 
      "odds": {
        "betonline": 225, 
        "bovada": 220, 
        "mybookie": 230, 
        "opening": 250, 
        "sportsbetting": 225
      }, 
      "short_name": "NODAK", 
      "win_probability": 0.3033258408258408
    }, 
    "team_2": {
      "full_name": "Denver", 
      "logo": "../../../img/ncaab-logos/Denver.png", 
      "money_multiplier": 1.3773584905660377, 
      "odds": {
        "betonline": -265, 
        "bovada": -270, 
        "mybookie": -270, 
        "opening": -400, 
        "sportsbetting": -265
      }, 
      "short_name": "DENVR", 
      "win_probability": 0.7423028507960014
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Murray State", 
      "logo": "../../../img/ncaab-logos/Murray State.png", 
      "money_multiplier": 1.1428571428571428, 
      "odds": {
        "betonline": -700, 
        "bovada": -700, 
        "mybookie": -700, 
        "opening": -833, 
        "sportsbetting": -700
      }, 
      "short_name": "MURRAY", 
      "win_probability": 0.8785637727759914
    }, 
    "team_2": {
      "full_name": "Southern Illinois-Edwardsville", 
      "logo": "../../../img/ncaab-logos/Southern Illinois-Edwardsville.png", 
      "money_multiplier": 6.2, 
      "odds": {
        "betonline": 520, 
        "bovada": 475, 
        "mybookie": 500, 
        "opening": 450, 
        "sportsbetting": 520
      }, 
      "short_name": "SIUED", 
      "win_probability": 0.16899570742487993
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Dixie State", 
      "logo": "../../../img/ncaab-logos/Dixie State.png", 
      "money_multiplier": 7.25, 
      "odds": {
        "betonline": 550, 
        "bovada": 525, 
        "mybookie": 625, 
        "opening": 450, 
        "sportsbetting": 550
      }, 
      "short_name": "DIXIE", 
      "win_probability": 0.15748830479864964
    }, 
    "team_2": {
      "full_name": "Utah Valley", 
      "logo": "../../../img/ncaab-logos/Utah Valley.png", 
      "money_multiplier": 1.1369863013698631, 
      "odds": {
        "betonline": -730, 
        "bovada": -800, 
        "mybookie": -925, 
        "opening": -833, 
        "sportsbetting": -730
      }, 
      "short_name": "UTVAL", 
      "win_probability": 0.8886365843474806
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Boston College", 
      "logo": "../../../img/ncaab-logos/Boston College.png", 
      "money_multiplier": 2.5, 
      "odds": {
        "betonline": 140, 
        "bovada": 140, 
        "mybookie": 130, 
        "opening": 150, 
        "sportsbetting": 140
      }, 
      "short_name": "BC", 
      "win_probability": 0.41695652173913045
    }, 
    "team_2": {
      "full_name": "Pittsburgh", 
      "logo": "../../../img/ncaab-logos/Pittsburgh.png", 
      "money_multiplier": 1.625, 
      "odds": {
        "betonline": -160, 
        "bovada": -165, 
        "mybookie": -160, 
        "opening": -222, 
        "sportsbetting": -160
      }, 
      "short_name": "PITT", 
      "win_probability": 0.6316472698753256
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Colorado State", 
      "logo": "../../../img/ncaab-logos/Colorado State.png", 
      "money_multiplier": 2.25, 
      "odds": {
        "betonline": 125, 
        "bovada": 125, 
        "mybookie": 125, 
        "opening": 120, 
        "sportsbetting": 125
      }, 
      "short_name": "COLST", 
      "win_probability": 0.44646464646464645
    }, 
    "team_2": {
      "full_name": "San Diego State", 
      "logo": "../../../img/ncaab-logos/San Diego State.png", 
      "money_multiplier": 1.6896551724137931, 
      "odds": {
        "betonline": -145, 
        "bovada": -145, 
        "mybookie": -145, 
        "opening": -167, 
        "sportsbetting": -145
      }, 
      "short_name": "SDST", 
      "win_probability": 0.5985630207139035
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "South Florida", 
      "logo": "../../../img/ncaab-logos/South Florida.png", 
      "money_multiplier": 4.0, 
      "odds": {
        "betonline": 220, 
        "bovada": 220, 
        "mybookie": 230, 
        "opening": 300, 
        "sportsbetting": 220
      }, 
      "short_name": "USF", 
      "win_probability": 0.2981060606060606
    }, 
    "team_2": {
      "full_name": "Tulane", 
      "logo": "../../../img/ncaab-logos/Tulane.png", 
      "money_multiplier": 1.3846153846153846, 
      "odds": {
        "betonline": -260, 
        "bovada": -270, 
        "mybookie": -270, 
        "opening": -500, 
        "sportsbetting": -260
      }, 
      "short_name": "TUL", 
      "win_probability": 0.7474474474474475
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Southeast Missouri State", 
      "logo": "../../../img/ncaab-logos/Southeast Missouri State.png", 
      "money_multiplier": 2.15, 
      "odds": {
        "betonline": 107, 
        "bovada": 110, 
        "mybookie": 110, 
        "opening": 115, 
        "sportsbetting": 107
      }, 
      "short_name": "SEMO", 
      "win_probability": 0.4767361612659894
    }, 
    "team_2": {
      "full_name": "Tennessee State", 
      "logo": "../../../img/ncaab-logos/Tennessee State.png", 
      "money_multiplier": 1.7874015748031495, 
      "odds": {
        "betonline": -127, 
        "bovada": -130, 
        "mybookie": -130, 
        "opening": -154, 
        "sportsbetting": -127
      }, 
      "short_name": "TNST", 
      "win_probability": 0.5711353452969308
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Bradley", 
      "logo": "../../../img/ncaab-logos/Bradley.png", 
      "money_multiplier": 8.0, 
      "odds": {
        "betonline": 675, 
        "bovada": 650, 
        "mybookie": 700, 
        "opening": 550, 
        "sportsbetting": 675
      }, 
      "short_name": "BRAD", 
      "win_probability": 0.13404880066170388
    }, 
    "team_2": {
      "full_name": "Loyola-Chicago", 
      "logo": "../../../img/ncaab-logos/Loyola-Chicago.png", 
      "money_multiplier": 1.1, 
      "odds": {
        "betonline": -1050, 
        "bovada": -1100, 
        "mybookie": -1200, 
        "opening": -1000, 
        "sportsbetting": -1050
      }, 
      "short_name": "LCU", 
      "win_probability": 0.9149842910712476
    }
  }, 
  {
    "datetime": "2022-01-08 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Cal Poly", 
      "logo": "../../../img/ncaab-logos/Cal Poly.png", 
      "money_multiplier": 2.3, 
      "odds": {
        "betonline": 120, 
        "bovada": 115, 
        "mybookie": 115, 
        "opening": 130, 
        "sportsbetting": 120
      }, 
      "short_name": "CALPO", 
      "win_probability": 0.45482121518521923
    }, 
    "team_2": {
      "full_name": "Cal State-Northridge", 
      "logo": "../../../img/ncaab-logos/Cal State-Northridge.png", 
      "money_multiplier": 1.7407407407407407, 
      "odds": {
        "betonline": -140, 
        "bovada": -135, 
        "mybookie": -135, 
        "opening": -167, 
        "sportsbetting": -140
      }, 
      "short_name": "CALNO", 
      "win_probability": 0.588214200334688
    }
  }, 
  {
    "datetime": "2022-01-08 16:30:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Belmont", 
      "logo": "../../../img/ncaab-logos/Belmont.png", 
      "money_multiplier": 1.0699790062981105, 
      "odds": {
        "betonline": -2100, 
        "bovada": -2000, 
        "mybookie": -2100, 
        "opening": -1429, 
        "sportsbetting": -2100
      }, 
      "short_name": "BELM", 
      "win_probability": 0.9501230184683422
    }, 
    "team_2": {
      "full_name": "Tennessee-Martin", 
      "logo": "../../../img/ncaab-logos/Tennessee-Martin.png", 
      "money_multiplier": 11.0, 
      "odds": {
        "betonline": 850, 
        "bovada": 950, 
        "mybookie": 1000, 
        "opening": 650, 
        "sportsbetting": 850
      }, 
      "short_name": "UTM", 
      "win_probability": 0.10600136705399862
    }
  }, 
  {
    "datetime": "2022-01-08 17:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Appalachian State", 
      "logo": "../../../img/ncaab-logos/Appalachian State.png", 
      "money_multiplier": 2.15, 
      "odds": {
        "betonline": 115, 
        "bovada": 105, 
        "mybookie": 110, 
        "opening": 115, 
        "sportsbetting": 115
      }, 
      "short_name": "APP", 
      "win_probability": 0.47186883828971177
    }, 
    "team_2": {
      "full_name": "Troy", 
      "logo": "../../../img/ncaab-logos/Troy.png", 
      "money_multiplier": 1.8, 
      "odds": {
        "betonline": -135, 
        "bovada": -125, 
        "mybookie": -130, 
        "opening": -154, 
        "sportsbetting": -135
      }, 
      "short_name": "TROY", 
      "win_probability": 0.575201665934219
    }
  }, 
  {
    "datetime": "2022-01-08 17:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Morehead State", 
      "logo": "../../../img/ncaab-logos/Morehead State.png", 
      "money_multiplier": 1.2564102564102564, 
      "odds": {
        "betonline": -400, 
        "bovada": -415, 
        "mybookie": -390, 
        "opening": -500, 
        "sportsbetting": -400
      }, 
      "short_name": "MORE", 
      "win_probability": 0.8070153886797439
    }, 
    "team_2": {
      "full_name": "Austin Peay", 
      "logo": "../../../img/ncaab-logos/Austin Peay.png", 
      "money_multiplier": 4.25, 
      "odds": {
        "betonline": 320, 
        "bovada": 310, 
        "mybookie": 320, 
        "opening": 325, 
        "sportsbetting": 320
      }, 
      "short_name": "PEAY", 
      "win_probability": 0.23869645419143265
    }
  }, 
  {
    "datetime": "2022-01-08 17:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Baylor", 
      "logo": "../../../img/ncaab-logos/Baylor.png", 
      "money_multiplier": 1.1923076923076923, 
      "odds": {
        "betonline": -525, 
        "bovada": -530, 
        "mybookie": -520, 
        "opening": -556, 
        "sportsbetting": -525
      }, 
      "short_name": "BAY", 
      "win_probability": 0.8415080988597904
    }, 
    "team_2": {
      "full_name": "TCU", 
      "logo": "../../../img/ncaab-logos/TCU.png", 
      "money_multiplier": 5.2, 
      "odds": {
        "betonline": 420, 
        "bovada": 380, 
        "mybookie": 395, 
        "opening": 350, 
        "sportsbetting": 420
      }, 
      "short_name": "TCU", 
      "win_probability": 0.20343822843822842
    }
  }, 
  {
    "datetime": "2022-01-08 17:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Miami-Ohio", 
      "logo": "../../../img/ncaab-logos/Miami-Ohio.png", 
      "money_multiplier": 2.1, 
      "odds": {
        "betonline": 110, 
        "bovada": 110, 
        "mybookie": 110, 
        "opening": -125, 
        "sportsbetting": 110
      }, 
      "short_name": "M-OH", 
      "win_probability": 0.4920634920634921
    }, 
    "team_2": {
      "full_name": "Bowling Green", 
      "logo": "../../../img/ncaab-logos/Bowling Green.png", 
      "money_multiplier": 1.9523809523809523, 
      "odds": {
        "betonline": -130, 
        "bovada": -130, 
        "mybookie": -130, 
        "opening": -105, 
        "sportsbetting": -130
      }, 
      "short_name": "BOWL", 
      "win_probability": 0.5546129374337221
    }
  }, 
  {
    "datetime": "2022-01-08 18:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Georgia", 
      "logo": "../../../img/ncaab-logos/Georgia.png", 
      "money_multiplier": 27.0, 
      "odds": {
        "betonline": 2600, 
        "bovada": 1325, 
        "mybookie": None, 
        "opening": 2587, 
        "sportsbetting": 2600
      }, 
      "short_name": "GA", 
      "win_probability": 0.045366434736305264
    }, 
    "team_2": {
      "full_name": "Kentucky", 
      "logo": "../../../img/ncaab-logos/Kentucky.png", 
      "money_multiplier": 1.0240211386019697, 
      "odds": {
        "betonline": -7000, 
        "bovada": -6500, 
        "mybookie": None, 
        "opening": -4163, 
        "sportsbetting": -7000
      }, 
      "short_name": "UK", 
      "win_probability": 0.9833054529595847
    }
  }, 
  {
    "datetime": "2022-01-08 18:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Columbia", 
      "logo": "../../../img/ncaab-logos/Columbia.png", 
      "money_multiplier": 10.25, 
      "odds": {
        "betonline": 790, 
        "bovada": 750, 
        "mybookie": 800, 
        "opening": 925, 
        "sportsbetting": 790
      }, 
      "short_name": "COLUM", 
      "win_probability": 0.11020764933359843
    }, 
    "team_2": {
      "full_name": "Pennsylvania", 
      "logo": "../../../img/ncaab-logos/Pennsylvania.png", 
      "money_multiplier": 1.0833333333333333, 
      "odds": {
        "betonline": -1300, 
        "bovada": -1400, 
        "mybookie": -1200, 
        "opening": -1400, 
        "sportsbetting": -1300
      }, 
      "short_name": "PENN", 
      "win_probability": 0.9293772893772895
    }
  }, 
  {
    "datetime": "2022-01-08 18:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Middle Tennessee", 
      "logo": "../../../img/ncaab-logos/Middle Tennessee.png", 
      "money_multiplier": 8.0, 
      "odds": {
        "betonline": 510, 
        "bovada": 475, 
        "mybookie": 475, 
        "opening": 700, 
        "sportsbetting": 510
      }, 
      "short_name": "MTSU", 
      "win_probability": 0.1601389878831076
    }, 
    "team_2": {
      "full_name": "North Texas", 
      "logo": "../../../img/ncaab-logos/North Texas.png", 
      "money_multiplier": 1.1538461538461537, 
      "odds": {
        "betonline": -660, 
        "bovada": -700, 
        "mybookie": -650, 
        "opening": -1250, 
        "sportsbetting": -660
      }, 
      "short_name": "UNT", 
      "win_probability": 0.88088693957115
    }
  }, 
  {
    "datetime": "2022-01-08 18:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Tennessee", 
      "logo": "../../../img/ncaab-logos/Tennessee.png", 
      "money_multiplier": 2.3, 
      "odds": {
        "betonline": 123, 
        "bovada": 130, 
        "mybookie": 125, 
        "opening": 130, 
        "sportsbetting": 123
      }, 
      "short_name": "TENN", 
      "win_probability": 0.4421741296765668
    }, 
    "team_2": {
      "full_name": "LSU", 
      "logo": "../../../img/ncaab-logos/LSU.png", 
      "money_multiplier": 1.6993006993006994, 
      "odds": {
        "betonline": -143, 
        "bovada": -150, 
        "mybookie": -145, 
        "opening": -182, 
        "sportsbetting": -143
      }, 
      "short_name": "LSU", 
      "win_probability": 0.6028363076252303
    }
  }, 
  {
    "datetime": "2022-01-08 18:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Northern Iowa", 
      "logo": "../../../img/ncaab-logos/Northern Iowa.png", 
      "money_multiplier": 3.1, 
      "odds": {
        "betonline": 156, 
        "bovada": 150, 
        "mybookie": 150, 
        "opening": 210, 
        "sportsbetting": 156
      }, 
      "short_name": "NIOWA", 
      "win_probability": 0.38076612903225804
    }, 
    "team_2": {
      "full_name": "Missouri State", 
      "logo": "../../../img/ncaab-logos/Missouri State.png", 
      "money_multiplier": 1.5714285714285714, 
      "odds": {
        "betonline": -176, 
        "bovada": -175, 
        "mybookie": -180, 
        "opening": -263, 
        "sportsbetting": -176
      }, 
      "short_name": "MOST", 
      "win_probability": 0.6558202008794894
    }
  }, 
  {
    "datetime": "2022-01-08 18:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Iowa State", 
      "logo": "../../../img/ncaab-logos/Iowa State.png", 
      "money_multiplier": 3.3, 
      "odds": {
        "betonline": 205, 
        "bovada": 210, 
        "mybookie": 230, 
        "opening": 180, 
        "sportsbetting": 205
      }, 
      "short_name": "IAST", 
      "win_probability": 0.3276983020504966
    }, 
    "team_2": {
      "full_name": "Oklahoma", 
      "logo": "../../../img/ncaab-logos/Oklahoma.png", 
      "money_multiplier": 1.4081632653061225, 
      "odds": {
        "betonline": -245, 
        "bovada": -250, 
        "mybookie": -270, 
        "opening": -286, 
        "sportsbetting": -245
      }, 
      "short_name": "OU", 
      "win_probability": 0.7210475883149909
    }
  }, 
  {
    "datetime": "2022-01-08 18:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Notre Dame", 
      "logo": "../../../img/ncaab-logos/Notre Dame.png", 
      "money_multiplier": 1.9009009009009008, 
      "odds": {
        "betonline": -117, 
        "bovada": -115, 
        "mybookie": None, 
        "opening": -111, 
        "sportsbetting": -117
      }, 
      "short_name": "ND", 
      "win_probability": 0.5348227713665045
    }, 
    "team_2": {
      "full_name": "Georgia Tech", 
      "logo": "../../../img/ncaab-logos/Georgia Tech.png", 
      "money_multiplier": 1.970873786407767, 
      "odds": {
        "betonline": -103, 
        "bovada": -105, 
        "mybookie": None, 
        "opening": -105, 
        "sportsbetting": -103
      }, 
      "short_name": "GTECH", 
      "win_probability": 0.509792142256398
    }
  }, 
  {
    "datetime": "2022-01-08 18:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Cornell", 
      "logo": "../../../img/ncaab-logos/Cornell.png", 
      "money_multiplier": 3.65, 
      "odds": {
        "betonline": 210, 
        "bovada": 205, 
        "mybookie": 210, 
        "opening": 265, 
        "sportsbetting": 210
      }, 
      "short_name": "CORN", 
      "win_probability": 0.31391667813652263
    }, 
    "team_2": {
      "full_name": "Princeton", 
      "logo": "../../../img/ncaab-logos/Princeton.png", 
      "money_multiplier": 1.4081632653061225, 
      "odds": {
        "betonline": -250, 
        "bovada": -245, 
        "mybookie": -250, 
        "opening": -325, 
        "sportsbetting": -250
      }, 
      "short_name": "PRIN", 
      "win_probability": 0.7235415905492633
    }
  }, 
  {
    "datetime": "2022-01-08 18:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Washington State", 
      "logo": "../../../img/ncaab-logos/Washington State.png", 
      "money_multiplier": 2.15, 
      "odds": {
        "betonline": -120, 
        "bovada": -120, 
        "mybookie": 115, 
        "opening": -104, 
        "sportsbetting": -120
      }, 
      "short_name": "WAZZU", 
      "win_probability": 0.5222567674004062
    }, 
    "team_2": {
      "full_name": "Utah", 
      "logo": "../../../img/ncaab-logos/Utah.png", 
      "money_multiplier": 2.0, 
      "odds": {
        "betonline": 100, 
        "bovada": 100, 
        "mybookie": -135, 
        "opening": -114, 
        "sportsbetting": 100
      }, 
      "short_name": "UTAH", 
      "win_probability": 0.5214356730960429
    }
  }, 
  {
    "datetime": "2022-01-08 18:30:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Idaho", 
      "logo": "../../../img/ncaab-logos/Idaho.png", 
      "money_multiplier": 8.0, 
      "odds": {
        "betonline": 615, 
        "bovada": 575, 
        "mybookie": 700, 
        "opening": 500, 
        "sportsbetting": 615
      }, 
      "short_name": "IDAHO", 
      "win_probability": 0.1439070189070189
    }, 
    "team_2": {
      "full_name": "Eastern Washington", 
      "logo": "../../../img/ncaab-logos/Eastern Washington.png", 
      "money_multiplier": 1.1176470588235294, 
      "odds": {
        "betonline": -850, 
        "bovada": -900, 
        "mybookie": -1100, 
        "opening": -1000, 
        "sportsbetting": -850
      }, 
      "short_name": "EWU", 
      "win_probability": 0.9030462519936204
    }
  }, 
  {
    "datetime": "2022-01-08 19:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Florida Atlantic", 
      "logo": "../../../img/ncaab-logos/Florida Atlantic.png", 
      "money_multiplier": 2.85, 
      "odds": {
        "betonline": 185, 
        "bovada": 175, 
        "mybookie": 180, 
        "opening": 160, 
        "sportsbetting": 185
      }, 
      "short_name": "FAU", 
      "win_probability": 0.3614297982719036
    }, 
    "team_2": {
      "full_name": "Marshall", 
      "logo": "../../../img/ncaab-logos/Marshall.png", 
      "money_multiplier": 1.4761904761904763, 
      "odds": {
        "betonline": -215, 
        "bovada": -210, 
        "mybookie": -210, 
        "opening": -250, 
        "sportsbetting": -215
      }, 
      "short_name": "MARCH", 
      "win_probability": 0.6868407578084997
    }
  }, 
  {
    "datetime": "2022-01-08 19:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "South Dakota", 
      "logo": "../../../img/ncaab-logos/South Dakota.png", 
      "money_multiplier": 11.5, 
      "odds": {
        "betonline": 850, 
        "bovada": 900, 
        "mybookie": 1050, 
        "opening": 800, 
        "sportsbetting": 850
      }, 
      "short_name": "SDAK", 
      "win_probability": 0.10171878972794306
    }, 
    "team_2": {
      "full_name": "South Dakota State", 
      "logo": "../../../img/ncaab-logos/South Dakota State.png", 
      "money_multiplier": 1.0526315789473684, 
      "odds": {
        "betonline": -2100, 
        "bovada": -1900, 
        "mybookie": -2000, 
        "opening": -2000, 
        "sportsbetting": -2100
      }, 
      "short_name": "SDAKST", 
      "win_probability": 0.9527705627705627
    }
  }, 
  {
    "datetime": "2022-01-08 19:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Sam Houston State", 
      "logo": "../../../img/ncaab-logos/Sam Houston State.png", 
      "money_multiplier": 5.3, 
      "odds": {
        "betonline": 430, 
        "bovada": 380, 
        "mybookie": 415, 
        "opening": 400, 
        "sportsbetting": 430
      }, 
      "short_name": "SAMHO", 
      "win_probability": 0.1959733162361849
    }, 
    "team_2": {
      "full_name": "Abilene Christian", 
      "logo": "../../../img/ncaab-logos/Abilene Christian.png", 
      "money_multiplier": 1.1886792452830188, 
      "odds": {
        "betonline": -550, 
        "bovada": -530, 
        "mybookie": -540, 
        "opening": -714, 
        "sportsbetting": -550
      }, 
      "short_name": "ABILE", 
      "win_probability": 0.8508954821454822
    }
  }, 
  {
    "datetime": "2022-01-08 19:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Southern Illinois", 
      "logo": "../../../img/ncaab-logos/Southern Illinois.png", 
      "money_multiplier": 2.1, 
      "odds": {
        "betonline": 110, 
        "bovada": 110, 
        "mybookie": 105, 
        "opening": -109, 
        "sportsbetting": 110
      }, 
      "short_name": "SIU", 
      "win_probability": 0.48758148141973556
    }, 
    "team_2": {
      "full_name": "Valparaiso", 
      "logo": "../../../img/ncaab-logos/Valparaiso.png", 
      "money_multiplier": 1.9174311926605505, 
      "odds": {
        "betonline": -130, 
        "bovada": -130, 
        "mybookie": -125, 
        "opening": -109, 
        "sportsbetting": -130
      }, 
      "short_name": "VALPO", 
      "win_probability": 0.5545477659894136
    }
  }, 
  {
    "datetime": "2022-01-08 19:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "San Diego", 
      "logo": "../../../img/ncaab-logos/San Diego.png", 
      "money_multiplier": 10.5, 
      "odds": {
        "betonline": 850, 
        "bovada": 950, 
        "mybookie": 890, 
        "opening": 700, 
        "sportsbetting": 850
      }, 
      "short_name": "SD", 
      "win_probability": 0.10635490240753398
    }, 
    "team_2": {
      "full_name": "San Francisco", 
      "logo": "../../../img/ncaab-logos/San Francisco.png", 
      "money_multiplier": 1.05998800239952, 
      "odds": {
        "betonline": -2100, 
        "bovada": -2000, 
        "mybookie": -1840, 
        "opening": -1667, 
        "sportsbetting": -2100
      }, 
      "short_name": "SF", 
      "win_probability": 0.9506664748153906
    }
  }, 
  {
    "datetime": "2022-01-08 19:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Brown", 
      "logo": "../../../img/ncaab-logos/Brown.png", 
      "money_multiplier": 1.6896551724137931, 
      "odds": {
        "betonline": -150, 
        "bovada": -160, 
        "mybookie": -150, 
        "opening": -145, 
        "sportsbetting": -150
      }, 
      "short_name": "BROWN", 
      "win_probability": 0.6014442700156987
    }, 
    "team_2": {
      "full_name": "Dartmouth", 
      "logo": "../../../img/ncaab-logos/Dartmouth.png", 
      "money_multiplier": 2.35, 
      "odds": {
        "betonline": 130, 
        "bovada": 135, 
        "mybookie": 130, 
        "opening": 125, 
        "sportsbetting": 130
      }, 
      "short_name": "DART", 
      "win_probability": 0.43486483708500356
    }
  }, 
  {
    "datetime": "2022-01-08 20:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Louisville", 
      "logo": "../../../img/ncaab-logos/Louisville.png", 
      "money_multiplier": 2.7, 
      "odds": {
        "betonline": 170, 
        "bovada": 170, 
        "mybookie": 165, 
        "opening": 170, 
        "sportsbetting": 170
      }, 
      "short_name": "LOUIS", 
      "win_probability": 0.3717679944095038
    }, 
    "team_2": {
      "full_name": "Florida State", 
      "logo": "../../../img/ncaab-logos/Florida State.png", 
      "money_multiplier": 1.5128205128205128, 
      "odds": {
        "betonline": -195, 
        "bovada": -200, 
        "mybookie": -195, 
        "opening": -286, 
        "sportsbetting": -195
      }, 
      "short_name": "FSU", 
      "win_probability": 0.678130031322268
    }
  }, 
  {
    "datetime": "2022-01-08 20:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Arkansas-Little Rock", 
      "logo": "../../../img/ncaab-logos/Arkansas-Little Rock.png", 
      "money_multiplier": 5.75, 
      "odds": {
        "betonline": 460, 
        "bovada": 450, 
        "mybookie": 475, 
        "opening": 425, 
        "sportsbetting": 460
      }, 
      "short_name": "UALR", 
      "win_probability": 0.18067005458309807
    }, 
    "team_2": {
      "full_name": "Louisiana-Lafayette", 
      "logo": "../../../img/ncaab-logos/Louisiana-Lafayette.png", 
      "money_multiplier": 1.1666666666666667, 
      "odds": {
        "betonline": -600, 
        "bovada": -665, 
        "mybookie": -650, 
        "opening": -714, 
        "sportsbetting": -600
      }, 
      "short_name": "ULL", 
      "win_probability": 0.8654766607707784
    }
  }, 
  {
    "datetime": "2022-01-08 20:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Florida", 
      "logo": "../../../img/ncaab-logos/Florida.png", 
      "money_multiplier": 4.25, 
      "odds": {
        "betonline": 300, 
        "bovada": 285, 
        "mybookie": 300, 
        "opening": 325, 
        "sportsbetting": 300
      }, 
      "short_name": "FLA", 
      "win_probability": 0.2490068754774637
    }, 
    "team_2": {
      "full_name": "Auburn", 
      "logo": "../../../img/ncaab-logos/Auburn.png", 
      "money_multiplier": 1.2777777777777777, 
      "odds": {
        "betonline": -370, 
        "bovada": -370, 
        "mybookie": -360, 
        "opening": -556, 
        "sportsbetting": -370
      }, 
      "short_name": "AUB", 
      "win_probability": 0.7983743597843008
    }
  }, 
  {
    "datetime": "2022-01-08 20:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Utah State", 
      "logo": "../../../img/ncaab-logos/Utah State.png", 
      "money_multiplier": 1.3636363636363635, 
      "odds": {
        "betonline": -275, 
        "bovada": -290, 
        "mybookie": -280, 
        "opening": -333, 
        "sportsbetting": -275
      }, 
      "short_name": "UTST", 
      "win_probability": 0.7432303266604957
    }, 
    "team_2": {
      "full_name": "New Mexico", 
      "logo": "../../../img/ncaab-logos/New Mexico.png", 
      "money_multiplier": 3.4, 
      "odds": {
        "betonline": 230, 
        "bovada": 240, 
        "mybookie": 240, 
        "opening": 210, 
        "sportsbetting": 230
      }, 
      "short_name": "NMEX", 
      "win_probability": 0.30337530906790866
    }
  }, 
  {
    "datetime": "2022-01-08 20:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "UC San Diego", 
      "logo": "../../../img/ncaab-logos/UC San Diego.png", 
      "money_multiplier": 2.8, 
      "odds": {
        "betonline": 175, 
        "bovada": 175, 
        "mybookie": 170, 
        "opening": 180, 
        "sportsbetting": 175
      }, 
      "short_name": "UC-SD", 
      "win_probability": 0.36368446368446367
    }, 
    "team_2": {
      "full_name": "UC Davis", 
      "logo": "../../../img/ncaab-logos/UC Davis.png", 
      "money_multiplier": 1.5, 
      "odds": {
        "betonline": -205, 
        "bovada": -210, 
        "mybookie": -200, 
        "opening": -286, 
        "sportsbetting": -205
      }, 
      "short_name": "UCD", 
      "win_probability": 0.685856191814878
    }
  }, 
  {
    "datetime": "2022-01-08 20:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "New Mexico State", 
      "logo": "../../../img/ncaab-logos/New Mexico State.png", 
      "money_multiplier": 1.170940170940171, 
      "odds": {
        "betonline": -600, 
        "bovada": -585, 
        "mybookie": -590, 
        "opening": -714, 
        "sportsbetting": -600
      }, 
      "short_name": "NMSU", 
      "win_probability": 0.8601045307487707
    }, 
    "team_2": {
      "full_name": "UTRGV", 
      "logo": "../../../img/ncaab-logos/UTRGV.png", 
      "money_multiplier": 5.6, 
      "odds": {
        "betonline": 460, 
        "bovada": 410, 
        "mybookie": 440, 
        "opening": 400, 
        "sportsbetting": 460
      }, 
      "short_name": "UTRGV", 
      "win_probability": 0.1876812947401183
    }
  }, 
  {
    "datetime": "2022-01-08 20:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Miami", 
      "logo": "../../../img/ncaab-logos/Miami.png", 
      "money_multiplier": 10.0, 
      "odds": {
        "betonline": 790, 
        "bovada": 775, 
        "mybookie": 900, 
        "opening": 550, 
        "sportsbetting": 790
      }, 
      "short_name": "MIAMI", 
      "win_probability": 0.11857019385109273
    }, 
    "team_2": {
      "full_name": "Duke", 
      "logo": "../../../img/ncaab-logos/Duke.png", 
      "money_multiplier": 1.09000900090009, 
      "odds": {
        "betonline": -1300, 
        "bovada": -1500, 
        "mybookie": -1600, 
        "opening": -1111, 
        "sportsbetting": -1300
      }, 
      "short_name": "DUKE", 
      "win_probability": 0.9306485889153351
    }
  }, 
  {
    "datetime": "2022-01-08 20:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "UCLA", 
      "logo": "../../../img/ncaab-logos/UCLA.png", 
      "money_multiplier": 1.2409638554216869, 
      "odds": {
        "betonline": -430, 
        "bovada": -415, 
        "mybookie": -425, 
        "opening": -500, 
        "sportsbetting": -430
      }, 
      "short_name": "UCLA", 
      "win_probability": 0.8142647790019104
    }, 
    "team_2": {
      "full_name": "California", 
      "logo": "../../../img/ncaab-logos/California.png", 
      "money_multiplier": 4.5, 
      "odds": {
        "betonline": 350, 
        "bovada": 310, 
        "mybookie": 345, 
        "opening": 350, 
        "sportsbetting": 350
      }, 
      "short_name": "CAL", 
      "win_probability": 0.22705764136293047
    }
  }, 
  {
    "datetime": "2022-01-08 20:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "UC Irvine", 
      "logo": "../../../img/ncaab-logos/UC Irvine.png", 
      "money_multiplier": 1.8333333333333333, 
      "odds": {
        "betonline": -120, 
        "bovada": -120, 
        "mybookie": None, 
        "opening": -133, 
        "sportsbetting": -120
      }, 
      "short_name": "UCI", 
      "win_probability": 0.5517947717518532
    }, 
    "team_2": {
      "full_name": "UC Riverside", 
      "logo": "../../../img/ncaab-logos/UC Riverside.png", 
      "money_multiplier": 2.0, 
      "odds": {
        "betonline": 100, 
        "bovada": 100, 
        "mybookie": None, 
        "opening": -105, 
        "sportsbetting": 100
      }, 
      "short_name": "UCR", 
      "win_probability": 0.5030487804878049
    }
  }, 
  {
    "datetime": "2022-01-08 20:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Stephen F. Austin", 
      "logo": "../../../img/ncaab-logos/Stephen F. Austin.png", 
      "money_multiplier": 1.8064516129032258, 
      "odds": {
        "betonline": -124, 
        "bovada": -125, 
        "mybookie": -125, 
        "opening": -133, 
        "sportsbetting": -124
      }, 
      "short_name": "SFA", 
      "win_probability": 0.5578138837795491
    }, 
    "team_2": {
      "full_name": "Tarleton State", 
      "logo": "../../../img/ncaab-logos/Tarleton State.png", 
      "money_multiplier": 2.05, 
      "odds": {
        "betonline": 104, 
        "bovada": 105, 
        "mybookie": 105, 
        "opening": -105, 
        "sportsbetting": 104
      }, 
      "short_name": "TARLE", 
      "win_probability": 0.49363940698230513
    }
  }, 
  {
    "datetime": "2022-01-08 20:30:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Mississippi State", 
      "logo": "../../../img/ncaab-logos/Mississippi State.png", 
      "money_multiplier": 1.7142857142857142, 
      "odds": {
        "betonline": -141, 
        "bovada": -140, 
        "mybookie": -140, 
        "opening": -182, 
        "sportsbetting": -141
      }, 
      "short_name": "MISST", 
      "win_probability": 0.5964362437832907
    }, 
    "team_2": {
      "full_name": "Mississippi-Ole Miss", 
      "logo": "../../../img/ncaab-logos/Mississippi-Ole Miss.png", 
      "money_multiplier": 2.3, 
      "odds": {
        "betonline": 121, 
        "bovada": 120, 
        "mybookie": 120, 
        "opening": 130, 
        "sportsbetting": 121
      }, 
      "short_name": "MISS", 
      "win_probability": 0.44977017867043434
    }
  }, 
  {
    "datetime": "2022-01-08 21:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Pepperdine", 
      "logo": "../../../img/ncaab-logos/Pepperdine.png", 
      "money_multiplier": 41.0, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 4000, 
        "sportsbetting": None
      }, 
      "short_name": "PEPP", 
      "win_probability": 0.024390243902439025
    }, 
    "team_2": {
      "full_name": "Gonzaga", 
      "logo": "../../../img/ncaab-logos/Gonzaga.png", 
      "money_multiplier": 1.011111111111111, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -9000, 
        "sportsbetting": None
      }, 
      "short_name": "GONZA", 
      "win_probability": 0.989010989010989
    }
  }, 
  {
    "datetime": "2022-01-08 21:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Southern Mississippi", 
      "logo": "../../../img/ncaab-logos/Southern Mississippi.png", 
      "money_multiplier": 5.5, 
      "odds": {
        "betonline": 450, 
        "bovada": 425, 
        "mybookie": 435, 
        "opening": 350, 
        "sportsbetting": 450
      }, 
      "short_name": "SMISS", 
      "win_probability": 0.19265013283704874
    }, 
    "team_2": {
      "full_name": "UTEP", 
      "logo": "../../../img/ncaab-logos/UTEP.png", 
      "money_multiplier": 1.1798561151079137, 
      "odds": {
        "betonline": -570, 
        "bovada": -615, 
        "mybookie": -585, 
        "opening": -556, 
        "sportsbetting": -570
      }, 
      "short_name": "UTEP", 
      "win_probability": 0.8526415943206389
    }
  }, 
  {
    "datetime": "2022-01-08 22:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Saint Mary's-California", 
      "logo": "../../../img/ncaab-logos/Saint Mary's-California.png", 
      "money_multiplier": 2.7, 
      "odds": {
        "betonline": 170, 
        "bovada": 165, 
        "mybookie": 160, 
        "opening": 130, 
        "sportsbetting": 170
      }, 
      "short_name": "STMAR", 
      "win_probability": 0.38749944492356303
    }, 
    "team_2": {
      "full_name": "BYU", 
      "logo": "../../../img/ncaab-logos/BYU.png", 
      "money_multiplier": 1.5494505494505495, 
      "odds": {
        "betonline": -195, 
        "bovada": -195, 
        "mybookie": -190, 
        "opening": -182, 
        "sportsbetting": -195
      }, 
      "short_name": "BYU", 
      "win_probability": 0.6567226664345434
    }
  }, 
  {
    "datetime": "2022-01-09 00:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Minnesota", 
      "logo": "../../../img/ncaab-logos/Minnesota.png", 
      "money_multiplier": 7.0, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 600, 
        "sportsbetting": None
      }, 
      "short_name": "MINN", 
      "win_probability": 0.14285714285714285
    }, 
    "team_2": {
      "full_name": "Indiana", 
      "logo": "../../../img/ncaab-logos/Indiana.png", 
      "money_multiplier": 1.1, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -1000, 
        "sportsbetting": None
      }, 
      "short_name": "INDY", 
      "win_probability": 0.9090909090909091
    }
  }, 
  {
    "datetime": "2022-01-09 13:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Quinnipiac", 
      "logo": "../../../img/ncaab-logos/Quinnipiac.png", 
      "money_multiplier": 2.3, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 130, 
        "sportsbetting": None
      }, 
      "short_name": "QUINN", 
      "win_probability": 0.43478260869565216
    }, 
    "team_2": {
      "full_name": "Niagara", 
      "logo": "../../../img/ncaab-logos/Niagara.png", 
      "money_multiplier": 1.5494505494505495, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -182, 
        "sportsbetting": None
      }, 
      "short_name": "NIAGR", 
      "win_probability": 0.6453900709219859
    }
  }, 
  {
    "datetime": "2022-01-09 13:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Purdue Fort Wayne", 
      "logo": "../../../img/ncaab-logos/Purdue Fort Wayne.png", 
      "money_multiplier": 1.7518796992481203, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -133, 
        "sportsbetting": None
      }, 
      "short_name": "PFW", 
      "win_probability": 0.5708154506437768
    }, 
    "team_2": {
      "full_name": "Robert Morris", 
      "logo": "../../../img/ncaab-logos/Robert Morris.png", 
      "money_multiplier": 1.9523809523809523, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -105, 
        "sportsbetting": None
      }, 
      "short_name": "ROBMO", 
      "win_probability": 0.5121951219512195
    }
  }, 
  {
    "datetime": "2022-01-09 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Yale", 
      "logo": "../../../img/ncaab-logos/Yale.png", 
      "money_multiplier": 2.2, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 120, 
        "sportsbetting": None
      }, 
      "short_name": "YALE", 
      "win_probability": 0.45454545454545453
    }, 
    "team_2": {
      "full_name": "Harvard", 
      "logo": "../../../img/ncaab-logos/Harvard.png", 
      "money_multiplier": 1.6493506493506493, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -154, 
        "sportsbetting": None
      }, 
      "short_name": "HARV", 
      "win_probability": 0.6062992125984252
    }
  }, 
  {
    "datetime": "2022-01-09 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Rider", 
      "logo": "../../../img/ncaab-logos/Rider.png", 
      "money_multiplier": 5.5, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 450, 
        "sportsbetting": None
      }, 
      "short_name": "RIDER", 
      "win_probability": 0.18181818181818182
    }, 
    "team_2": {
      "full_name": "Marist", 
      "logo": "../../../img/ncaab-logos/Marist.png", 
      "money_multiplier": 1.1400560224089635, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -714, 
        "sportsbetting": None
      }, 
      "short_name": "MRST", 
      "win_probability": 0.8771498771498771
    }
  }, 
  {
    "datetime": "2022-01-09 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Fairfield", 
      "logo": "../../../img/ncaab-logos/Fairfield.png", 
      "money_multiplier": 1.598802395209581, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -167, 
        "sportsbetting": None
      }, 
      "short_name": "FAIRF", 
      "win_probability": 0.6254681647940075
    }, 
    "team_2": {
      "full_name": "Siena", 
      "logo": "../../../img/ncaab-logos/Siena.png", 
      "money_multiplier": 2.25, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 125, 
        "sportsbetting": None
      }, 
      "short_name": "SIENA", 
      "win_probability": 0.4444444444444444
    }
  }, 
  {
    "datetime": "2022-01-09 14:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Cleveland State", 
      "logo": "../../../img/ncaab-logos/Cleveland State.png", 
      "money_multiplier": 1.6493506493506493, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -154, 
        "sportsbetting": None
      }, 
      "short_name": "CLEVE", 
      "win_probability": 0.6062992125984252
    }, 
    "team_2": {
      "full_name": "Youngstown State", 
      "logo": "../../../img/ncaab-logos/Youngstown State.png", 
      "money_multiplier": 2.2, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 120, 
        "sportsbetting": None
      }, 
      "short_name": "YOUNG", 
      "win_probability": 0.45454545454545453
    }
  }, 
  {
    "datetime": "2022-01-09 15:30:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Cincinnati", 
      "logo": "../../../img/ncaab-logos/Cincinnati.png", 
      "money_multiplier": 4.0, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 300, 
        "sportsbetting": None
      }, 
      "short_name": "CINCY", 
      "win_probability": 0.25
    }, 
    "team_2": {
      "full_name": "Memphis", 
      "logo": "../../../img/ncaab-logos/Memphis.png", 
      "money_multiplier": 1.2252252252252251, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -444, 
        "sportsbetting": None
      }, 
      "short_name": "MEM", 
      "win_probability": 0.8161764705882353
    }
  }, 
  {
    "datetime": "2022-01-09 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Hofstra", 
      "logo": "../../../img/ncaab-logos/Hofstra.png", 
      "money_multiplier": 1.9009009009009008, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -111, 
        "sportsbetting": None
      }, 
      "short_name": "HOF", 
      "win_probability": 0.5260663507109005
    }, 
    "team_2": {
      "full_name": "James Madison", 
      "logo": "../../../img/ncaab-logos/James Madison.png", 
      "money_multiplier": 1.8, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -125, 
        "sportsbetting": None
      }, 
      "short_name": "JAMES", 
      "win_probability": 0.5555555555555556
    }
  }, 
  {
    "datetime": "2022-01-09 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Elon", 
      "logo": "../../../img/ncaab-logos/Elon.png", 
      "money_multiplier": 5.0, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 400, 
        "sportsbetting": None
      }, 
      "short_name": "ELON", 
      "win_probability": 0.2
    }, 
    "team_2": {
      "full_name": "College of Charleston", 
      "logo": "../../../img/ncaab-logos/College of Charleston.png", 
      "money_multiplier": 1.16, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -625, 
        "sportsbetting": None
      }, 
      "short_name": "COFC", 
      "win_probability": 0.8620689655172413
    }
  }, 
  {
    "datetime": "2022-01-09 16:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Wisconsin-Milwaukee", 
      "logo": "../../../img/ncaab-logos/Wisconsin-Milwaukee.png", 
      "money_multiplier": 5.0, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 400, 
        "sportsbetting": None
      }, 
      "short_name": "UWM", 
      "win_probability": 0.2
    }, 
    "team_2": {
      "full_name": "Oakland", 
      "logo": "../../../img/ncaab-logos/Oakland.png", 
      "money_multiplier": 1.1400560224089635, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -714, 
        "sportsbetting": None
      }, 
      "short_name": "OAK", 
      "win_probability": 0.8771498771498771
    }
  }, 
  {
    "datetime": "2022-01-09 16:30:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Northeastern", 
      "logo": "../../../img/ncaab-logos/Northeastern.png", 
      "money_multiplier": 3.5, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 250, 
        "sportsbetting": None
      }, 
      "short_name": "NEU", 
      "win_probability": 0.2857142857142857
    }, 
    "team_2": {
      "full_name": "Towson", 
      "logo": "../../../img/ncaab-logos/Towson.png", 
      "money_multiplier": 1.25, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -400, 
        "sportsbetting": None
      }, 
      "short_name": "TOWS", 
      "win_probability": 0.8
    }
  }, 
  {
    "datetime": "2022-01-09 17:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Washington", 
      "logo": "../../../img/ncaab-logos/Washington.png", 
      "money_multiplier": 4.0, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 300, 
        "sportsbetting": None
      }, 
      "short_name": "WASH", 
      "win_probability": 0.25
    }, 
    "team_2": {
      "full_name": "Colorado", 
      "logo": "../../../img/ncaab-logos/Colorado.png", 
      "money_multiplier": 1.2, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -500, 
        "sportsbetting": None
      }, 
      "short_name": "COLO", 
      "win_probability": 0.8333333333333334
    }
  }, 
  {
    "datetime": "2022-01-09 17:30:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Northwestern", 
      "logo": "../../../img/ncaab-logos/Northwestern.png", 
      "money_multiplier": 3.5, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 250, 
        "sportsbetting": None
      }, 
      "short_name": "NWEST", 
      "win_probability": 0.2857142857142857
    }, 
    "team_2": {
      "full_name": "Ohio State", 
      "logo": "../../../img/ncaab-logos/Ohio State.png", 
      "money_multiplier": 1.25, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -400, 
        "sportsbetting": None
      }, 
      "short_name": "OSU", 
      "win_probability": 0.8
    }
  }, 
  {
    "datetime": "2022-01-09 19:00:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Montana", 
      "logo": "../../../img/ncaab-logos/Montana.png", 
      "money_multiplier": 2.2, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": 120, 
        "sportsbetting": None
      }, 
      "short_name": "MONT", 
      "win_probability": 0.45454545454545453
    }, 
    "team_2": {
      "full_name": "Montana State", 
      "logo": "../../../img/ncaab-logos/Montana State.png", 
      "money_multiplier": 1.6493506493506493, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -154, 
        "sportsbetting": None
      }, 
      "short_name": "MTST", 
      "win_probability": 0.6062992125984252
    }
  }, 
  {
    "datetime": "2022-01-09 19:30:00", 
    "sport": "ncaab", 
    "team_1": {
      "full_name": "Wisconsin", 
      "logo": "../../../img/ncaab-logos/Wisconsin.png", 
      "money_multiplier": 1.8, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -125, 
        "sportsbetting": None
      }, 
      "short_name": "WIS", 
      "win_probability": 0.5555555555555556
    }, 
    "team_2": {
      "full_name": "Maryland", 
      "logo": "../../../img/ncaab-logos/Maryland.png", 
      "money_multiplier": 1.9009009009009008, 
      "odds": {
        "betonline": None, 
        "bovada": None, 
        "mybookie": None, 
        "opening": -111, 
        "sportsbetting": None
      }, 
      "short_name": "MARYL", 
      "win_probability": 0.5260663507109005
    }
  }
],
		
        "ncaaf": [
  {
    "datetime": "2022-01-10 20:00:00", 
    "sport": "ncaaf", 
    "team_1": {
      "full_name": "Georgia", 
      "logo": "../../../img/ncaaf-logos/Georgia.png", 
      "money_multiplier": 1.7692307692307692, 
      "odds": {
        "betonline": -136, 
        "bodog": -135, 
        "bumbet": -135, 
        "caesars": -135, 
        "intertops": -140, 
        "mirage": -145, 
        "mybookie": -130, 
        "opening": -135, 
        "station": -140, 
        "westgate": -135, 
        "wynn": -145
      }, 
      "short_name": "GA", 
      "win_probability": 0.5785608308483057
    }, 
    "team_2": {
      "full_name": "Alabama", 
      "logo": "../../../img/ncaaf-logos/Alabama.png", 
      "money_multiplier": 2.25, 
      "odds": {
        "betonline": 116, 
        "bodog": 115, 
        "bumbet": 115, 
        "caesars": 115, 
        "intertops": 120, 
        "mirage": 120, 
        "mybookie": 110, 
        "opening": 115, 
        "station": 120, 
        "westgate": 125, 
        "wynn": 125
      }, 
      "short_name": "BAMA", 
      "win_probability": 0.45928580072343284
    }
  }
],
		
        "nfl": [
  {
    "datetime": "2022-01-09 13:00:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "Chicago", 
      "logo": "../../../img/nfl-logos/Chicago.png", 
      "money_multiplier": 3.11, 
      "odds": {
        "betonline": 175, 
        "bodog": 175, 
        "bumbet": 175, 
        "caesars": 170, 
        "intertops": 175, 
        "mirage": 165, 
        "mybookie": 175, 
        "opening": 211, 
        "station": 175, 
        "westgate": 170, 
        "wynn": 175
      }, 
      "short_name": "CHI", 
      "win_probability": 0.36228156228376845
    }, 
    "team_2": {
      "full_name": "Minnesota", 
      "logo": "../../../img/nfl-logos/Minnesota.png", 
      "money_multiplier": 1.5263157894736843, 
      "odds": {
        "betonline": -205, 
        "bodog": -210, 
        "bumbet": -210, 
        "caesars": -190, 
        "intertops": -205, 
        "mirage": -200, 
        "mybookie": -210, 
        "opening": -239, 
        "station": -200, 
        "westgate": -190, 
        "wynn": -210
      }, 
      "short_name": "MIN", 
      "win_probability": 0.6729666022380804
    }
  }, 
  {
    "datetime": "2022-01-09 13:00:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "Tennessee", 
      "logo": "../../../img/nfl-logos/Tennessee.png", 
      "money_multiplier": 1.22883295194508, 
      "odds": {
        "betonline": -515, 
        "bodog": -530, 
        "bumbet": -530, 
        "caesars": -500, 
        "intertops": -530, 
        "mirage": -475, 
        "mybookie": -540, 
        "opening": -437, 
        "station": -500, 
        "westgate": -500, 
        "wynn": -500
      }, 
      "short_name": "TEN", 
      "win_probability": 0.8343780407596337
    }, 
    "team_2": {
      "full_name": "Houston", 
      "logo": "../../../img/nfl-logos/Houston.png", 
      "money_multiplier": 5.1, 
      "odds": {
        "betonline": 410, 
        "bodog": 380, 
        "bumbet": 380, 
        "caesars": 400, 
        "intertops": 400, 
        "mirage": 365, 
        "mybookie": 395, 
        "opening": 373, 
        "station": 400, 
        "westgate": 400, 
        "wynn": 400
      }, 
      "short_name": "HOU", 
      "win_probability": 0.2037486867260487
    }
  }, 
  {
    "datetime": "2022-01-09 13:00:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "Green Bay", 
      "logo": "../../../img/nfl-logos/Green Bay.png", 
      "money_multiplier": 1.625, 
      "odds": {
        "betonline": -165, 
        "bodog": -170, 
        "bumbet": -170, 
        "caesars": -160, 
        "intertops": -165, 
        "mirage": -170, 
        "mybookie": -175, 
        "opening": -531, 
        "station": -175, 
        "westgate": -160, 
        "wynn": -160
      }, 
      "short_name": "GB", 
      "win_probability": 0.6449613110226964
    }, 
    "team_2": {
      "full_name": "Detroit", 
      "logo": "../../../img/nfl-logos/Detroit.png", 
      "money_multiplier": 5.44, 
      "odds": {
        "betonline": 145, 
        "bodog": 145, 
        "bumbet": 145, 
        "caesars": 140, 
        "intertops": 145, 
        "mirage": 140, 
        "mybookie": 145, 
        "opening": 444, 
        "station": 155, 
        "westgate": 140, 
        "wynn": 140
      }, 
      "short_name": "DET", 
      "win_probability": 0.3894057623049219
    }
  }, 
  {
    "datetime": "2022-01-09 13:00:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "Indianapolis", 
      "logo": "../../../img/nfl-logos/Indianapolis.png", 
      "money_multiplier": 1.22883295194508, 
      "odds": {
        "betonline": -1050, 
        "bodog": -1100, 
        "bumbet": -1100, 
        "caesars": -1100, 
        "intertops": -1100, 
        "mirage": -1000, 
        "mybookie": -1000, 
        "opening": -437, 
        "station": -1200, 
        "westgate": -1400, 
        "wynn": -1200
      }, 
      "short_name": "IND", 
      "win_probability": 0.9082872184821972
    }, 
    "team_2": {
      "full_name": "Jacksonville", 
      "logo": "../../../img/nfl-logos/Jacksonville.png", 
      "money_multiplier": 9.0, 
      "odds": {
        "betonline": 675, 
        "bodog": 650, 
        "bumbet": 650, 
        "caesars": 700, 
        "intertops": 675, 
        "mirage": 625, 
        "mybookie": 700, 
        "opening": 373, 
        "station": 750, 
        "westgate": 800, 
        "wynn": 700
      }, 
      "short_name": "JAC", 
      "win_probability": 0.13434880706357782
    }
  }, 
  {
    "datetime": "2022-01-09 13:00:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "Washington", 
      "logo": "../../../img/nfl-logos/Washington.png", 
      "money_multiplier": 1.5376344086021505, 
      "odds": {
        "betonline": -315, 
        "bodog": -310, 
        "bumbet": -310, 
        "caesars": -310, 
        "intertops": -320, 
        "mirage": -300, 
        "mybookie": -320, 
        "opening": -186, 
        "station": -310, 
        "westgate": -310, 
        "wynn": -290
      }, 
      "short_name": "WAS", 
      "win_probability": 0.7461157152004799
    }, 
    "team_2": {
      "full_name": "NY Giants", 
      "logo": "../../../img/nfl-logos/NY Giants.png", 
      "money_multiplier": 3.65, 
      "odds": {
        "betonline": 265, 
        "bodog": 255, 
        "bumbet": 255, 
        "caesars": 255, 
        "intertops": 260, 
        "mirage": 240, 
        "mybookie": 260, 
        "opening": 169, 
        "station": 255, 
        "westgate": 260, 
        "wynn": 235
      }, 
      "short_name": "NYG", 
      "win_probability": 0.2907671655540584
    }
  }, 
  {
    "datetime": "2022-01-09 13:00:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "Pittsburgh", 
      "logo": "../../../img/nfl-logos/Pittsburgh.png", 
      "money_multiplier": 3.26, 
      "odds": {
        "betonline": 165, 
        "bodog": 160, 
        "bumbet": 160, 
        "caesars": 175, 
        "intertops": 165, 
        "mirage": 165, 
        "mybookie": 165, 
        "opening": 226, 
        "station": 165, 
        "westgate": 160, 
        "wynn": 165
      }, 
      "short_name": "PIT", 
      "win_probability": 0.37167108428512835
    }, 
    "team_2": {
      "full_name": "Baltimore", 
      "logo": "../../../img/nfl-logos/Baltimore.png", 
      "money_multiplier": 1.5555555555555556, 
      "odds": {
        "betonline": -190, 
        "bodog": -185, 
        "bumbet": -185, 
        "caesars": -200, 
        "intertops": -190, 
        "mirage": -200, 
        "mybookie": -195, 
        "opening": -254, 
        "station": -185, 
        "westgate": -180, 
        "wynn": -185
      }, 
      "short_name": "BAL", 
      "win_probability": 0.6601416004811986
    }
  }, 
  {
    "datetime": "2022-01-09 13:00:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "Cincinnati", 
      "logo": "../../../img/nfl-logos/Cincinnati.png", 
      "money_multiplier": 3.05, 
      "odds": {
        "betonline": 190, 
        "bodog": 190, 
        "bumbet": 190, 
        "caesars": 205, 
        "intertops": 180, 
        "mirage": 195, 
        "mybookie": 190, 
        "opening": 105, 
        "station": 190, 
        "westgate": 190, 
        "wynn": 185
      }, 
      "short_name": "CIN", 
      "win_probability": 0.3574220317019952
    }, 
    "team_2": {
      "full_name": "Cleveland", 
      "logo": "../../../img/nfl-logos/Cleveland.png", 
      "money_multiplier": 1.8403361344537814, 
      "odds": {
        "betonline": -220, 
        "bodog": -230, 
        "bumbet": -230, 
        "caesars": -245, 
        "intertops": -220, 
        "mirage": -235, 
        "mybookie": -235, 
        "opening": -119, 
        "station": -220, 
        "westgate": -220, 
        "wynn": -230
      }, 
      "short_name": "CLE", 
      "win_probability": 0.6815834625914526
    }
  }, 
  {
    "datetime": "2022-01-09 16:25:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "Carolina", 
      "logo": "../../../img/nfl-logos/Carolina.png", 
      "money_multiplier": 10.17, 
      "odds": {
        "betonline": 320, 
        "bodog": 310, 
        "bumbet": 310, 
        "caesars": 350, 
        "intertops": 295, 
        "mirage": 340, 
        "mybookie": 310, 
        "opening": 917, 
        "station": 335, 
        "westgate": 330, 
        "wynn": 325
      }, 
      "short_name": "CAR", 
      "win_probability": 0.22441161756282527
    }, 
    "team_2": {
      "full_name": "Tampa Bay", 
      "logo": "../../../img/nfl-logos/Tampa Bay.png", 
      "money_multiplier": 1.2702702702702702, 
      "odds": {
        "betonline": -400, 
        "bodog": -415, 
        "bumbet": -415, 
        "caesars": -430, 
        "intertops": -370, 
        "mirage": -450, 
        "mybookie": -400, 
        "opening": -1233, 
        "station": -420, 
        "westgate": -400, 
        "wynn": -425
      }, 
      "short_name": "TB", 
      "win_probability": 0.8155076784923936
    }
  }, 
  {
    "datetime": "2022-01-09 16:25:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "New England", 
      "logo": "../../../img/nfl-logos/New England.png", 
      "money_multiplier": 1.6802721088435375, 
      "odds": {
        "betonline": -266, 
        "bodog": -270, 
        "bumbet": -270, 
        "caesars": -270, 
        "intertops": -270, 
        "mirage": -300, 
        "mybookie": -275, 
        "opening": -147, 
        "station": -290, 
        "westgate": -265, 
        "wynn": -290
      }, 
      "short_name": "NE", 
      "win_probability": 0.7215797084891841
    }, 
    "team_2": {
      "full_name": "Miami", 
      "logo": "../../../img/nfl-logos/Miami.png", 
      "money_multiplier": 3.45, 
      "odds": {
        "betonline": 226, 
        "bodog": 220, 
        "bumbet": 220, 
        "caesars": 230, 
        "intertops": 230, 
        "mirage": 240, 
        "mybookie": 225, 
        "opening": 133, 
        "station": 245, 
        "westgate": 225, 
        "wynn": 235
      }, 
      "short_name": "MIA", 
      "win_probability": 0.31498712902438836
    }
  }, 
  {
    "datetime": "2022-01-09 16:25:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "New Orleans", 
      "logo": "../../../img/nfl-logos/New Orleans.png", 
      "money_multiplier": 1.5714285714285714, 
      "odds": {
        "betonline": -180, 
        "bodog": -175, 
        "bumbet": -175, 
        "caesars": -180, 
        "intertops": -180, 
        "mirage": -180, 
        "mybookie": -185, 
        "opening": -200, 
        "station": -180, 
        "westgate": -180, 
        "wynn": -180
      }, 
      "short_name": "NO", 
      "win_probability": 0.6444106133101349
    }, 
    "team_2": {
      "full_name": "Atlanta", 
      "logo": "../../../img/nfl-logos/Atlanta.png", 
      "money_multiplier": 2.78, 
      "odds": {
        "betonline": 160, 
        "bodog": 150, 
        "bumbet": 150, 
        "caesars": 160, 
        "intertops": 160, 
        "mirage": 150, 
        "mybookie": 155, 
        "opening": 178, 
        "station": 160, 
        "westgate": 160, 
        "wynn": 160
      }, 
      "short_name": "ATL", 
      "win_probability": 0.38723285460483936
    }
  }, 
  {
    "datetime": "2022-01-09 16:25:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "NY Jets", 
      "logo": "../../../img/nfl-logos/NY Jets.png", 
      "money_multiplier": 10.96, 
      "odds": {
        "betonline": 675, 
        "bodog": 700, 
        "bumbet": 700, 
        "caesars": 800, 
        "intertops": 700, 
        "mirage": 800, 
        "mybookie": 750, 
        "opening": 996, 
        "station": 800, 
        "westgate": 900, 
        "wynn": 850
      }, 
      "short_name": "NYJ", 
      "win_probability": 0.11377424400259314
    }, 
    "team_2": {
      "full_name": "Buffalo", 
      "logo": "../../../img/nfl-logos/Buffalo.png", 
      "money_multiplier": 1.0952380952380953, 
      "odds": {
        "betonline": -1050, 
        "bodog": -1200, 
        "bumbet": -1200, 
        "caesars": -1300, 
        "intertops": -1200, 
        "mirage": -1400, 
        "mybookie": -1400, 
        "opening": -1329, 
        "station": -1400, 
        "westgate": -1600, 
        "wynn": -1700
      }, 
      "short_name": "BUF", 
      "win_probability": 0.9296806895270578
    }
  }, 
  {
    "datetime": "2022-01-09 16:25:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "San Francisco", 
      "logo": "../../../img/nfl-logos/San Francisco.png", 
      "money_multiplier": 3.26, 
      "odds": {
        "betonline": 165, 
        "bodog": 160, 
        "bumbet": 160, 
        "caesars": 165, 
        "intertops": 165, 
        "mirage": 155, 
        "mybookie": 160, 
        "opening": 226, 
        "station": 165, 
        "westgate": 165, 
        "wynn": 165
      }, 
      "short_name": "SF", 
      "win_probability": 0.3742638569313769
    }, 
    "team_2": {
      "full_name": "LA Rams", 
      "logo": "../../../img/nfl-logos/LA Rams.png", 
      "money_multiplier": 1.5405405405405406, 
      "odds": {
        "betonline": -190, 
        "bodog": -185, 
        "bumbet": -185, 
        "caesars": -185, 
        "intertops": -190, 
        "mirage": -185, 
        "mybookie": -190, 
        "opening": -254, 
        "station": -185, 
        "westgate": -185, 
        "wynn": -185
      }, 
      "short_name": "LAR", 
      "win_probability": 0.6569900922541728
    }
  }, 
  {
    "datetime": "2022-01-09 16:25:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "Seattle", 
      "logo": "../../../img/nfl-logos/Seattle.png", 
      "money_multiplier": 3.2, 
      "odds": {
        "betonline": 205, 
        "bodog": 215, 
        "bumbet": 215, 
        "caesars": 210, 
        "intertops": 210, 
        "mirage": 195, 
        "mybookie": 205, 
        "opening": 186, 
        "station": 220, 
        "westgate": 210, 
        "wynn": 210
      }, 
      "short_name": "SEA", 
      "win_probability": 0.325646756452876
    }, 
    "team_2": {
      "full_name": "Arizona", 
      "logo": "../../../img/nfl-logos/Arizona.png", 
      "money_multiplier": 1.4672897196261683, 
      "odds": {
        "betonline": -245, 
        "bodog": -260, 
        "bumbet": -260, 
        "caesars": -250, 
        "intertops": -250, 
        "mirage": -235, 
        "mybookie": -255, 
        "opening": -214, 
        "station": -260, 
        "westgate": -250, 
        "wynn": -260
      }, 
      "short_name": "ARI", 
      "win_probability": 0.7130201834700918
    }
  }, 
  {
    "datetime": "2022-01-09 20:20:00", 
    "sport": "nfl", 
    "team_1": {
      "full_name": "LA Chargers", 
      "logo": "../../../img/nfl-logos/LA Chargers.png", 
      "money_multiplier": 1.7575757575757576, 
      "odds": {
        "betonline": -159, 
        "bodog": -160, 
        "bumbet": -160, 
        "caesars": -160, 
        "intertops": -160, 
        "mirage": -160, 
        "mybookie": -155, 
        "opening": -132, 
        "station": -155, 
        "westgate": -160, 
        "wynn": -160
      }, 
      "short_name": "LAC", 
      "win_probability": 0.6096585193948276
    }, 
    "team_2": {
      "full_name": "Las Vegas", 
      "logo": "../../../img/nfl-logos/Las Vegas.png", 
      "money_multiplier": 2.4, 
      "odds": {
        "betonline": 139, 
        "bodog": 135, 
        "bumbet": 135, 
        "caesars": 140, 
        "intertops": 140, 
        "mirage": 135, 
        "mybookie": 130, 
        "opening": 118, 
        "station": 135, 
        "westgate": 140, 
        "wynn": 140
      }, 
      "short_name": "LV", 
      "win_probability": 0.425518415737097
    }
  }
],
        
        "boxing": [
  {
    "datetime": "2022-01-15 18:00:00", 
    "sport": "boxing", 
    "team_1": {
      "full_name": "Callum Johnson", 
      "logo": "../../../img/boxing-logos/Callum Johnson.png", 
      "money_multiplier": 3.75, 
      "odds": {
        "betonline": 275, 
        "bodog": 265, 
        "bumbet": 265, 
        "intertops": 250, 
        "mybookie": 270, 
        "opening": 190
      }, 
      "short_name": "", 
      "win_probability": 0.2859040023895952
    }, 
    "team_2": {
      "full_name": "Joe Smith Jr", 
      "logo": "../../../img/boxing-logos/Joe Smith Jr.png", 
      "money_multiplier": 1.3846153846153846, 
      "odds": {
        "betonline": -375, 
        "bodog": -385, 
        "bumbet": -385, 
        "intertops": -351, 
        "mybookie": -340, 
        "opening": -260
      }, 
      "short_name": "", 
      "win_probability": 0.7750537591862049
    }
  }, 
  {
    "datetime": "2022-01-22 21:00:00", 
    "sport": "boxing", 
    "team_1": {
      "full_name": "Gary Russell Jr", 
      "logo": "../../../img/boxing-logos/Gary Russell Jr.png", 
      "money_multiplier": 1.2222222222222223, 
      "odds": {
        "betonline": -450, 
        "bodog": -475, 
        "bumbet": -475, 
        "intertops": None, 
        "mybookie": None, 
        "opening": -714
      }, 
      "short_name": "", 
      "win_probability": 0.8368764020937934
    }, 
    "team_2": {
      "full_name": "Mark Magsayo", 
      "logo": "../../../img/boxing-logos/Mark Magsayo.png", 
      "money_multiplier": 5.2, 
      "odds": {
        "betonline": 325, 
        "bodog": 315, 
        "bumbet": 315, 
        "intertops": None, 
        "mybookie": None, 
        "opening": 420
      }, 
      "short_name": "", 
      "win_probability": 0.22738238019953116
    }
  }
]}
    
    return fake[sport_league]