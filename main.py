import pygame
import button
from game import Game

pygame.init()

pygame.display.set_caption("tic tac toe","assets/icon.jpg")
screen = pygame.display.set_mode((1080,720))

background = pygame.image.load("assets/background.jpg")






#load button images
Jouer_img=pygame.image.load("button/Jouer.jpg").convert_alpha()
Deux_joueurs_img=pygame.image.load("button/2 joueurs.jpg").convert_alpha()
Debutant_img=pygame.image.load("button/Debutant.jpg").convert_alpha()
Difficile_img=pygame.image.load("button/Difficile.jpg").convert_alpha()
IA_img=pygame.image.load("button/IA.jpg").convert_alpha()
Intermediaire_img=pygame.image.load("button/Intermédiaire.jpg").convert_alpha()
Rejouer_img=pygame.image.load("button/Rejouer.jpg").convert_alpha()
Retour_img=pygame.image.load("button/Retour.jpg").convert_alpha()
Quitter_img=pygame.image.load("button/Quitter.jpg").convert_alpha()

#create button instances
Jouer_button = button.Button(920, 300, Jouer_img, 1)
Deux_joueurs_button = button.Button(920, 400, Deux_joueurs_img, 1)
Debutant_button = button.Button(920, 300, Debutant_img, 1)
Difficile_button = button.Button(920, 500, Difficile_img, 1)
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
            pass
        if Intermediaire_button.draw(screen):
            pass
        if Difficile_button.draw(screen):
            menu_state = "IA_dur"
            game = Game()
        if Retour_button.draw(screen):
            menu_state="jouer"

           
    if menu_state == "IA_dur":
        game.play(screen)
        if game.part.player == 2:
            game.part.turn_ia_diff()
        


    if menu_state == "2j":
       game.play(screen) 





    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            # if event.key == pygame.K_1: #touche 1 qui sera change par un clic plus tard
            #    game.part.turn (0,0)
            # if event.key == pygame.K_2: 
            #    game.part.turn (1,0)
            # if event.key == pygame.K_3: 
            #    game.part.turn (2,0)
            # if event.key == pygame.K_4: 
            #    game.part.turn (0,1)
            # if event.key == pygame.K_5: 
            #    game.part.turn (1,1)
            # if event.key == pygame.K_6: 
            #    game.part.turn (2,1)
            # if event.key == pygame.K_7: 
            #    game.part.turn (0,2)
            # if event.key == pygame.K_8:
            #    game.part.turn (1,2)
            # if event.key == pygame.K_9:
            #    game.part.turn (2,2)
            if event.key == pygame.K_r:
                menu = True
                menu_state="main"
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if mouse_x >= 250 + 190*j and mouse_x < 250 + 190*(j+1) and mouse_y >= 75 + 200*i and mouse_y < 75 + 200*(i+1) :
                        if menu_state == "2j":
                            game.part.turn(i,j)
                        if menu_state == "IA_dur" and game.part.player == 1:
                            game.part.turn(i,j)



                        
    pygame.display.flip()  
