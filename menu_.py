#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#importation de la librairie pygame et initialistaion
import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((500,700))

#création de l'objet curseur
class curseur:
        pos_x = 50
        pos_y = 50
        image = pygame.image.load("maps/pic/curseur.jpg").convert()


#création de l'objet ligne
class ligne:
        pos_x = 50
        pos_y = 50
        image = pygame.image.load("maps/pic/ligne.png").convert()

#initialisation de la boucle infinie du jeu


def menu_():
        global fenetre
        global ligne
        global curseur

        #Ouverture de la fenêtre Pygame
        largeur = 500
        hauteur = 700
        fenetre = pygame.display.set_mode((largeur,hauteur))

        options = pygame.image.load("maps/pic/options.png").convert()
        #Chargement et collage du fond
        fond = pygame.image.load("maps/pic/black.png").convert()

        #chargement et collage des images
        titre = pygame.image.load("maps/pic/titre.png").convert_alpha()
        start = pygame.image.load("maps/pic/jouer.png").convert()
        son = pygame.image.load("maps/pic/son.png").convert()
        echap = pygame.image.load("maps/pic/echap.png").convert()
        cote = pygame.image.load("maps/pic/cote.png").convert()
        cote_2 = pygame.image.load("maps/pic/cote_2.png").convert()
        fleche = pygame.image.load("maps/pic/fleche.png").convert_alpha()
        fond_ = pygame.image.load("maps/pic/map.png").convert()

        ligne_1 = ligne()
        ligne_2 = ligne()

        curseur_1 = curseur()
        curseur_2 = curseur()

        selection = 0
        option = 0
        quitter = 0
        pos_l = 50
        pos_h = 200
        pygame.mixer.music.load("son/musique.wav")  # Serieusement (-_-)
        pygame.mixer.music.play()

        while 1==1: 
                
                if quitter == 1:
                        break
                menu = 1
        #initialisation de la boucle du menu
                while menu == 1:
                        
                        if option == 1:
                                while option == 1:
                                        if quitter == 1:
                                                break
        #on affiche ensuite le premier curseur et on actualise la fenetre
                                        fenetre.blit(fond, (0,0))
                                        curseur_1.pos_x = int((pygame.mixer.music.get_volume()*425))
                                        curseur_1.pos_y = 180
                                        fenetre.blit(son, (30,100))
                                        fenetre.blit(echap, (50,450))
                                        ligne_1.pos_y = 180
                                        fenetre.blit(ligne_1.image, (ligne_1.pos_x, ligne_1.pos_y))
                                        ligne_2.pos_y = 300
                                        fenetre.blit(ligne_2.image, (ligne_2.pos_x, ligne_2.pos_y))
                                        fenetre.blit(curseur_1.image, (curseur_1.pos_x, curseur_1.pos_y))
                                        pygame.display.flip()
        #initialisation de la boucle de détection des entrées (2)
                                        while selection == 1:
                                                for event in pygame.event.get():
        #on détecte si l'utilisateur bouge la souris tout en cliquant
                                                        if event.type == MOUSEMOTION:
                                                                nvol = float(event.pos[0])-25
                                                                if event.pos[0] in range(50,450):
                                                                        curseur_1.pos_x = event.pos[0]-25
                                                                        pygame.mixer.music.set_volume((nvol/425))
                                                                        fenetre.blit(fond, (0,0))
                                                                        fenetre.blit(ligne_1.image, (ligne_1.pos_x, ligne_1.pos_y))
                                                                        fenetre.blit(ligne_2.image, (ligne_2.pos_x, ligne_2.pos_y))
                                                                        fenetre.blit(echap, (50,450))
                                                                        fenetre.blit(cote_2, (0,0))
                                                                        fenetre.blit(son, (30,100))
                                                                        fenetre.blit(cote, (450,0))
                                                                        fenetre.blit(curseur_1.image, (curseur_1.pos_x, curseur_1.pos_y))
                                                                        pygame.display.flip()
                                                        if event.type == MOUSEBUTTONUP:
                                                                if event.button == 1:
                                                                        selection = 0
                                                pygame.display.flip()
                                        print("volume :",pygame.mixer.music.get_volume())
                                        for event in pygame.event.get():

                                                if event.type == QUIT:
                                                        quitter = 1
                                                        break

        # on donne au curseur 1 la fonction du volume, or le volume va de 0 a 1 en passant par des decimaux pour python
        #il a donc pour coordonnées la valeur entière du volume * 400 car la fenetre fait 500 pixels
        #auxquels on ajoute 25 car le curseur fait 50 pixels de haut et on veut que le milieu du curseur
        #arrive au milieu de la ligne

        #association de la touche echap a la sortie des options
                                                if event.type == KEYDOWN:
                                                        if event.key == K_ESCAPE:                                                        
                                                                option = 0
                                                        if event.key == K_LEFT:
                                                        	pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()-0.001)
                                                        	pygame.time.wait(10)

                                                        if event.key == K_RIGHT:
                                                        	pygame.mixer.music.set_volume(pygame.mixer.music.get_volume()+0.001)
                                                        	pygame.time.wait(10)

        #on détecte si l'utilisateur clique
                                                if event.type == MOUSEBUTTONDOWN:
                                                        
                                                        if event.button == 1 and event.pos[0] in  range (50,450):
        #on regarde si l'utilisateur clique sur la hitbox du curseur
                                                                if event.pos[0] in range (curseur_1.pos_x, curseur.pos_x+50) and event.pos[1] in range (curseur_1.pos_y, curseur.pos_y+50) or event.pos[1] in range(ligne_1.pos_x+15,ligne_1.pos_y+35):
                                                                        
                                                                        curseur_1.pos_x = event.pos[0]-25
                                                                        
                                                                        nvol = float(event.pos[0])-25
                                                                        
                                                                        pygame.mixer.music.set_volume((nvol/425))
        #on réaffiche le curseur en fonction d'où a cliqué l'utilisateur
                                                                        fenetre.blit(fond, (0,0))
                                                                        fenetre.blit(ligne_1.image, (ligne_1.pos_x,ligne_1.pos_y))                                                              
                                                                        fenetre.blit(son, (30,100))
                                                                        fenetre.blit(curseur_1.image, (curseur_1.pos_x, curseur_1.pos_y))
                                                                        pygame.display.flip()
                                                                        
                                                                        selection = 1

                        if quitter == 1:
                                break
        #affichage du menu et rafraîchissement de la page

                        fenetre.blit(fond_,(0,0))
                        fenetre.blit(titre, (100,0))
                        fenetre.blit(start, (100,200))
                        fenetre.blit(options, (100,300))
                        fenetre.blit(fleche, (pos_l,pos_h))
                        pygame.display.flip()

        #boucle de lecture des entrees
                        for event in pygame.event.get():
                                if event.type == QUIT:
                                        quitter = 1
                                        menu = 0
                                        break
                                if event.type == KEYDOWN:
                                #ici on detecte simplement si l'utilisateur veut quitter
                                        if event.key == K_ESCAPE:
                                                quitter = 1
                                                break

                                #à ce niveau on déplace la petite fleche blanche entre jouer et options à l'aide des touches
                                #et s'il appuie sur entree, on effectue une action en fonction de la position de la fleche
                                        if event.key == K_DOWN or K_UP or K_RETURN:
                                                if event.key == K_DOWN:
                                                        pos_h = 300

                                                if event.key == K_UP:
                                                        pos_h = 200

                                                if event.key == K_RETURN and pos_h == 200:
                                                        jouer = 1
                                                        menu = 0
                                                        quitter = 1
                                                        break

                                                if event.key == K_RETURN and pos_h == 300:
                                                        option = 1
                        
                                if event.type == MOUSEBUTTONDOWN:
                                        if event.button == 1:

        #détection de l'entrée en jeu,
        #on détecte si l'utilisateur clique sur le bouton jouer
                                                if event.pos[0] in range(100,400) and event.pos[1] in range(200,250):
                                                        jouer = 1
                                                        menu = 0
                                                        quitter = 1
                                                        break
        #détection de l'entrée dans les options
        #on détecte si l'utilisateur appuie sur le bouton options
                                                if event.pos[0] in range(100,400) and event.pos[1] in range(300,350):
        #et on l'oriente vers le menu des options
                                                        option = 1

        pygame.mixer.music.stop()
