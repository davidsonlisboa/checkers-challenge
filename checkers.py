############################################
#      Code by:                            #
#      Davidson Lisboa                     #
#                                          #
#             CHECKERS                     #
#                                          #
############################################

from types import NoneType
import pygame
from pygame.locals import *
from disc import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Checkers")
        self.screen = pygame.display.set_mode((374,400))
        self.background = pygame.image.load('board.png')
        self.font = pygame.font.Font(None, 22)
        self.player1 = Player(1)
        self.player2 = Player(2)

        self.turn = 0
        self.move = False
        self.movingDisc = Disc(0,0,0)

    def run(self):
        while True:
            self.eventHandler()
            self.screen.blit(self.background,(0,0))
            self.player1.discs.draw(self.screen)
            self.player2.discs.draw(self.screen)
            pygame.display.update()
            #self.updateTurn()
            if (not self.player1.discs):
                pygame.quit()
            elif(not self.player2.discs):
                pygame.quit()

    def eventHandler(self):
        a = Disc(0,0,0)
        b = Disc(0,0,0)
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            elif (event.type == KEYDOWN):
                if (event.key == K_ESCAPE):
                    pygame.quit()
            if (event.type == MOUSEBUTTONDOWN):
                a = self.player1.checkMouse(event.pos, self.player2.discs)
                b = self.player2.checkMouse(event.pos, self.player1.discs)

                if (a.x!=0 and a.y!=0):
                    self.movingDisc = a
                    self.move = True
                if (b.x!=0 and b.y!=0):
                    self.movingDisc = b
                    self.move = True
                    
            if (event.type == MOUSEBUTTONUP):
                self.move = False
                #self.updateTurn()

            if (event.type == MOUSEMOTION and self.move == True):
                self.movingDisc.moveDisc(event.pos)
                self.player1.checkMouse(event.pos, self.player2.discs)
                self.player2.checkMouse(event.pos, self.player1.discs) 

            print(event)

    def updateTurn(self):
            if (self.turn == 0):
                text = self.font.render("Player 1 turn! ", True, (255, 255, 255))
                self.screen.blit(text, (130,380))
                self.turn = 1
            else:
                text = self.font.render("Player 2 turn! ", True, (255, 255, 255))
                self.screen.blit(text, (130,380))
                self.turn = 0

#starts the game
if (__name__ == '__main__'):
    game = Game()
    game.run()