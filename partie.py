import pygame
from case import Case

class Partie(pygame.sprite.Sprite):

    def __init__ (self):
        super().__init__()
        self.tab = [[0 for _ in range(3)] for _ in range (3)]
        self.all_case_comp = pygame.sprite.Group()
        self.fin = False
        self.player = 1
        self.image = pygame.image.load("assets/tab.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 240
        self.rect.y = 60

        
    #turn aura d'autre argument pour la case designe
    def turn (self,i,j):
        self.all_case_comp.add(Case(self.player,i,j))
        self.player = 1 if self.player ==2 else 2 #permet de changer de joueur apres avoir clique

