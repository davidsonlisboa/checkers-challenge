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

    def mouseClick(self, mouse, discs):
        '''
        Receives the mouse position and a group of discs. Checks if the mouse intercepts a disc.
        If the mouse is intercepting a piece, this piece is later returned to the eventHandler method to keep moving.
        The method returns an empty disc otherwise. 
        Then moves the disc to the mouse position and check if the moving disc is overlapping any other player discs.
        The overlaped disc is deleted from the group.
        '''
        for i in self.discs:
            if (i.checkMouseCollision(mouse)):
                    i.moveDisc(mouse)
                    return i

        for i in discs:
            if (i.checkMouseCollision(mouse)):
                    i.moveDisc(mouse)
                    return i

        return Disc(0,0,0)

    def checkPiecesCollision(self, turn, discs):
        '''
        
        '''
        if (turn==1):
            pygame.sprite.groupcollide(self.discs, discs, False, True)
        else:
            pygame.sprite.groupcollide(self.discs, discs, True, False)
        

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