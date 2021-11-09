import unittest
import scrape_data as scraper
import requests
from bs4 import BeautifulSoup

# TO RUN, be at backend as current directory.  Run python -m unittest tests.test_scrape_data -v

class TestWebScraping(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.selectors = {
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
        cls.url = 'https://www.oddsshark.com/ncaaf/odds'
        cls.response = requests.get(cls.url)
        cls.page_html = BeautifulSoup(cls.response.content, 'html.parser')
        cls.book_names = scraper.get_sportsbook_names(cls.page_html, cls.selectors)

    def test_create_odds_object(self):
        """"""
        # Non-integer odds text (empty string, string, decimal)
        self.assertEqual(scraper.create_odds_object(
            ["book1", "book2", "book3", "book4", "book5", "book6"],
            ["10000", "-200", "0", "", "abc", "1.1"]), 
            {
                "book1": 10000,
                "book2": -200,
                "book3": 0,
                "book4": None,
                "book5": None,
                "book6": None
            })
    
        # Empty books list
        self.assertEqual(scraper.create_odds_object([],["10000", "-200", "0", "", "abc", "1.1"]), {})

        # Book name is empty
        self.assertEqual(scraper.create_odds_object(["", "book2"], ["1", "2"]), {})

        # Empty odds list
        self.assertEqual(scraper.create_odds_object(["book1", "book2", "book3"],[]),
        {
            "book1": None,
            "book2": None,
            "book3": None
            }
        )
        
        # More books than odds
        self.assertEqual(scraper.create_odds_object(["book1", "book2"],["-222"]),
        {
            "book1": -222,
            "book2": None,
            }
        )

        # More odds than books
        self.assertEqual(scraper.create_odds_object(["book1"],["-222", "100"]),
        {
            "book1": -222,
            }
        )
    

if __name__ == '__main__':
    unittest.main()