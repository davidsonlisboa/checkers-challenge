import unittest
from disc import *

class TestDisc(unittest.TestCase):

    def testCheckKing(self):
        '''
        Tests if the pieces are turning kings when it is necessary.
        '''
        disc = Disc('red', 0, 330)
        disc.checkKing()
        self.assertEqual(disc.king, False)
        disc. y = 350
        disc.checkKing()
        self.assertEqual(disc.king, True)


    def testMouseCollision(self):
        '''
        Tests if the mouseCollision method is returning the right boolean value when the mouse hits a disc.
        '''
        disc = Disc('red', 130, 200)
        self.assertEqual(disc.checkMouseCollision([50,30]), False)
        self.assertEqual(disc.checkMouseCollision([130,180]), True)
