import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card_1 = Card("Clubs", 1)
        self.card_2 = Card("Hearts", 2)
        self.card_3 = Card("Spades", 3)

        self.card_game = CardGame()


    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card_1))