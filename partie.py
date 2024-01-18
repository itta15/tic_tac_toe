import pygame
from case import Case
from random import choice

class Partie(pygame.sprite.Sprite):

    def __init__ (self):
        super().__init__()
        self.tab = [[0 for _ in range(3)] for _ in range (3)]
        self.all_case_comp = pygame.sprite.Group()
        self.fin = None       
        self.player = 1
        self.image = pygame.image.load("assets/tab.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 240
        self.rect.y = 60

        
    #turn aura d'autre argument pour la case designe
    def turn (self,i,j):
        if (self.fin == None and self.tab[i][j]==0):
            self.tab[i][j] = self.player
            self.all_case_comp.add(Case(self.player,i,j))
            self.player = 1 if self.player ==2 else 2 #permet de changer de joueur apres avoir clique
            self.est_fini()



    # met a jour à la valeur de self.fin au joueur gagnat si il existe, et a 0 en cas d egalite
    def est_fini (self):
        for j in range(1,3): #suivant si c'est le joueur 1 ou le 2 qui a gagne
            #on verifie les lignes et les colonnes
            for i in range (3): 
                if self.tab[i][0]==j and self.tab[i][1]==j and self.tab[i][2]==j or self.tab[0][i]==j and self.tab[1][i]==j and self.tab[2][i]==j:
                    self.fin = j
            #on verifie les diagonales
            if self.tab[0][0] == j and self.tab [1][1] == j and self.tab[2][2] ==j or self.tab[0][2] ==j and self.tab[1][1] ==j and self.tab[2][0] == j:
                self.fin = j

        #on verifie que le tableau est pas plein
        if self.fin == None :            
            est_plein = True
            for j in range(3):
                for i in range(3):
                    if self.tab[i][j]==0 :
                        est_plein=False
            if est_plein :
                self.fin = 0


#prend en argument si l'ia est j1 ou j2
    def turn_ia_int (self, ia_play) :
        if ia_play == 1:
            l=[1,2]
        else:
            l=[2,1]
        if self.fin == None :
            for p in l:
                for i in range(3):
                    #on verifie les lignes
                    if self.tab[i][0]== p and self.tab[i][1] == p and self.tab[i][2]==0 :
                        self.turn (i,2)
                        return
                    if self.tab[i][0]== p and self.tab[i][2] == p and self.tab[i][1]==0 :
                        self.turn (i,1)
                        return
                    if self.tab[i][2]== p and self.tab[i][1] == p and self.tab[i][0]==0 :
                        self.turn (i,0)
                        return
                    
                    #on verifie les colonnes
                    if self.tab[0][i]==p and self.tab[1][i]==p and self.tab[2][i]==0 :
                        self.turn (2,i)
                        return
                    if self.tab[0][i]==p and self.tab[2][i]==p and self.tab[1][i]==0 :
                        self.turn (1,i)
                        return
                    if self.tab[2][i]==p and self.tab[1][i]==p and self.tab[0][i]==0 :
                        self.turn (0,i)
                        return

                #on verifie les diagonales
                if self.tab[0][0]==p and self.tab[1][1] == p and self.tab[2][2]==0 :
                    self.turn (2,2)
                    return
                if self.tab[2][2] == p and self.tab[1][1] == p and self.tab[0][0]==0 :
                    self.turn (0,0)
                    return
                if self.tab[0][0] == p and self.tab[2][2] == p and self.tab[1][1]==0 :
                    self.turn (1,1)
                    return

                if self.tab[0][2]==p and self.tab[1][1]==p and self.tab[2][0]==0 :
                    self.turn (2,0)
                    return
                if self.tab[2][0]==p and self.tab[1][1]==p and self.tab[0][2]==0 :
                    self.turn (0,2)
                    return
                if self.tab[0][2]==p and self.tab[2][0]==p and self.tab[1][1]==0 :
                    self.turn (1,1)
                    return
            self.turn_ia_debutant ()
            
            
            
    def turn_ia_debutant (self) :
        if self.fin == None:
            #création de la liste des cases vides
            est_vide=[]
            for i in range(3) :
                for j in range(3) :
                    if self.tab[i][j]==0 :
                        est_vide.append((i,j))
            #on sélectionne au hasard une case vide où jouer
            (i,j) = choice(est_vide)
            self.turn(i,j)


    def turn_ia_diff (self,ia_play):
        if self.fin == None:
            _,(i,j) = self.minimax(ia_play)
            self.turn (i,j)





    def jouer_coup(self, i, j):
        self.tab[i][j] = self.player
        self.player = 1 if self.player==2 else 2
        

    def dejouer_coup(self, i, j):
        self.tab[i][j] = 0
        self.player = 1 if self.player==2 else 2
        if self.fin != None: 
            self.fin = None




    #renvoie si il existe une solution optimal ainsi que le meilleurs coups a jouer si joueur = self.player (None sinon)
    def minimax(self, joueur):
        if self.fin != None:
            return (0,None)


    #on regarde tous les cas et on prend le pire
        if self.player != joueur:
            meilleure_evaluation = 1 #c'est le maximum
            for i in range(3):
                for j in range(3):
                    if self.tab[i][j] == 0:
                        self.jouer_coup(i, j) 
                        self.est_fini()
                        # si l'autre joueur joue (i, j), on perd donc on a pas jouer le bon coup 
                        if self.fin != joueur and self.fin != None and self.fin != 0:
                            self.dejouer_coup(i, j) 
                            return (-1,(None))
                        
                        else:
                            evaluation,_ = self.minimax(joueur)
                            meilleure_evaluation = min(evaluation, meilleure_evaluation)
                            self.dejouer_coup(i, j)
            return (meilleure_evaluation,None)
        
        #on cherche le bon coup
        else:
            meilleure_evaluation = -1 #c'est le minimum
            meilleur_coup = (0,0)
            for i in range(3):
                for j in range(3):
                    if self.tab[i][j] == 0:
                        self.jouer_coup(i, j) 
                        self.est_fini()

                        #si on gagne la partie en jouant (i,j)
                        if self.fin == joueur:
                            self.dejouer_coup(i, j) 
                            return (1,(i,j))
                        else:
                            evaluation,_ = self.minimax(joueur) 
                            if evaluation > meilleure_evaluation:
                                meilleure_evaluation = evaluation
                                meilleur_coup = (i,j)
                            self.dejouer_coup(i, j) 
            return (meilleure_evaluation, meilleur_coup)



