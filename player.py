import pygame
from pygame.locals import *
from disc import *


class Player:
    '''
    Class that represents the player, has a group of pieces associated.
    '''
    def __init__(self, number):
        self.discs = pygame.sprite.Group()
        self.number = number
        self.placePieces()

    def mouseClick(self, mouse, discs, turn):
        '''
        Receives the mouse position and a group of discs. Checks if the mouse intercepts a disc.
        If the mouse is intercepting a piece, this piece is later returned to the eventHandler method to keep moving.
        The method returns an empty disc otherwise. 
        Then moves the disc to the current mouse position.
        '''
        for i in self.discs:
            if (i.checkMouseCollision(mouse) and turn==1):
                    i.moveDisc(mouse)
                    return i

        for i in discs:
            if (i.checkMouseCollision(mouse) and turn==2):
                    i.moveDisc(mouse)
                    return i

        return Disc(0,0,0)

    def checkPiecesCollision(self, turn, discs, pos1, pos2):
        '''
        Checks if we must delete any other player discs.
        Calculating the position according to the color.
        '''
        x = 0
        y = 0
        if (turn==1):
            if (pos1[0]- pos2[0] > 0):
                x = pos2[0] + 50
            else:
                x = pos2[0] - 50
            y = pos2[1]-50 
            for i in discs:
                if (i.checkMouseCollision([x,y])):
                    i.kill()
        else:
            if (pos1[0]- pos2[0] > 0):
                x = pos2[0] + 50
            else:
                x = pos2[0] - 50
            y = pos2[1]+50
            for i in self.discs:
                if (i.checkMouseCollision([x,y])):
                    i.kill()
        
            

    def placePieces(self):
        '''
        Places the pieces on the board, adjusting by the color and current number of the piece.
        Each If statement inside the loop is one row of the board.
        Every position is calculated with an offset value to separate the discs. 
        '''
        if (self.number == 1):
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