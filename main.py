import pygame
import button
from game import Game
from random import randint

pygame.init()

pygame.display.set_caption("tic tac toe","assets/icon.jpg")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load("assets/background.jpg")

#load button images
Jouer_img=pygame.image.load("assets/button/Jouer.jpg").convert_alpha()
Deux_joueurs_img=pygame.image.load("assets/button/2 joueurs.jpg").convert_alpha()
Debutant_img=pygame.image.load("assets/button/Debutant.jpg").convert_alpha()
Difficile_img=pygame.image.load("assets/button/Difficile.jpg").convert_alpha()
IA_img=pygame.image.load("assets/button/IA.jpg").convert_alpha()
Intermediaire_img=pygame.image.load("assets/button/Intermédiaire.jpg").convert_alpha()
Rejouer_img=pygame.image.load("assets/button/Rejouer.jpg").convert_alpha()
Retour_img=pygame.image.load("assets/button/Retour.jpg").convert_alpha()
Quitter_img=pygame.image.load("assets/button/Quitter.jpg").convert_alpha()

#create button instances
Jouer_button = button.Button(920, 300, Jouer_img, 1)
Deux_joueurs_button = button.Button(920, 400, Deux_joueurs_img, 1)
Debutant_button = button.Button(920, 300, Debutant_img, 1)
Difficile_button = button.Button(920, 600, Difficile_img, 1)
IA_button = button.Button(920, 500, IA_img, 1)
Intermediaire_button = button.Button(920, 400, Intermediaire_img, 1)
Rejouer_button = button.Button(920, 300, Rejouer_img, 1)
Retour_button = button.Button(920, 200, Retour_img, 1)
Quitter_button = button.Button(920, 400, Quitter_img, 1)



menu_state="main"
running = True
game = None








while running:
    screen.blit(background, (0,0)) #affiche le fond
    
    
    if menu_state=="main":
        if Jouer_button.draw(screen):
            menu_state="jouer"
        if Quitter_button.draw(screen):
            running= False
            pygame.quit()
    if menu_state=="jouer":
        if Deux_joueurs_button.draw(screen):
            menu_state = "2j"
            game = Game()
        if IA_button.draw(screen):
            menu_state="IA"
        if Retour_button.draw(screen):
            menu_state="main"
    if menu_state=="IA":
        if Debutant_button.draw(screen):
            menu_state = "IA_deb"
            ia_player = randint(1,2)
            game = Game()
        if Intermediaire_button.draw(screen):
            menu_state = "IA_int"
            ia_player = randint(1,2)
            game = Game()
        if Difficile_button.draw(screen):
            menu_state = "IA_diff"
            ia_player = randint(1,2)
            game = Game()
        if Retour_button.draw(screen):
            menu_state="jouer"



    if menu_state == "IA_deb":
        game.play(screen)
        if game.part.player == ia_player:
            game.part.turn_ia_debutant()
    


    if menu_state == "IA_int":
        game.play(screen)
        if game.part.player == ia_player:
            game.part.turn_ia_int(ia_player)


           
    if menu_state == "IA_diff":
        game.play(screen)
        if game.part.player == ia_player:
            game.part.turn_ia_diff(ia_player)
        


    if menu_state == "2j":
       game.play(screen) 





    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                menu_state="main"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if mouse_x >= 250 + 190*j and mouse_x < 250 + 190*(j+1) and mouse_y >= 75 + 200*i and mouse_y < 75 + 200*(i+1) :
                        if menu_state == "2j":
                            game.part.turn(i,j)
                        if (menu_state == "IA_diff" or menu_state == "IA_int" or menu_state== "IA_deb") and game.part.player != ia_player:
                            game.part.turn(i,j)



                        
    pygame.display.flip()  
