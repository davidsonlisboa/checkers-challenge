import pygame
from pygame.locals import *
from disc import *

class Player:
    def __init__(self, number):
        self.discs = pygame.sprite.Group()
        if (number == 1):
            for i in range(12):
                if (i<4):
                    disc = Disc('red', 90*i + 28, 20)
                    self.discs.add(disc)
                if (i>=4 and i<8):
                    disc = Disc('red', 90*(i-4) + 74, 70)
                    self.discs.add(disc)
                if (i>=8):
                    disc = Disc('red', 90*(i-8) + 28, 118)
                    self.discs.add(disc)
        else:
            for i in range(12):
                if (i<4):
                    disc = Disc('blue', 90*i + 74, 257)
                    self.discs.add(disc)
                if (i>=4 and i<8):
                    disc = Disc('blue', 90*(i-4) + 28, 303)
                    self.discs.add(disc)
                if (i>=8):
                    disc = Disc('blue', 90*(i-8) + 74, 350)
                    self.discs.add(disc)

    def checkMouse(self, mouse, discs):
        for i in self.discs:
            if (i.checkColision(mouse)):
                    i.moveDisc(mouse)
                    pygame.sprite.groupcollide(self.discs, discs, False, True)
                    return i
        return Disc(0,0,0)