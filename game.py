from partie import Partie
import pygame

class Game:

    def __init__(self):
        self.part = Partie()

    def play(self,screen):
        screen.blit(self.part.image, self.part.rect) #met la grille dans screen
        self.part.all_case_comp.draw(screen) #dessine les cases
        

                  


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