import pygame
from pygame.locals import *

class Disc(pygame.sprite.Sprite):
    '''
    Class that represents a disc in the board.
    '''
    def __init__(self, color, x, y):
        '''
        Initializes the coordinates, icon, and the rectangle of the piece.
        '''
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.king = False
        self.color = color
        self.loadIcon()
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]

    def loadIcon(self):
        '''
        Loads the icon into the center of the piece. 
        The images are located inside this folder.
        '''
        if (self.color == 'red'):
            self.image = pygame.image.load('red.png')
        else:
            self.image = pygame.image.load('blue.png')

    def checkMouseCollision(self, pos):
        '''
        Checks if the mouse position is intercepting the rectangle that surrounds the piece.
        '''
        if self.rect.collidepoint(pos):
            return True

    def checkMove(self, pos):
        '''
        Checks if the movement is valid according to the checkers rules.
        The piece cannot move to the white coordinates in the board.
        Also if the piece isn't a king, it cannot move backwards.
        If the final position doesn't respect the rules, the piece comes back to the initial position.
        '''
        x,y = pos
        if (abs(self.x - x)<21):
            self.x = x
            self.y = y
            self.rect.center = [x,y]
        if (not self.king):
            if (self.color == 'red'):
                if ((self.y - y)<35 or (self.y - y)>95):
                    self.x = x
                    self.y = y
                    self.rect.center = [x,y]
            else:
                if ((y - self.y)<35 or (y - self.y)>95):
                    self.x = x
                    self.y = y
                    self.rect.center = [x,y]
        else:
            if (abs(self.y - y)<35 or abs(self.y - y)>95):
                    self.x = x
                    self.y = y
                    self.rect.center = [x,y]

    def moveDisc(self, pos):
        '''
        Moves the piece to the received position and checks if the piece needs to turn into a king.
        '''
        x,y = pos
        self.x = x
        self.y = y
        self.rect.center = [x,y]
        self.checkKing()

    def checkKing(self):
        '''
        If the y coordinate of the piece exceeds the specified value, the piece turns into a king.
        These y values changes if the piece is red or blue.
        '''
        if (self.color == 'red'):
            if (self.y > 345):
                self.turnKing()
        else:
            if (self.y < 30):
                self.turnKing()

    def turnKing(self):
        '''
        Turn the piece into a king, changing the flag variable and the icon.
        '''
        self.king = True
        if (self.color == 'red'):
            self.image = pygame.image.load('red_king.png')
        else:
            self.image = pygame.image.load('blue_king.png')