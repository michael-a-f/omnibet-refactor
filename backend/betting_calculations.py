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
        return None

    if odd > 0:
        money_multiplier = (100 + odd) / 100
    else:
        money_multiplier = (100 + abs(odd)) / abs(odd)

    return money_multiplier


def get_fake_data():
    fake =  [
    {
        "date": "Tuesday October 26",
        "time": "7:30pm",
        "team_1": {
            "full_name": "Philadelphia",
            "short_name": "PHI",
            "odds": {
                "opening": 100,
                "bovada": 105,
                "betonline": 105,
                "intertops": 100,
                "sportsbetting": 105,
                "betnow": -102,
                "mybookie": 120,
                "gtbets": 100
            },
            "win_probability": 0.4904
        },
        "team_2": {
            "full_name": "New York",
            "short_name": "NY",
            "odds": {
                "opening": -118,
                "bovada": -125,
                "betonline": -125,
                "intertops": -120,
                "sportsbetting": -125,
                "betnow": -118,
                "mybookie": -140,
                "gtbets": -120
            },
            "win_probability": 0.5529
        }
    },
    {
        "date": "Tuesday October 26",
        "time": "8:00pm",
        "team_1": {
            "full_name": "Golden State",
            "short_name": "GS",
            "odds": {
                "opening": -396,
                "bovada": -500,
                "betonline": -540,
                "intertops": -450,
                "sportsbetting": -540,
                "betnow": -450,
                "mybookie": -495,
                "gtbets": -495
            },
            "win_probability": 0.8274
        },
        "team_2": {
            "full_name": "Oklahoma City",
            "short_name": "OKC",
            "odds": {
                "opening": 330,
                "bovada": 360,
                "betonline": 435,
                "intertops": 350,
                "sportsbetting": 435,
                "betnow": 360,
                "mybookie": 375,
                "gtbets": 370
            },
            "win_probability": 0.2108
        }
    },
    {
        "date": "Tuesday October 26",
        "time": "8:30pm",
        "team_1": {
            "full_name": "Houston",
            "short_name": "HOU",
            "odds": {
                "opening": 493,
                "bovada": 445,
                "betonline": 485,
                "intertops": 450,
                "sportsbetting": 485,
                "betnow": 465,
                "mybookie": 470,
                "gtbets": 450
            },
            "win_probability": 0.1763
        },
        "team_2": {
            "full_name": "Dallas",
            "short_name": "DAL",
            "odds": {
                "opening": -633,
                "bovada": -655,
                "betonline": -625,
                "intertops": -620,
                "sportsbetting": -625,
                "betnow": -630,
                "mybookie": -640,
                "gtbets": -650
            },
            "win_probability": 0.8639
        }
    },
    {
        "date": "Tuesday October 26",
        "time": "8:30pm",
        "team_1": {
            "full_name": "LA Lakers",
            "short_name": "LAL",
            "odds": {
                "opening": -175,
                "bovada": 110,
                "betonline": 110,
                "intertops": 105,
                "sportsbetting": 110,
                "betnow": 120,
                "mybookie": -145,
                "gtbets": 115
            },
            "win_probability": 0.508
        },
        "team_2": {
            "full_name": "San Antonio",
            "short_name": "SAN",
            "odds": {
                "opening": 145,
                "bovada": -130,
                "betonline": -130,
                "intertops": -125,
                "sportsbetting": -130,
                "betnow": -140,
                "mybookie": 125,
                "gtbets": -135
            },
            "win_probability": 0.5327
        }
    },
    {
        "date": "Tuesday October 26",
        "time": "10:00pm",
        "team_1": {
            "full_name": "Denver",
            "short_name": "DEN",
            "odds": {
                "opening": 258,
                "bovada": 260,
                "betonline": 265,
                "intertops": 255,
                "sportsbetting": 265,
                "betnow": 260,
                "mybookie": 260,
                "gtbets": 115
            },
            "win_probability": 0.3009
        },
        "team_2": {
            "full_name": "Utah",
            "short_name": "UTA",
            "odds": {
                "opening": -300,
                "bovada": -320,
                "betonline": -315,
                "intertops": -310,
                "sportsbetting": -315,
                "betnow": -320,
                "mybookie": -320,
                "gtbets": -145
            },
            "win_probability": 0.7377
        }
    },
    {
        "date": "Wednesday October 27",
        "time": "7:00pm",
        "team_1": {
            "full_name": "Charlotte",
            "short_name": "CHR",
            "odds": {
                "opening": -250,
                "bovada": -240,
                "betonline": -240,
                "intertops": None,
                "sportsbetting": -240,
                "betnow": None,
                "mybookie": None,
                "gtbets": -245
            },
            "win_probability": None
        },
        "team_2": {
            "full_name": "Orlando",
            "short_name": "ORL",
            "odds": {
                "opening": 200,
                "bovada": 200,
                "betonline": 200,
                "intertops": None,
                "sportsbetting": 200,
                "betnow": None,
                "mybookie": None,
                "gtbets": 205
            },
            "win_probability": None
        }
    },
    {
        "date": "Wednesday October 27",
        "time": "7:30pm",
        "team_1": {
            "full_name": "Washington",
            "short_name": "WAS",
            "odds": {
                "opening": 150,
                "bovada": 155,
                "betonline": 160,
                "intertops": None,
                "sportsbetting": 160,
                "betnow": None,
                "mybookie": None,
                "gtbets": 160
            },
            "win_probability": None
        },
        "team_2": {
            "full_name": "Boston",
            "short_name": "BOS",
            "odds": {
                "opening": -182,
                "bovada": -180,
                "betonline": -180,
                "intertops": None,
                "sportsbetting": -180,
                "betnow": None,
                "mybookie": None,
                "gtbets": -185
            },
            "win_probability": None
        }
    },
    {
        "date": "Wednesday October 27",
        "time": "7:30pm",
        "team_1": {
            "full_name": "Miami",
            "short_name": "MIA",
            "odds": {
                "opening": 165,
                "bovada": 170,
                "betonline": 170,
                "intertops": None,
                "sportsbetting": 170,
                "betnow": None,
                "mybookie": None,
                "gtbets": 160
            },
            "win_probability": None
        },
        "team_2": {
            "full_name": "Brooklyn",
            "short_name": "BKN",
            "odds": {
                "opening": -200,
                "bovada": -200,
                "betonline": -195,
                "intertops": None,
                "sportsbetting": -195,
                "betnow": None,
                "mybookie": None,
                "gtbets": -190
            },
            "win_probability": None
        }
    },
    {
        "date": "Wednesday October 27",
        "time": "7:30pm",
        "team_1": {
            "full_name": "Atlanta",
            "short_name": "ATL",
            "odds": {
                "opening": -250,
                "bovada": -240,
                "betonline": -240,
                "intertops": None,
                "sportsbetting": -240,
                "betnow": None,
                "mybookie": None,
                "gtbets": -245
            },
            "win_probability": None
        },
        "team_2": {
            "full_name": "New Orleans",
            "short_name": "NOP",
            "odds": {
                "opening": 200,
                "bovada": 200,
                "betonline": 200,
                "intertops": None,
                "sportsbetting": 200,
                "betnow": None,
                "mybookie": None,
                "gtbets": 205
            },
            "win_probability": None
        }
    },
    {
        "date": "Wednesday October 27",
        "time": "7:30pm",
        "team_1": {
            "full_name": "Indiana",
            "short_name": "IND",
            "odds": {
                "opening": -111,
                "bovada": -120,
                "betonline": -120,
                "intertops": None,
                "sportsbetting": -120,
                "betnow": None,
                "mybookie": None,
                "gtbets": -120
            },
            "win_probability": None
        },
        "team_2": {
            "full_name": "Toronto",
            "short_name": "TOR",
            "odds": {
                "opening": -105,
                "bovada": 100,
                "betonline": 100,
                "intertops": None,
                "sportsbetting": 100,
                "betnow": None,
                "mybookie": None,
                "gtbets": 100
            },
            "win_probability": None
        }
    },
    {
        "date": "Wednesday October 27",
        "time": "8:00pm",
        "team_1": {
            "full_name": "Minnesota",
            "short_name": "MIN",
            "odds": {
                "opening": None,
                "bovada": None,
                "betonline": None,
                "intertops": None,
                "sportsbetting": None,
                "betnow": None,
                "mybookie": None,
                "gtbets": None
            },
            "win_probability": None
        },
        "team_2": {
            "full_name": "Milwaukee",
            "short_name": "MIL",
            "odds": {
                "opening": None,
                "bovada": None,
                "betonline": None,
                "intertops": None,
                "sportsbetting": None,
                "betnow": None,
                "mybookie": None,
                "gtbets": None
            },
            "win_probability": None
        }
    },
    {
        "date": "Wednesday October 27",
        "time": "8:00pm",
        "team_1": {
            "full_name": "LA Lakers",
            "short_name": "LAL",
            "odds": {
                "opening": None,
                "bovada": None,
                "betonline": None,
                "intertops": None,
                "sportsbetting": None,
                "betnow": None,
                "mybookie": None,
                "gtbets": None
            },
            "win_probability": None
        },
        "team_2": {
            "full_name": "Oklahoma City",
            "short_name": "OKC",
            "odds": {
                "opening": None,
                "bovada": None,
                "betonline": None,
                "intertops": None,
                "sportsbetting": None,
                "betnow": None,
                "mybookie": None,
                "gtbets": None
            },
            "win_probability": None
        }
    },
    {
        "date": "Wednesday October 27",
        "time": "10:00pm",
        "team_1": {
            "full_name": "Sacramento",
            "short_name": "SAC",
            "odds": {
                "opening": 296,
                "bovada": 285,
                "betonline": 290,
                "intertops": None,
                "sportsbetting": 290,
                "betnow": None,
                "mybookie": None,
                "gtbets": 270
            },
            "win_probability": None
        },
        "team_2": {
            "full_name": "Phoenix",
            "short_name": "PHO",
            "odds": {
                "opening": -350,
                "bovada": -370,
                "betonline": -360,
                "intertops": None,
                "sportsbetting": -360,
                "betnow": None,
                "mybookie": None,
                "gtbets": -355
            },
            "win_probability": None
        }
    },
    {
        "date": "Wednesday October 27",
        "time": "10:00pm",
        "team_1": {
            "full_name": "Memphis",
            "short_name": "MEM",
            "odds": {
                "opening": 115,
                "bovada": 110,
                "betonline": 110,
                "intertops": None,
                "sportsbetting": 110,
                "betnow": None,
                "mybookie": None,
                "gtbets": 110
            },
            "win_probability": None
        },
        "team_2": {
            "full_name": "Portland",
            "short_name": "POR",
            "odds": {
                "opening": -138,
                "bovada": -130,
                "betonline": -130,
                "intertops": None,
                "sportsbetting": -130,
                "betnow": None,
                "mybookie": None,
                "gtbets": -130
            },
            "win_probability": None
        }
    },
    {
        "date": "Wednesday October 27",
        "time": "10:30pm",
        "team_1": {
            "full_name": "Cleveland",
            "short_name": "CLE",
            "odds": {
                "opening": 300,
                "bovada": 270,
                "betonline": 290,
                "intertops": None,
                "sportsbetting": 290,
                "betnow": None,
                "mybookie": None,
                "gtbets": 265
            },
            "win_probability": None
        },
        "team_2": {
            "full_name": "LA Clippers",
            "short_name": "LAC",
            "odds": {
                "opening": -400,
                "bovada": -340,
                "betonline": -360,
                "intertops": None,
                "sportsbetting": -360,
                "betnow": None,
                "mybookie": None,
                "gtbets": -345
            },
            "win_probability": None
        }
    }
]

    return fake