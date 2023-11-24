import pygame
from game import Game

pygame.init()

pygame.display.set_caption("tic tac toe","assets/icon.jpg")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load("assets/background.jpg")

game = Game()


running =  True

while running:

   screen.blit(background, (0,0))
   screen.blit(game.part.fond, game.part.rect_fond)

   pygame.display.flip()


   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                print("a")