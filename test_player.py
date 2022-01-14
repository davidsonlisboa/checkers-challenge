import unittest
from player import *
import random

class TestPlayer(unittest.TestCase):

    def testMouseClick(self):
        '''
        Checks if the mouseClick method is returning a valid disc when the mouse hits a piece.
        '''
        player1 = Player(1)
        player2 = Player(2)
        invalidDisc = Disc(0,0,0)
        returnedDisc = player1.mouseClick([160,200], player2.discs)
        self.assertEqual(invalidDisc.color, returnedDisc.color)
        returnedDisc = player1.mouseClick([115,115], player2.discs)
        self.assertNotEqual(invalidDisc.color, returnedDisc.color)

    def testPiecesCollision(self):
        '''
        Checks if the overlapped pieces are being removed.
        '''
        player1 = Player(1)
        player2 = Player(2)
        testDisc = random.choice(player1.discs.sprites())
        testDisc.rect.center = [180,230]
        player1.checkPiecesCollision(1, player2.discs)
        for i in player2.discs:
            flag = i.checkMouseCollision([180,230])
        self.assertEqual(flag, False)