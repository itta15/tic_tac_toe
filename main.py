import pygame
from game import Game

pygame.init()

pygame.display.set_caption("tic tac toe","assets/icon.jpg")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load("assets/background.jpg")

game = Game()


running =  True

while running:

   screen.blit(background, (0,0)) #affiche le fond
   screen.blit(game.part.image, game.part.rect) #affiche la grilee
   game.part.all_case_comp.draw(screen)

   pygame.display.flip()


   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1: #touche 1 qui sera change par un clic plus tard
                game.part.turn (0,0)
                print("a")
            if event.key == pygame.K_2: 
                game.part.turn (1,0)
                print("a")
            if event.key == pygame.K_3: 
                game.part.turn (2,0)
                print("a")
            if event.key == pygame.K_4: 
                game.part.turn (0,1)
                print("a")
            if event.key == pygame.K_5: 
                game.part.turn (1,1)
                print("a")
            if event.key == pygame.K_6: 
                game.part.turn (2,1)
                print("a")
            if event.key == pygame.K_7: 
                game.part.turn (0,2)
                print("a")
            if event.key == pygame.K_8:
                game.part.turn (1,2)
                print("a")
            if event.key == pygame.K_9:
                game.part.turn (2,2)
                print("a")
