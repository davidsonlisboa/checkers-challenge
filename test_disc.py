import unittest
from disc import *

class TestDisc(unittest.TestCase):

    def testCheckKing(self):
        disc = Disc('red', 0, 330)
        disc.checkKing()
        self.assertEqual(disc.king, False)
        disc. y = 350
        disc.checkKing()
        self.assertEqual(disc.king, True)


    def testMouseCollision(self):
        disc = Disc('red', 130, 200)
        self.assertEqual(disc.checkMouseCollision([50,30]), False)
        self.assertEqual(disc.checkMouseCollision([130,180]), True)
