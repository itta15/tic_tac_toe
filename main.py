import pygame
from game import Game

pygame.init()

pygame.display.set_caption("tic tac toe","assets/icon.jpg")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load("assets/background.jpg")

game = Game()

running = True

while running:

   screen.blit(background, (0,0)) #affiche le fond
   game.play(screen)

