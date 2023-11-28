from partie import Partie
import pygame

class Game:

    def __init__(self):
        self.part = Partie()

    def play(self,screen):
        screen.blit(self.part.image, self.part.rect) #met la grille dans screen
        self.part.all_case_comp.draw(screen) #dessine les cases
        
        pygame.display.flip() #affiche à l'ecran

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1: #touche 1 qui sera change par un clic plus tard
                    self.part.turn (0,0)
                if event.key == pygame.K_2: 
                    self.part.turn (1,0)
                if event.key == pygame.K_3: 
                    self.part.turn (2,0)
                if event.key == pygame.K_4: 
                    self.part.turn (0,1)
                if event.key == pygame.K_5: 
                    self.part.turn (1,1)
                if event.key == pygame.K_6: 
                    self.part.turn (2,1)
                if event.key == pygame.K_7: 
                    self.part.turn (0,2)
                if event.key == pygame.K_8:
                    self.part.turn (1,2)
                if event.key == pygame.K_9:
                    self.part.turn (2,2)
                    