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
   for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.KEYDOWN:
               # if event.key == pygame.K_1: #touche 1 qui sera change par un clic plus tard
               #    game.part.turn (0,0)
               # if event.key == pygame.K_2: 
               #    game.part.turn (1,0)
               # if event.key == pygame.K_3: 
               #    game.part.turn (2,0)
               # if event.key == pygame.K_4: 
               #    game.part.turn (0,1)
               # if event.key == pygame.K_5: 
               #    game.part.turn (1,1)
               # if event.key == pygame.K_6: 
               #    game.part.turn (2,1)
               # if event.key == pygame.K_7: 
               #    game.part.turn (0,2)
               # if event.key == pygame.K_8:
               #    game.part.turn (1,2)
               # if event.key == pygame.K_9:
               #    game.part.turn (2,2)
               if event.key == pygame.K_r:
                  game = Game()  
            elif event.type = pygame.MOUSEBUTTONDOWN:
               mouse_x, mouse_y = pygame.mouse.get_pos()
               for i in range(3):
                  for j in range(3):
                     if mouse_x >= 250 + 190*j and mouse_x < 250 + 190*(j+1) and mouse_y >= 75 + 200*i and mouse_y < 75 + 200*(i+1) :
                        game.part.turn(i,j)

