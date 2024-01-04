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
                    


                  


        if self.part.fin != None: 
            font = pygame.font.SysFont(None, 50)
            color = [(0,0,255),(255,0,0),(0,255,0)]
            if self.part.fin !=0:
                text = font.render('Joueur '+str(self.part.fin) +' a gagné', True, color[self.part.fin])
                screen.blit(text, (380, 15))
            else:
                text = font.render('Egalité', True, color[self.part.fin])
                screen.blit(text, (480, 15))
            

        pygame.display.flip() #affiche à l'ecran
