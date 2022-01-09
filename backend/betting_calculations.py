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
                "sport": "nba",
                "date": "Friday November 19",
                "time": "7:00p",
                "team_1": {
                    "full_name": "Indiana",
                    "short_name": "IND",
                    "logo": "../../../img/nba-logos/Indiana.png",
                    "odds": {
                        "opening": 123,
                        "bovada": None,
                        "betonline": None,
                        "sportsbetting": None,
                        "betnow": 120,
                        "gtbets": 120
                    },
                    "money_multiplier": 2.23,
                    "win_probability": 0.4525071341214839
                },
                "team_2": {
                    "full_name": "Charlotte",
                    "short_name": "CHR",
                    "logo": "../../../img/nba-logos/Charlotte.png",
                    "odds": {
                        "opening": -136,
                        "bovada": None,
                        "betonline": None,
                        "sportsbetting": None,
                        "betnow": -140,
                        "gtbets": -140
                    },
                    "money_multiplier": 1.7352941176470589,
                    "win_probability": 0.580979284369115
                }
            },
            {
                "sport": "nba",
                "date": "Friday November 19",
                "time": "7:00p",
                "team_1": {
                    "full_name": "Golden State",
                    "short_name": "GS",
                    "logo": "../../../img/nba-logos/Golden State.png",
                    "odds": {
                        "opening": -600,
                        "bovada": None,
                        "betonline": None,
                        "sportsbetting": None,
                        "betnow": None,
                        "gtbets": None
                    },
                    "money_multiplier": 1.1666666666666667,
                    "win_probability": 0.8571428571428571
                },
                "team_2": {
                    "full_name": "Detroit",
                    "short_name": "DET",
                    "logo": "../../../img/nba-logos/Detroit.png",
                    "odds": {
                        "opening": 425,
                        "bovada": None,
                        "betonline": None,
                        "sportsbetting": None,
                        "betnow": None,
                        "gtbets": None
                    },
                    "money_multiplier": 5.25,
                    "win_probability": 0.19047619047619047
                }
            },
            {
                "sport": "nba",
                "date": "Friday November 19",
                "time": "7:30p",
                "team_1": {
                    "full_name": "LA Lakers",
                    "short_name": "LAL",
                    "logo": "../../../img/nba-logos/LA Lakers.png",
                    "odds": {
                        "opening": 110,
                        "bovada": None,
                        "betonline": None,
                        "sportsbetting": None,
                        "betnow": None,
                        "gtbets": None
                    },
                    "money_multiplier": 2.1,
                    "win_probability": 0.47619047619047616
                },
                "team_2": {
                    "full_name": "Boston",
                    "short_name": "BOS",
                    "logo": "../../../img/nba-logos/Boston.png",
                    "odds": {
                        "opening": -130,
                        "bovada": None,
                        "betonline": None,
                        "sportsbetting": None,
                        "betnow": None,
                        "gtbets": None
                    },
                    "money_multiplier": 1.7692307692307692,
                    "win_probability": 0.5652173913043478
                }
            },
            {
                "sport": "nba",
                "date": "Friday November 19",
                "time": "7:30p",
                "team_1": {
                    "full_name": "Orlando",
                    "short_name": "ORL",
                    "logo": "../../../img/nba-logos/Orlando.png",
                    "odds": {
                        "opening": 650,
                        "bovada": None,
                        "betonline": None,
                        "sportsbetting": None,
                        "betnow": None,
                        "gtbets": None
                    },
                    "money_multiplier": 7.5,
                    "win_probability": 0.13333333333333333
                },
                "team_2": {
                    "full_name": "Brooklyn",
                    "short_name": "BKN",
                    "logo": "../../../img/nba-logos/Brooklyn.png",
                    "odds": {
                        "opening": -1000,
                        "bovada": None,
                        "betonline": None,
                        "sportsbetting": None,
                        "betnow": None,
                        "gtbets": None
                    },
                    "money_multiplier": 1.1,
                    "win_probability": 0.9090909090909091
                }
            },
            {
                "sport": "nba",
                "date": "Friday November 19",
                "time": "8:00p",
                "team_1": {
                    "full_name": "Oklahoma City",
                    "short_name": "OKC",
                    "logo": "../../../img/nba-logos/Oklahoma City.png",
                    "odds": {
                        "opening": 700,
                        "bovada": None,
                        "betonline": None,
                        "sportsbetting": None,
                        "betnow": None,
                        "gtbets": None
                    },
                    "money_multiplier": 8.0,
                    "win_probability": 0.125
                },
                "team_2": {
                    "full_name": "Milwaukee",
                    "short_name": "MIL",
                    "logo": "../../../img/nba-logos/Milwaukee.png",
                    "odds": {
                        "opening": -1100,
                        "bovada": None,
                        "betonline": None,
                        "sportsbetting": None,
                        "betnow": None,
                        "gtbets": None
                    },
                    "money_multiplier": 1.0909090909090908,
                    "win_probability": 0.9166666666666666
                }
            },
            {
                "sport": "nba",
                "date": "Friday November 19",
                "time": "8:00p",
                "team_1": {
                    "full_name": "LA Clippers",
                    "short_name": "LAC",
                    "logo": "../../../img/nba-logos/LA Clippers.png",
                    "odds": {
                        "opening": -157,
                        "bovada": None,
                        "betonline": None,
                        "sportsbetting": None,
                        "betnow": None,
                        "gtbets": -165
                    },
                    "money_multiplier": 1.6369426751592357,
                    "win_probability": 0.6167682255341018
                },
                "team_2": {
                    "full_name": "New Orleans",
                    "short_name": "NOP",
                    "logo": "../../../img/nba-logos/New Orleans.png",
                    "odds": {
                        "opening": 141,
                        "bovada": None,
                        "betonline": None,
                        "sportsbetting": None,
                        "betnow": None,
                        "gtbets": 145
                    },
                    "money_multiplier": 2.45,
                    "win_probability": 0.41155051232111106
                }
            }],
            
        "nhl": [
            {
                "sport": "nhl",
                "date": "Thursday November 18",
                "time": "7:00p",
                "team_1": {
                    "full_name": "Calgary",
                    "short_name": "CAL",
                    "logo": "../../../img/nhl-logos/Calgary.png",
                    "odds": {
                        "opening": -185,
                        "bovada": -185,
                        "betonline": -182,
                        "intertops": -190,
                        "sportsbetting": -182,
                        "betnow": -185,
                        "mybookie": -190,
                        "gtbets": -190
                    },
                    "money_multiplier": 1.5494505494505495,
                    "win_probability": 0.6504582255344892
                },
                "team_2": {
                    "full_name": "Buffalo",
                    "short_name": "BUF",
                    "logo": "../../../img/nhl-logos/Buffalo.png",
                    "odds": {
                        "opening": 130,
                        "bovada": 160,
                        "betonline": 164,
                        "intertops": 165,
                        "sportsbetting": 164,
                        "betnow": 160,
                        "mybookie": 165,
                        "gtbets": 165
                    },
                    "money_multiplier": 2.65,
                    "win_probability": 0.38670807590003653
                }
            },
            {
                "sport": "nhl",
                "date": "Thursday November 18",
                "time": "7:00p",
                "team_1": {
                    "full_name": "New Jersey",
                    "short_name": "NJ",
                    "logo": "../../../img/nhl-logos/New Jersey.png",
                    "odds": {
                        "opening": 145,
                        "bovada": 165,
                        "betonline": 175,
                        "intertops": 170,
                        "sportsbetting": 175,
                        "betnow": 170,
                        "mybookie": 170,
                        "gtbets": 170
                    },
                    "money_multiplier": 2.75,
                    "win_probability": 0.3742844955782961
                },
                "team_2": {
                    "full_name": "Florida",
                    "short_name": "FLA",
                    "logo": "../../../img/nhl-logos/Florida.png",
                    "odds": {
                        "opening": -213,
                        "bovada": -195,
                        "betonline": -195,
                        "intertops": -200,
                        "sportsbetting": -195,
                        "betnow": -200,
                        "mybookie": -200,
                        "gtbets": -200
                    },
                    "money_multiplier": 1.5128205128205128,
                    "win_probability": 0.666278587029115
                }
            },
            {
                "sport": "nhl",
                "date": "Thursday November 18",
                "time": "7:00p",
                "team_1": {
                    "full_name": "Pittsburgh",
                    "short_name": "PIT",
                    "logo": "../../../img/nhl-logos/Pittsburgh.png",
                    "odds": {
                        "opening": -141,
                        "bovada": -150,
                        "betonline": -148,
                        "intertops": -150,
                        "sportsbetting": -148,
                        "betnow": -152,
                        "mybookie": -150,
                        "gtbets": -150
                    },
                    "money_multiplier": 1.7092198581560283,
                    "win_probability": 0.5977231538669097
                },
                "team_2": {
                    "full_name": "Montreal",
                    "short_name": "MON",
                    "logo": "../../../img/nhl-logos/Montreal.png",
                    "odds": {
                        "opening": 100,
                        "bovada": 130,
                        "betonline": 134,
                        "intertops": 130,
                        "sportsbetting": 134,
                        "betnow": 132,
                        "mybookie": 130,
                        "gtbets": 130
                    },
                    "money_multiplier": 2.34,
                    "win_probability": 0.4406082215302605
                }
            },
            {
                "sport": "nhl",
                "date": "Thursday November 18",
                "time": "7:00p",
                "team_1": {
                    "full_name": "Tampa Bay",
                    "short_name": "TB",
                    "logo": "../../../img/nhl-logos/Tampa Bay.png",
                    "odds": {
                        "opening": 145,
                        "bovada": -135,
                        "betonline": -130,
                        "intertops": -130,
                        "sportsbetting": -130,
                        "betnow": -132,
                        "mybookie": -130,
                        "gtbets": -130
                    },
                    "money_multiplier": 2.45,
                    "win_probability": 0.547210478021953
                },
                "team_2": {
                    "full_name": "Philadelphia",
                    "short_name": "PHI",
                    "logo": "../../../img/nhl-logos/Philadelphia.png",
                    "odds": {
                        "opening": 235,
                        "bovada": 115,
                        "betonline": 118,
                        "intertops": 110,
                        "sportsbetting": 118,
                        "betnow": 112,
                        "mybookie": 110,
                        "gtbets": 110
                    },
                    "money_multiplier": 3.35,
                    "win_probability": 0.4476655595244826
                }
            },
            {
                "sport": "nhl",
                "date": "Thursday November 18",
                "time": "7:00p",
                "team_1": {
                    "full_name": "NY Rangers",
                    "short_name": "NYR",
                    "logo": "../../../img/nhl-logos/NY Rangers.png",
                    "odds": {
                        "opening": 135,
                        "bovada": 150,
                        "betonline": 152,
                        "intertops": 150,
                        "sportsbetting": 152,
                        "betnow": 150,
                        "mybookie": 150,
                        "gtbets": 150
                    },
                    "money_multiplier": 2.52,
                    "win_probability": 0.4023978385680513
                },
                "team_2": {
                    "full_name": "Toronto",
                    "short_name": "TOR",
                    "logo": "../../../img/nhl-logos/Toronto.png",
                    "odds": {
                        "opening": -196,
                        "bovada": -175,
                        "betonline": -168,
                        "intertops": -170,
                        "sportsbetting": -168,
                        "betnow": -170,
                        "mybookie": -170,
                        "gtbets": -170
                    },
                    "money_multiplier": 1.5952380952380953,
                    "win_probability": 0.6338469575409874
                }
            },
            {
                "sport": "nhl",
                "date": "Thursday November 18",
                "time": "8:00p",
                "team_1": {
                    "full_name": "Dallas",
                    "short_name": "DAL",
                    "logo": "../../../img/nhl-logos/Dallas.png",
                    "odds": {
                        "opening": 250,
                        "bovada": 115,
                        "betonline": 122,
                        "intertops": 120,
                        "sportsbetting": 122,
                        "betnow": 115,
                        "mybookie": 120,
                        "gtbets": 120
                    },
                    "money_multiplier": 3.5,
                    "win_probability": 0.43506051354888564
                },
                "team_2": {
                    "full_name": "Minnesota",
                    "short_name": "MIN",
                    "logo": "../../../img/nhl-logos/Minnesota.png",
                    "odds": {
                        "opening": 130,
                        "bovada": -135,
                        "betonline": -135,
                        "intertops": -140,
                        "sportsbetting": -135,
                        "betnow": -135,
                        "mybookie": -140,
                        "gtbets": -140
                    },
                    "money_multiplier": 2.3,
                    "win_probability": 0.5603318686401481
                }
            }],
		
        "ufc": [
            {
                "sport": "ufc",
                "date": "Saturday November 20",
                "time": "6:00p",
                "team_1": {
                    "full_name": "Ketlen Vieira",
                    "short_name": "",
                    "logo": "../../../img/ufc-logos/Ketlen Vieira.png",
                    "odds": {
                        "opening": -160,
                        "bovada": -120,
                        "betonline": -115,
                        "intertops": -120,
                        "sportsbetting": -115,
                        "mybookie": -115
                    },
                    "money_multiplier": 1.8695652173913044,
                    "win_probability": 0.5518241448474007
                },
                "team_2": {
                    "full_name": "Miesha Tate",
                    "short_name": "",
                    "logo": "../../../img/ufc-logos/Miesha Tate.png",
                    "odds": {
                        "opening": 140,
                        "bovada": 100,
                        "betonline": -105,
                        "intertops": -110,
                        "sportsbetting": -105,
                        "mybookie": -115
                    },
                    "money_multiplier": 2.4,
                    "win_probability": 0.49995835921814374
                }
            },
            {
                "sport": "ufc",
                "date": "Saturday November 20",
                "time": "6:00p",
                "team_1": {
                    "full_name": "Sean Brady",
                    "short_name": "",
                    "logo": "../../../img/ufc-logos/Sean Brady.png",
                    "odds": {
                        "opening": -150,
                        "bovada": -165,
                        "betonline": -158,
                        "intertops": -160,
                        "sportsbetting": -158,
                        "mybookie": -160
                    },
                    "money_multiplier": 1.6666666666666667,
                    "win_probability": 0.6130361569589301
                },
                "team_2": {
                    "full_name": "Michael Chiesa",
                    "short_name": "",
                    "logo": "../../../img/ufc-logos/Michael Chiesa.png",
                    "odds": {
                        "opening": 120,
                        "bovada": 135,
                        "betonline": 138,
                        "intertops": 125,
                        "sportsbetting": 138,
                        "mybookie": 130
                    },
                    "money_multiplier": 2.38,
                    "win_probability": 0.4332734261721583
                }
            },
            {
                "sport": "ufc",
                "date": "Saturday November 20",
                "time": "6:00p",
                "team_1": {
                    "full_name": "Kang Kyung Ho",
                    "short_name": "",
                    "logo": "../../../img/ufc-logos/Kang Kyung Ho.png",
                    "odds": {
                        "opening": 110,
                        "bovada": -115,
                        "betonline": -115,
                        "intertops": -120,
                        "sportsbetting": -115,
                        "mybookie": -115
                    },
                    "money_multiplier": 2.1,
                    "win_probability": 0.5268633175609919
                },
                "team_2": {
                    "full_name": "Rani Yahya",
                    "short_name": "",
                    "logo": "../../../img/ufc-logos/Rani Yahya.png",
                    "odds": {
                        "opening": -130,
                        "bovada": -105,
                        "betonline": -105,
                        "intertops": -110,
                        "sportsbetting": -105,
                        "mybookie": -115
                    },
                    "money_multiplier": 1.9523809523809523,
                    "win_probability": 0.5267493336496271
                }
            },
            {
                "sport": "ufc",
                "date": "Saturday November 20",
                "time": "6:00p",
                "team_1": {
                    "full_name": "Joanne Calderwood",
                    "short_name": "",
                    "logo": "../../../img/ufc-logos/Joanne Calderwood.png",
                    "odds": {
                        "opening": 220,
                        "bovada": 270,
                        "betonline": 280,
                        "intertops": 265,
                        "sportsbetting": 280,
                        "mybookie": 285
                    },
                    "money_multiplier": 3.85,
                    "win_probability": 0.2737998203706567
                },
                "team_2": {
                    "full_name": "Taila Santos",
                    "short_name": "",
                    "logo": "../../../img/ufc-logos/Taila Santos.png",
                    "odds": {
                        "opening": -300,
                        "bovada": -360,
                        "betonline": -355,
                        "intertops": -370,
                        "sportsbetting": -355,
                        "mybookie": -360
                    },
                    "money_multiplier": 1.3333333333333333,
                    "win_probability": 0.7771484990495167
                }
            },
            {
                "sport": "ufc",
                "date": "Saturday November 20",
                "time": "6:00p",
                "team_1": {
                    "full_name": "Davey Grant",
                    "short_name": "",
                    "logo": "../../../img/ufc-logos/Davey Grant.png",
                    "odds": {
                        "opening": 200,
                        "bovada": 240,
                        "betonline": 260,
                        "intertops": 225,
                        "sportsbetting": 260,
                        "mybookie": 255
                    },
                    "money_multiplier": 3.6,
                    "win_probability": 0.29539816408084846
                },
                "team_2": {
                    "full_name": "Adrian Yanez",
                    "short_name": "",
                    "logo": "../../../img/ufc-logos/Adrian Yanez.png",
                    "odds": {
                        "opening": -260,
                        "bovada": -310,
                        "betonline": -310,
                        "intertops": -300,
                        "sportsbetting": -310,
                        "mybookie": -315
                    },
                    "money_multiplier": 1.3846153846153846,
                    "win_probability": 0.7499251749545607
                }
            },
            {
                "sport": "ufc",
                "date": "Saturday November 20",
                "time": "3:00p",
                "team_1": {
                    "full_name": "Tucker Lutz",
                    "short_name": "",
                    "logo": "../../../img/ufc-logos/Tucker Lutz.png",
                    "odds": {
                        "opening": 130,
                        "bovada": 105,
                        "betonline": 100,
                        "intertops": 105,
                        "sportsbetting": 100,
                        "mybookie": -105
                    },
                    "money_multiplier": 2.3,
                    "win_probability": 0.48709791445740547
                },
                "team_2": {
                    "full_name": "Patrick Sabatini",
                    "short_name": "",
                    "logo": "../../../img/ufc-logos/Patrick Sabatini.png",
                    "odds": {
                        "opening": -150,
                        "bovada": -125,
                        "betonline": -120,
                        "intertops": -135,
                        "sportsbetting": -120,
                        "mybookie": -125
                    },
                    "money_multiplier": 1.8333333333333333,
                    "win_probability": 0.5627480478544308
                }
            }],

		"ncaab": [
            {
                "sport": "ncaab",
                "date": "Thursday November 18",
                "time": "12:00p",
                "team_1": {
                    "full_name": "Davidson",
                    "short_name": "DAVID",
                    "logo": "../../../img/ncaab-logos/Davidson.png",
                    "odds": {
                        "opening": -132,
                        "bovada": 130,
                        "betonline": 136,
                        "intertops": 140,
                        "sportsbetting": 136,
                        "betnow": 135,
                        "mybookie": 105,
                        "gtbets": 135
                    },
                    "money_multiplier": 2.4,
                    "win_probability": 0.45084264094479465
                },
                "team_2": {
                    "full_name": "New Mexico State",
                    "short_name": "NMSU",
                    "logo": "../../../img/ncaab-logos/New Mexico State.png",
                    "odds": {
                        "opening": 118,
                        "bovada": -150,
                        "betonline": -156,
                        "intertops": -160,
                        "sportsbetting": -156,
                        "betnow": -155,
                        "mybookie": -125,
                        "gtbets": -160
                    },
                    "money_multiplier": 2.18,
                    "win_probability": 0.5839541899887455
                }
            },
            {
                "sport": "ncaab",
                "date": "Thursday November 18",
                "time": "2:00p",
                "team_1": {
                    "full_name": "St. Bonaventure",
                    "short_name": "BONA",
                    "logo": "../../../img/ncaab-logos/St. Bonaventure.png",
                    "odds": {
                        "opening": -302,
                        "bovada": -180,
                        "betonline": -176,
                        "intertops": -180,
                        "sportsbetting": -176,
                        "betnow": -165,
                        "mybookie": -165,
                        "gtbets": -185
                    },
                    "money_multiplier": 1.606060606060606,
                    "win_probability": 0.6508407764418576
                },
                "team_2": {
                    "full_name": "Boise State",
                    "short_name": "BOISE",
                    "logo": "../../../img/ncaab-logos/Boise State.png",
                    "odds": {
                        "opening": 263,
                        "bovada": 155,
                        "betonline": 156,
                        "intertops": 160,
                        "sportsbetting": 156,
                        "betnow": 145,
                        "mybookie": 145,
                        "gtbets": 155
                    },
                    "money_multiplier": 3.63,
                    "win_probability": 0.3802484667977172
                }
            },
            {
                "sport": "ncaab",
                "date": "Thursday November 18",
                "time": "2:49p",
                "team_1": {
                    "full_name": "Pennsylvania",
                    "short_name": "PENN",
                    "logo": "../../../img/ncaab-logos/Pennsylvania.png",
                    "odds": {
                        "opening": 415,
                        "bovada": 290,
                        "betonline": 295,
                        "intertops": 295,
                        "sportsbetting": 295,
                        "betnow": 313,
                        "mybookie": 315,
                        "gtbets": 280
                    },
                    "money_multiplier": 5.15,
                    "win_probability": 0.2445413981677177
                },
                "team_2": {
                    "full_name": "Utah State",
                    "short_name": "UTST",
                    "logo": "../../../img/ncaab-logos/Utah State.png",
                    "odds": {
                        "opening": -485,
                        "bovada": -380,
                        "betonline": -365,
                        "intertops": -370,
                        "sportsbetting": -365,
                        "betnow": -375,
                        "mybookie": -375,
                        "gtbets": -370
                    },
                    "money_multiplier": 1.273972602739726,
                    "win_probability": 0.7930043027965265
                }
            },
            {
                "sport": "ncaab",
                "date": "Thursday November 18",
                "time": "3:00p",
                "team_1": {
                    "full_name": "UNC Greensboro",
                    "short_name": "UNCG",
                    "logo": "../../../img/ncaab-logos/UNC Greensboro.png",
                    "odds": {
                        "opening": -450,
                        "bovada": -470,
                        "betonline": -480,
                        "intertops": -450,
                        "sportsbetting": -480,
                        "betnow": -450,
                        "mybookie": -500,
                        "gtbets": -495
                    },
                    "money_multiplier": 1.2222222222222223,
                    "win_probability": 0.8249431722862384
                },
                "team_2": {
                    "full_name": "Wisconsin-Green Bay",
                    "short_name": "UWGB",
                    "logo": "../../../img/ncaab-logos/Wisconsin-Green Bay.png",
                    "odds": {
                        "opening": 360,
                        "bovada": 345,
                        "betonline": 390,
                        "intertops": 350,
                        "sportsbetting": 390,
                        "betnow": 360,
                        "mybookie": 400,
                        "gtbets": 385
                    },
                    "money_multiplier": 5.0,
                    "win_probability": 0.21200909554473768
                }
            },
            {
                "sport": "ncaab",
                "date": "Thursday November 18",
                "time": "4:30p",
                "team_1": {
                    "full_name": "Clemson",
                    "short_name": "CLEM",
                    "logo": "../../../img/ncaab-logos/Clemson.png",
                    "odds": {
                        "opening": -181,
                        "bovada": -260,
                        "betonline": -240,
                        "intertops": -240,
                        "sportsbetting": -240,
                        "betnow": -235,
                        "mybookie": -220,
                        "gtbets": -245
                    },
                    "money_multiplier": 1.5524861878453038,
                    "win_probability": 0.6978918574718025
                },
                "team_2": {
                    "full_name": "Temple",
                    "short_name": "TEMP",
                    "logo": "../../../img/ncaab-logos/Temple.png",
                    "odds": {
                        "opening": 164,
                        "bovada": 215,
                        "betonline": 200,
                        "intertops": 200,
                        "sportsbetting": 200,
                        "betnow": 195,
                        "mybookie": 190,
                        "gtbets": 205
                    },
                    "money_multiplier": 3.15,
                    "win_probability": 0.33849096072019585
                }
            },
            {
                "sport": "ncaab",
                "date": "Thursday November 18",
                "time": "5:30p",
                "team_1": {
                    "full_name": "UMass",
                    "short_name": "UMASS",
                    "logo": "../../../img/ncaab-logos/UMass.png",
                    "odds": {
                        "opening": -118,
                        "bovada": 120,
                        "betonline": 115,
                        "intertops": 120,
                        "sportsbetting": 115,
                        "betnow": 125,
                        "mybookie": 120,
                        "gtbets": 115
                    },
                    "money_multiplier": 2.25,
                    "win_probability": 0.46808925611997937
                },
                "team_2": {
                    "full_name": "Weber State",
                    "short_name": "WEBER",
                    "logo": "../../../img/ncaab-logos/Weber State.png",
                    "odds": {
                        "opening": -102,
                        "bovada": -140,
                        "betonline": -135,
                        "intertops": -140,
                        "sportsbetting": -135,
                        "betnow": -145,
                        "mybookie": -140,
                        "gtbets": -135
                    },
                    "money_multiplier": 1.9803921568627452,
                    "win_probability": 0.5712739356328165
                }
            }],
		
        "ncaaf": [
            {
                "sport": "ncaaf",
                "date": "Friday November 19",
                "time": "8:00p",
                "team_1": {
                    "full_name": "Southern Miss",
                    "short_name": "SMISS",
                    "logo": "../../../img/ncaaf-logos/Southern Miss.png",
                    "odds": {
                        "opening": 600,
                        "bovada": 525,
                        "betonline": 520,
                        "intertops": 550,
                        "sportsbetting": 520,
                        "betnow": 500,
                        "mybookie": 525,
                        "gtbets": 165
                    },
                    "money_multiplier": 7.0,
                    "win_probability": 0.18541363738716143
                },
                "team_2": {
                    "full_name": "LA Tech",
                    "short_name": "LTECH",
                    "logo": "../../../img/ncaaf-logos/LA Tech.png",
                    "odds": {
                        "opening": -900,
                        "bovada": -800,
                        "betonline": -700,
                        "intertops": -800,
                        "sportsbetting": -700,
                        "betnow": -700,
                        "mybookie": -750,
                        "gtbets": -240
                    },
                    "money_multiplier": 1.4166666666666667,
                    "win_probability": 0.8613766339869281
                }
            },
            {
                "sport": "ncaaf",
                "date": "Friday November 19",
                "time": "9:00p",
                "team_1": {
                    "full_name": "Arizona",
                    "short_name": "ARIZ",
                    "logo": "../../../img/ncaaf-logos/Arizona.png",
                    "odds": {
                        "opening": 450,
                        "bovada": 450,
                        "betonline": 460,
                        "intertops": 485,
                        "sportsbetting": 460,
                        "betnow": 475,
                        "mybookie": 475,
                        "gtbets": 165
                    },
                    "money_multiplier": 5.85,
                    "win_probability": 0.20211299615524386
                },
                "team_2": {
                    "full_name": "Washington State",
                    "short_name": "WAZZU",
                    "logo": "../../../img/ncaaf-logos/Washington State.png",
                    "odds": {
                        "opening": -600,
                        "bovada": -665,
                        "betonline": -600,
                        "intertops": -680,
                        "sportsbetting": -600,
                        "betnow": -650,
                        "mybookie": -650,
                        "gtbets": -240
                    },
                    "money_multiplier": 1.4166666666666667,
                    "win_probability": 0.8439650219061984
                }
            },
            {
                "sport": "ncaaf",
                "date": "Friday November 19",
                "time": "9:00p",
                "team_1": {
                    "full_name": "Memphis",
                    "short_name": "MEM",
                    "logo": "../../../img/ncaaf-logos/Memphis.png",
                    "odds": {
                        "opening": 300,
                        "bovada": 275,
                        "betonline": 270,
                        "intertops": 280,
                        "sportsbetting": 270,
                        "betnow": 275,
                        "mybookie": 270,
                        "gtbets": 140
                    },
                    "money_multiplier": 4.0,
                    "win_probability": 0.2842460881934566
                },
                "team_2": {
                    "full_name": "Houston",
                    "short_name": "HOU",
                    "logo": "../../../img/ncaaf-logos/Houston.png",
                    "odds": {
                        "opening": -360,
                        "bovada": -350,
                        "betonline": -325,
                        "intertops": -350,
                        "sportsbetting": -325,
                        "betnow": -335,
                        "mybookie": -340,
                        "gtbets": -170
                    },
                    "money_multiplier": 1.588235294117647,
                    "win_probability": 0.7550059825999061
                }
            },
            {
                "sport": "ncaaf",
                "date": "Friday November 19",
                "time": "9:00p",
                "team_1": {
                    "full_name": "Air Force",
                    "short_name": "AIRFO",
                    "logo": "../../../img/ncaaf-logos/Air Force.png",
                    "odds": {
                        "opening": -103,
                        "bovada": -105,
                        "betonline": -105,
                        "intertops": -105,
                        "sportsbetting": -105,
                        "betnow": -102,
                        "mybookie": 105,
                        "gtbets": -115
                    },
                    "money_multiplier": 2.05,
                    "win_probability": 0.5104760930493716
                },
                "team_2": {
                    "full_name": "Nevada",
                    "short_name": "NEV",
                    "logo": "../../../img/ncaaf-logos/Nevada.png",
                    "odds": {
                        "opening": -117,
                        "bovada": -115,
                        "betonline": -115,
                        "intertops": -115,
                        "sportsbetting": -115,
                        "betnow": -118,
                        "mybookie": -125,
                        "gtbets": -125
                    },
                    "money_multiplier": 1.8695652173913044,
                    "win_probability": 0.5413876131767761
                }
            },
            {
                "sport": "ncaaf",
                "date": "Friday November 19",
                "time": "11:30p",
                "team_1": {
                    "full_name": "San Diego State",
                    "short_name": "SDST",
                    "logo": "../../../img/ncaaf-logos/San Diego State.png",
                    "odds": {
                        "opening": -425,
                        "bovada": -445,
                        "betonline": -430,
                        "intertops": -450,
                        "sportsbetting": -430,
                        "betnow": -420,
                        "mybookie": -450,
                        "gtbets": -200
                    },
                    "money_multiplier": 1.5,
                    "win_probability": 0.7949252113935341
                },
                "team_2": {
                    "full_name": "UNLV",
                    "short_name": "UNLV",
                    "logo": "../../../img/ncaaf-logos/UNLV.png",
                    "odds": {
                        "opening": 340,
                        "bovada": 330,
                        "betonline": 350,
                        "intertops": 350,
                        "sportsbetting": 350,
                        "betnow": 335,
                        "mybookie": 350,
                        "gtbets": 150
                    },
                    "money_multiplier": 4.5,
                    "win_probability": 0.2473256016459705
                }
            },
            {
                "sport": "ncaaf",
                "date": "Saturday November 20",
                "time": "12:00p",
                "team_1": {
                    "full_name": "Wake Forest",
                    "short_name": "WAKE",
                    "logo": "../../../img/ncaaf-logos/Wake Forest.png",
                    "odds": {
                        "opening": 138,
                        "bovada": 165,
                        "betonline": 170,
                        "intertops": 170,
                        "sportsbetting": 170,
                        "betnow": 165,
                        "mybookie": 165,
                        "gtbets": 170
                    },
                    "money_multiplier": 2.7,
                    "win_probability": 0.3792156275508106
                },
                "team_2": {
                    "full_name": "Clemson",
                    "short_name": "CLEM",
                    "logo": "../../../img/ncaaf-logos/Clemson.png",
                    "odds": {
                        "opening": -152,
                        "bovada": -195,
                        "betonline": -195,
                        "intertops": -200,
                        "sportsbetting": -195,
                        "betnow": -190,
                        "mybookie": -195,
                        "gtbets": -195
                    },
                    "money_multiplier": 1.6578947368421053,
                    "win_probability": 0.6537623036746356
                }
            }],
		
        "nfl": [
            {
                "sport": "nfl",
                "date": "Sunday November 21",
                "time": "1:00p",
                "team_1": {
                    "full_name": "Houston",
                    "short_name": "HOU",
                    "logo": "../../../img/nfl-logos/Houston.png",
                    "odds": {
                        "opening": 425,
                        "bovada": 360,
                        "betonline": 360,
                        "intertops": 350,
                        "sportsbetting": 360,
                        "betnow": 355,
                        "mybookie": 370,
                        "gtbets": 360
                    },
                    "money_multiplier": 5.25,
                    "win_probability": 0.21435122591459316
                },
                "team_2": {
                    "full_name": "Tennessee",
                    "short_name": "TEN",
                    "logo": "../../../img/nfl-logos/Tennessee.png",
                    "odds": {
                        "opening": -550,
                        "bovada": -500,
                        "betonline": -450,
                        "intertops": -450,
                        "sportsbetting": -450,
                        "betnow": -460,
                        "mybookie": -475,
                        "gtbets": -460
                    },
                    "money_multiplier": 1.2222222222222223,
                    "win_probability": 0.8253720916764394
                }
            },
            {
                "sport": "nfl",
                "date": "Sunday November 21",
                "time": "1:00p",
                "team_1": {
                    "full_name": "Green Bay",
                    "short_name": "GB",
                    "logo": "../../../img/nfl-logos/Green Bay.png",
                    "odds": {
                        "opening": -125,
                        "bovada": -125,
                        "betonline": -117,
                        "intertops": -120,
                        "sportsbetting": -117,
                        "betnow": -120,
                        "mybookie": -130,
                        "gtbets": -120
                    },
                    "money_multiplier": 1.8547008547008548,
                    "win_probability": 0.5488791440754974
                },
                "team_2": {
                    "full_name": "Minnesota",
                    "short_name": "MIN",
                    "logo": "../../../img/nfl-logos/Minnesota.png",
                    "odds": {
                        "opening": 110,
                        "bovada": 105,
                        "betonline": -103,
                        "intertops": 100,
                        "sportsbetting": -103,
                        "betnow": 100,
                        "mybookie": 110,
                        "gtbets": 100
                    },
                    "money_multiplier": 2.1,
                    "win_probability": 0.4943705194441107
                }
            },
            {
                "sport": "nfl",
                "date": "Sunday November 21",
                "time": "1:00p",
                "team_1": {
                    "full_name": "Baltimore",
                    "short_name": "BAL",
                    "logo": "../../../img/nfl-logos/Baltimore.png",
                    "odds": {
                        "opening": -275,
                        "bovada": -240,
                        "betonline": -220,
                        "intertops": -220,
                        "sportsbetting": -220,
                        "betnow": -225,
                        "mybookie": -205,
                        "gtbets": -225
                    },
                    "money_multiplier": 1.4878048780487805,
                    "win_probability": 0.6948077773038598
                },
                "team_2": {
                    "full_name": "Chicago",
                    "short_name": "CHI",
                    "logo": "../../../img/nfl-logos/Chicago.png",
                    "odds": {
                        "opening": 230,
                        "bovada": 200,
                        "betonline": 190,
                        "intertops": 180,
                        "sportsbetting": 190,
                        "betnow": 185,
                        "mybookie": 175,
                        "gtbets": 195
                    },
                    "money_multiplier": 3.3,
                    "win_probability": 0.3420822841733205
                }
            },
            {
                "sport": "nfl",
                "date": "Sunday November 21",
                "time": "1:00p",
                "team_1": {
                    "full_name": "Indianapolis",
                    "short_name": "IND",
                    "logo": "../../../img/nfl-logos/Indianapolis.png",
                    "odds": {
                        "opening": 250,
                        "bovada": 265,
                        "betonline": 265,
                        "intertops": 260,
                        "sportsbetting": 265,
                        "betnow": 265,
                        "mybookie": 270,
                        "gtbets": 265
                    },
                    "money_multiplier": 3.7,
                    "win_probability": 0.27545316843262047
                },
                "team_2": {
                    "full_name": "Buffalo",
                    "short_name": "BUF",
                    "logo": "../../../img/nfl-logos/Buffalo.png",
                    "odds": {
                        "opening": -300,
                        "bovada": -330,
                        "betonline": -315,
                        "intertops": -320,
                        "sportsbetting": -315,
                        "betnow": -330,
                        "mybookie": -340,
                        "gtbets": -330
                    },
                    "money_multiplier": 1.3333333333333333,
                    "win_probability": 0.7631287381480012
                }
            },
            {
                "sport": "nfl",
                "date": "Sunday November 21",
                "time": "1:00p",
                "team_1": {
                    "full_name": "New Orleans",
                    "short_name": "NO",
                    "logo": "../../../img/nfl-logos/New Orleans.png",
                    "odds": {
                        "opening": -108,
                        "bovada": 105,
                        "betonline": 110,
                        "intertops": 110,
                        "sportsbetting": 110,
                        "betnow": 110,
                        "mybookie": 110,
                        "gtbets": 110
                    },
                    "money_multiplier": 2.1,
                    "win_probability": 0.4830223130528009
                },
                "team_2": {
                    "full_name": "Philadelphia",
                    "short_name": "PHI",
                    "logo": "../../../img/nfl-logos/Philadelphia.png",
                    "odds": {
                        "opening": -105,
                        "bovada": -125,
                        "betonline": -130,
                        "intertops": -130,
                        "sportsbetting": -130,
                        "betnow": -130,
                        "mybookie": -130,
                        "gtbets": -130
                    },
                    "money_multiplier": 1.9523809523809523,
                    "win_probability": 0.5573818781666077
                }
            },
            {
                "sport": "nfl",
                "date": "Sunday November 21",
                "time": "1:00p",
                "team_1": {
                    "full_name": "Miami",
                    "short_name": "MIA",
                    "logo": "../../../img/nfl-logos/Miami.png",
                    "odds": {
                        "opening": -133,
                        "bovada": -180,
                        "betonline": -177,
                        "intertops": -180,
                        "sportsbetting": -177,
                        "betnow": -185,
                        "mybookie": -185,
                        "gtbets": -185
                    },
                    "money_multiplier": 1.7518796992481203,
                    "win_probability": 0.6352345620951093
                },
                "team_2": {
                    "full_name": "NY Jets",
                    "short_name": "NYJ",
                    "logo": "../../../img/nfl-logos/NY Jets.png",
                    "odds": {
                        "opening": 115,
                        "bovada": 155,
                        "betonline": 157,
                        "intertops": 160,
                        "sportsbetting": 157,
                        "betnow": 155,
                        "mybookie": 160,
                        "gtbets": 160
                    },
                    "money_multiplier": 2.6,
                    "win_probability": 0.39768578439220437
                }
            }],
        
        "boxing": [
            {
                "sport": "boxing",
                "date": "Friday November 19",
                "time": "8:00p",
                "team_1": {
                    "full_name": "Murodjon Akhmadaliev",
                    "short_name": "",
                    "logo": "../../../img/boxing-logos/Murodjon Akhmadaliev.png",
                    "odds": {
                        "opening": -400,
                        "bovada": -600,
                        "betonline": -600,
                        "intertops": -556,
                        "sportsbetting": -600,
                        "betnow": -500,
                        "mybookie": -510,
                        "gtbets": None,
                        "skybook": None
                    },
                    "money_multiplier": 1.25,
                    "win_probability": 0.8411983505917361
                },
                "team_2": {
                    "full_name": "Ronny Rios",
                    "short_name": "",
                    "logo": "../../../img/boxing-logos/Ronny Rios.png",
                    "odds": {
                        "opening": 270,
                        "bovada": 375,
                        "betonline": 400,
                        "intertops": 360,
                        "sportsbetting": 400,
                        "betnow": 400,
                        "mybookie": 380,
                        "gtbets": None,
                        "skybook": None
                    },
                    "money_multiplier": 5.0,
                    "win_probability": 0.2152173176772719
                }
            },
            {
                "sport": "boxing",
                "date": "Friday November 19",
                "time": "9:00p",
                "team_1": {
                    "full_name": "McWilliams Arroyo",
                    "short_name": "",
                    "logo": "../../../img/boxing-logos/McWilliams Arroyo.png",
                    "odds": {
                        "opening": 853,
                        "bovada": 700,
                        "betonline": 650,
                        "intertops": 700,
                        "sportsbetting": 650,
                        "betnow": 850,
                        "mybookie": 825,
                        "gtbets": None,
                        "skybook": None
                    },
                    "money_multiplier": 9.53,
                    "win_probability": 0.11928138957188496
                },
                "team_2": {
                    "full_name": "Julio Cesar Martinez Aguilar",
                    "short_name": "",
                    "logo": "../../../img/boxing-logos/Julio Cesar Martinez Aguilar.png",
                    "odds": {
                        "opening": -1427,
                        "bovada": -1400,
                        "betonline": -1200,
                        "intertops": -1429,
                        "sportsbetting": -1200,
                        "betnow": -1300,
                        "mybookie": -1300,
                        "gtbets": None,
                        "skybook": None
                    },
                    "money_multiplier": 1.0833333333333333,
                    "win_probability": 0.9293914183161586
                }
            },
            {
                "sport": "boxing",
                "date": "Friday November 19",
                "time": "10:00p",
                "team_1": {
                    "full_name": "Demetrius Andrade",
                    "short_name": "",
                    "logo": "../../../img/boxing-logos/Demetrius Andrade.png",
                    "odds": {
                        "opening": -588,
                        "bovada": -1800,
                        "betonline": -1600,
                        "intertops": -2500,
                        "sportsbetting": -1600,
                        "betnow": -1900,
                        "mybookie": -1500,
                        "gtbets": None,
                        "skybook": None
                    },
                    "money_multiplier": 1.1700680272108843,
                    "win_probability": 0.9333444266511802
                },
                "team_2": {
                    "full_name": "Jason Quigley",
                    "short_name": "",
                    "logo": "../../../img/boxing-logos/Jason Quigley.png",
                    "odds": {
                        "opening": 365,
                        "bovada": 725,
                        "betonline": 800,
                        "intertops": 900,
                        "sportsbetting": 800,
                        "betnow": 1200,
                        "mybookie": 750,
                        "gtbets": None,
                        "skybook": None
                    },
                    "money_multiplier": 13.0,
                    "win_probability": 0.12186546323168715
                }
            },
            {
                "sport": "boxing",
                "date": "Saturday November 20",
                "time": "12:00p",
                "team_1": {
                    "full_name": "Nick Campbell",
                    "short_name": "",
                    "logo": "../../../img/boxing-logos/Nick Campbell.png",
                    "odds": {
                        "opening": -2000,
                        "bovada": -2000,
                        "betonline": -1800,
                        "intertops": -2000,
                        "sportsbetting": -1800,
                        "betnow": None,
                        "mybookie": -1500,
                        "gtbets": None,
                        "skybook": None
                    },
                    "money_multiplier": 1.0666666666666667,
                    "win_probability": 0.9482299498746868
                },
                "team_2": {
                    "full_name": "Danny Whitaker",
                    "short_name": "",
                    "logo": "../../../img/boxing-logos/Danny Whitaker.png",
                    "odds": {
                        "opening": 750,
                        "bovada": 900,
                        "betonline": 900,
                        "intertops": 800,
                        "sportsbetting": 900,
                        "betnow": None,
                        "mybookie": 750,
                        "gtbets": None,
                        "skybook": None
                    },
                    "money_multiplier": 10.0,
                    "win_probability": 0.10773420479302832
                }
            },
            {
                "sport": "boxing",
                "date": "Saturday November 20",
                "time": "12:00p",
                "team_1": {
                    "full_name": "Christopher Diaz",
                    "short_name": "",
                    "logo": "../../../img/boxing-logos/Christopher Diaz.png",
                    "odds": {
                        "opening": 135,
                        "bovada": 130,
                        "betonline": 130,
                        "intertops": 125,
                        "sportsbetting": 130,
                        "betnow": None,
                        "mybookie": 130,
                        "gtbets": None,
                        "skybook": None
                    },
                    "money_multiplier": 2.35,
                    "win_probability": 0.434851132353445
                },
                "team_2": {
                    "full_name": "Isaac Dogboe",
                    "short_name": "",
                    "logo": "../../../img/boxing-logos/Isaac Dogboe.png",
                    "odds": {
                        "opening": -175,
                        "bovada": -170,
                        "betonline": -160,
                        "intertops": -175,
                        "sportsbetting": -160,
                        "betnow": None,
                        "mybookie": -160,
                        "gtbets": None,
                        "skybook": None
                    },
                    "money_multiplier": 1.625,
                    "win_probability": 0.624751791418458
                }
            },
            {
                "sport": "boxing",
                "date": "Saturday November 20",
                "time": "2:00p",
                "team_1": {
                    "full_name": "Florian Marku",
                    "short_name": "",
                    "logo": "../../../img/boxing-logos/Florian Marku.png",
                    "odds": {
                        "opening": -10000,
                        "bovada": -6600,
                        "betonline": -5000,
                        "intertops": -5000,
                        "sportsbetting": -5000,
                        "betnow": None,
                        "mybookie": -3000,
                        "gtbets": None,
                        "skybook": None
                    },
                    "money_multiplier": 1.0333333333333334,
                    "win_probability": 0.9806820071397947
                },
                "team_2": {
                    "full_name": "Jorick Luisetto",
                    "short_name": "",
                    "logo": "../../../img/boxing-logos/Jorick Luisetto.png",
                    "odds": {
                        "opening": 1200,
                        "bovada": 1300,
                        "betonline": 1600,
                        "intertops": 1000,
                        "sportsbetting": 1600,
                        "betnow": None,
                        "mybookie": 1100,
                        "gtbets": None,
                        "skybook": None
                    },
                    "money_multiplier": 17.0,
                    "win_probability": 0.07337352190293366
                }
            }]}
    
    return fake[sport_league]