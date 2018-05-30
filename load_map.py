#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fonction permettant d'afficher une carte à partir d'un fichier textuel

import pygame
from pygame.locals import*

pygame.init()
hitbox = []
tiles = []
tiles_l2 = []


#setup du mode video (obligatoire si on veut pouvoir charger des images)
fenetre = pygame.display.set_mode((960,640))


#création de la liste tiles(elements non collisionables(en général le sol))
tiles.append(pygame.image.load("maps/pic/herb.png").convert())#0
tiles.append(pygame.image.load("maps/pic/flowr.png").convert())#1
tiles.append(pygame.image.load("maps/pic/grass.png").convert())#2
tiles.append(pygame.image.load("maps/pic/cobbl.png").convert())#3

#création de la liste tiles_l2 correspondant aux éléments collisionables (maisons, marché, etc)
tiles_l2.append(pygame.image.load("maps/pic/vide.png").convert_alpha())#0
tiles_l2.append(pygame.image.load("maps/pic/hous_1.png").convert_alpha())#1
tiles_l2.append(pygame.image.load("maps/pic/hous_2.png").convert_alpha())#2
tiles_l2.append(pygame.image.load("maps/pic/market.png").convert_alpha())#3

def load_map(file, tiles, fenetre, show_hitboxes=False):
    global tiles_l2 #liste des elements de collision
    global hitbox #liste correspondant aux rectangles des hitbox des elements de collison

    if tiles == tiles_l2: # si on utilise la liste correspondant aux elements "collisionablisé
#on met alors la variable tile_set a 1 ou 2 pour indiquer si on doit prendre en compte les collisisions ou non
        tile_set = 2
    else:
        tile_set = 1

    y = 0
    x = 0
    
    for i in file:
        # Que fait buff exactement ? Ah nan c'est bon j'ai compris c'est pour savoir quel tile on charge
        if i != " " and i!= "\n":
            try:
                buff = int(i)
            except:
                print(i)
        else:
            buff = 0
        if i == "\n":
            y = y + 1
            x = 0
#ici on reset simplement la position des objets de type maison
#pour ne pas qu'ils sortent de l'écran

#c'est ça on utilise en fait la variable solve_x et solve_y pour corriger le fait que les maisons ayant un
#une image plus grande que 64*64 puissent sortir de l'écran - Ok :)
            
        if x > 7 and pygame.Surface.get_width(tiles[buff]) > 64:
            solve_x = -1
        else:
            solve_x = 0
        if y > 5 and pygame.Surface.get_height(tiles[buff]) > 64:
            solve_y = -1
        else:
            solve_y = 0
        if buff < len(tiles):
            fenetre.blit(tiles[buff],((x+solve_x)*64,(y+solve_y)*64))
            pygame.display.flip()
        if tile_set == 2 and buff in range(1,10):
            hitbox.append(pygame.Rect((x+solve_x)*64,(y+solve_y)*64,pygame.Surface.get_width(tiles[buff]), pygame.Surface.get_height(tiles[buff])))

        if i != " " and i != "\n":
            x = x + 1

    #on peut enlever le "#" de commentaire en dessous pour afficher les hitbox
    #des maisons et shop.  ATTENTION c'est moche
    if show_hitboxes:        
        for i in range(0,len(hitbox)):
            pygame.draw.rect(fenetre, Color(255,0,0,255), hitbox[i])
