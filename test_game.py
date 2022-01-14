import unittest
from game import *

class TestGame(unittest.TestCase):

    def testUpdateTurn(self):
        game = Game()
        self.assertEqual(game.turn, 1)
        game.updateTurn()
        self.assertEqual(game.turn, 2)
