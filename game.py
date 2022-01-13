############################################
#      Code by:                            #
#      Davidson Lisboa                     #
#                                          #
#             CHECKERS                     #
#                                          #
############################################

import pygame
from pygame.locals import *
from disc import *
from player import *

class Game:
    '''
    Main class that runs the game
    All the essential variables are contained in this class
    '''
    def __init__(self):
        '''
        Initialize the variables and the sprites that will be displayed
        '''
        pygame.init()
        self.running = True
        pygame.display.set_caption("Checkers")
        self.screen = pygame.display.set_mode((374,400))
        self.background = pygame.image.load('board.png')
        self.font = pygame.font.Font(None, 22)
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.move = False
        self.movingDisc = Disc(0,0,0)
        self.discPos = [0,0]
        self.turn = 1

    def run(self):
        '''
        While the game is running, check the current event and update the display
        '''
        while self.running:
            self.eventHandler()
            self.updateWindow()
            pygame.display.update()

    def updateWindow(self):
        '''
        Draws the background image, the pieces, the turn, and checks if there is a winner already
        '''
        pygame.draw.rect(self.screen, (0,0,0), [5,300,360,374])
        self.screen.blit(self.background,(0,0))
        self.player1.discs.draw(self.screen)
        self.player2.discs.draw(self.screen)
        text = self.font.render("Player " + str(self.turn) + " turn!", 1, (255, 255, 255))
        self.screen.blit(text, (5,380))
        self.checkEnd()

    def eventHandler(self):
        '''
        All actions the player takes are registered in this method. 
        Checks if the game must be closed when pressing ESC key or close the window.
        When the mouse is pressed down, checks if collides with other players pieces
        If the mouse collided, set the movement flag to True and tracks the position until the mouse is released
        '''
        a = Disc(0,0,0)
        b = Disc(0,0,0)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                self.running = False

            if (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    self.running = False
            
            if (event.type == MOUSEBUTTONDOWN):
                a = self.player1.checkMouse(event.pos, self.player2.discs)
                b = self.player2.checkMouse(event.pos, self.player1.discs)
                
                if (a.x!=0 and a.y!=0):
                    self.movingDisc = a
                    self.move = True
                    self.discPos = [a.x,a.y]
                if (b.x!=0 and b.y!=0):
                    self.movingDisc = b
                    self.move = True
                    self.discPos = [b.x,b.y]
                    
            if (event.type == MOUSEBUTTONUP):
                if (self.move == True):
                    self.updateTurn()
                self.move = False
                self.movingDisc.checkMove(self.discPos)

            if (event.type == MOUSEMOTION and self.move == True):
                self.movingDisc.moveDisc(event.pos)
                self.player1.checkMouse(event.pos, self.player2.discs)
                self.player2.checkMouse(event.pos, self.player1.discs) 

            print(event)

    def updateTurn(self):
        '''
        Changes the turn to the next player
        '''
        if (self.turn == 1):
            self.turn = 2
        else:
            self.turn = 1

    def checkEnd(self):
        '''
        If the game is over (there are no more discs), display the winner on the screen.
        '''
        winner = 0
        if (not self.player1.discs):
            winner = 2
        elif(not self.player2.discs):
            winner = 1
        if (winner != 0):
            text = self.font.render("Player " + str(winner) + " Won!", 1, (255, 255, 255))
            self.screen.blit(text, (200, 380))

if (__name__ == '__main__'):
    '''
    Checks if the file is running, then creates the game
    '''
    game = Game()
    game.run()