import unittest
from game import *

class TestGame(unittest.TestCase):

    def testUpdateTurn(self):
        '''
        Test to see if the method is updating the round correctly.
        '''
        game = Game()
        self.assertEqual(game.turn, 1)
        game.updateTurn()
        self.assertEqual(game.turn, 2)
