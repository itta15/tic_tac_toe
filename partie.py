import numpy as np
import pygame

class Partie(pygame.sprite.Sprite):

    def __init__ (self):
        super().__init__()
        self.tab = [[0 for _ in range(3)] for _ in range (3)]
        self.fin = False
        self.turn = 1
        self.fond = pygame.image.load("assets/tab.jpg")
        self.rect_fond = self.fond.get_rect()
        self.rect_fond.x = (1080 - 600)/2
        self.rect_fond.y = (720-600)/2



