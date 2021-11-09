import unittest
import requests
from bs4 import BeautifulSoup
import betting_calculations as bc
import scrape_data as scraper

class TestBettingCalculations(unittest.TestCase):
    

    def test_implied_probability(self):
        self.assertAlmostEqual(bc.implied_probability(110), 0.47619047619047616)
        self.assertAlmostEqual(bc.implied_probability(-200), 0.6666666666666666)
        self.assertAlmostEqual(bc.implied_probability(0), 1.0)


    def test_win_probability_from_odds(self):
        # Average of non-null values in the dictionary argument
        self.assertAlmostEqual(round(bc.win_probability_from_odds(
            {
                "opening": -120,
                "bovada": -110,
                "betonline": -108,
                "sportsbetting": -108,
                "betnow": -107,
                "mybookie": -110,
                "gtbets": 105
            }), 4), .5195)

        # Null values are excluded from average
        self.assertAlmostEqual(round(bc.win_probability_from_odds(
            {
                "opening": 110,
                "gtbets": -200,
                "foo": None
            }), 4), 0.5714)

        # Empty odds
        self.assertEqual(bc.win_probability_from_odds({}), None)

        # Odds values are all None
        self.assertEqual(bc.win_probability_from_odds({"odd1": None, "odd2": None}), None)

    def test_optimal_odd_to_bet(self):
        self.assertEqual(bc.optimal_odd_to_bet({
                "opening": -120,
                "bovada": -110,
                "gtbets": 105
            }), 105)

        self.assertAlmostEqual(bc.optimal_odd_to_bet({
            "opening": -120,
            "bovada": -1100,
            "gtbets": -1405
        }), -120)


    def test_money_multiplier(self):
        # Odd is positive
        self.assertAlmostEqual(bc.money_multiplier(110), 2.1)

        # Odd is negative
        self.assertAlmostEqual(bc.money_multiplier(-500), 1.2)

        # Odd is zero
        self.assertAlmostEqual(bc.money_multiplier(0), None)

        # Odd is None
        self.assertAlmostEqual(bc.money_multiplier(None), None)


if __name__ == '__main__':
    unittest.main()