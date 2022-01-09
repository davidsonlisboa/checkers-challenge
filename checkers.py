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

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Checkers")
        self.screen = pygame.display.set_mode((374,400))
        self.background = pygame.image.load('board.png')
        self.font = pygame.font.Font("freesansbold.ttf", 22)
        self.player1 = Player(1)
        self.player2 = Player(2)
        self.turn = 0

    def run(self):
        while True:
            mx, my = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    pygame.quit()
                elif (event.type == KEYDOWN):
                    if (event.key == K_ESCAPE):
                        pygame.quit()
                print(event)

            self.screen.blit(self.background,(0,0))
            self.player1.discs.draw(self.screen)
            self.player2.discs.draw(self.screen)
            pygame.display.update()
            self.updateTurn()

    def updateTurn(self):
            if (self.turn == 0):
                text = self.font.render("Player 1 turn! ", True, (255, 255, 255))
                self.screen.blit(text, (130,380))
                self.turn = 1
            else:
                text = self.font.render("Player 2 turn! ", True, (255, 255, 255))
                self.screen.blit(text, (130,380))
                self.turn = 0


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

#starts the game
if (__name__ == '__main__'):
    game = Game()
    game.run()