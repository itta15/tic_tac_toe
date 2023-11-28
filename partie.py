import pygame
from case import Case

class Partie(pygame.sprite.Sprite):

    def __init__ (self):
        super().__init__()
        self.tab = [[0 for _ in range(3)] for _ in range (3)]
        self.all_case_comp = pygame.sprite.Group()
        self.fin = 0       
        self.player = 1
        self.image = pygame.image.load("assets/tab.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 240
        self.rect.y = 60

        
    #turn aura d'autre argument pour la case designe
    def turn (self,i,j):
        if (not (self.fin) and self.tab[i][j]==0):
            self.tab[i][j] = self.player
            self.all_case_comp.add(Case(self.player,i,j))
            self.player = 1 if self.player ==2 else 2 #permet de changer de joueur apres avoir clique
            for j in range(1,3): #suivant si c'est le joueur 1 ou le 2 qui a gagne
                #on verifie les lignes et les colonnes
                for i in range (3): 
                    if self.tab[i][0]==j and self.tab[i][j]==j and self.tab[i][2]==j or self.tab[0][i]==j and self.tab[1][i]==j and self.tab[2][i]==j:
                        self.fin = j
                #on verifie les diagonales
                if self.tab[0][0] == j and self.tab [1][1] == j and self.tab[2][2] ==j or self.tab[0][2] ==j and self.tab[1][1] ==j and self.tab[2][0] == j:
                    self.fin = j

