import pygame

class Case (pygame.sprite.Sprite):
    
    def __init__(self,joueur,i,j):
        super().__init__()
        self.state = 0
        self.image = pygame.image.load("assets/cross.jpg") if joueur==1 else pygame.image.load("assets/circle.jpg")
        self.rect = self.image.get_rect()
        self.rect.x= 25 + 240 + 200*j #pour l'afficher dans la bonne case
        self.rect.y= 25 + 60 + 200*i 
        