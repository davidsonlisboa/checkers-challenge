import pygame
from pygame.locals import *

class Disc(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.color = color
        self.loadIcon()
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def loadIcon(self):
        if (self.color == 'red'):
            self.image = pygame.image.load('red.png')
        else:
            self.image = pygame.image.load('blue.png')

    def checkColision(self, pos):
        if self.rect.collidepoint(pos):
            return True

    def moveDisc(self, pos):
        x,y = pos
        self.x = x
        self.y = y
        self.rect.center = [x,y]
        if (self.checkKing()):
            self.turnKing()

    def checkKing(self):
        if (self.color == 'red'):
            if (self.y > 345):
                return True
        else:
            if (self.y < 30):
                return True
        return False

    def turnKing(self):
        if (self.color == 'red'):
            self.image = pygame.image.load('red_king.png')
        else:
            self.image = pygame.image.load('blue_king.png')

