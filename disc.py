import pygame
from pygame.locals import *

class Disc(pygame.sprite.Sprite):
    def __init__(self,color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.king = False
        self.x = x
        self.y = y
        if (color == 'red'):
            self.image = pygame.image.load('red.png')
        else:
            self.image = pygame.image.load('blue.png')
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def position(self):
        return

    def moveDisc():
        return

    #adicionar imagem diferente/numero em cima com draw
    def turnKing(self):
        self.king = True
