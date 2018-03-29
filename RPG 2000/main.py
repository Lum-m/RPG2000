## Demo de RPG multijoueur pour un projet d'ISN
#sapristi saucisse
import pygame
from pygame.locals import*

pygame.init()

fenetre = pygame.display.set_mode((960,640))

tiles = []
tiles[:]=[]
tiles_l2 = []
tiles_l2[:] =[]

quitter = 0
px = 0
py = 0
direction = 'haut'


tiles.append(pygame.image.load("maps/pic/herb.png").convert())#0
tiles.append(pygame.image.load("maps/pic/flowr.png").convert())#1
tiles.append(pygame.image.load("maps/pic/grass.png").convert())#2
tiles.append(pygame.image.load("maps/pic/cobbl.png").convert())#3

tiles_l2.append(pygame.image.load("maps/pic/vide.png").convert_alpha())#0
tiles_l2.append(pygame.image.load("maps/pic/hous_1.png").convert_alpha())#1
tiles_l2.append(pygame.image.load("maps/pic/hous_2.png").convert_alpha())#2
tiles_l2.append(pygame.image.load("maps/pic/market.png").convert_alpha())#3

apparence = []
apparence[:] = []

apparence.append(" ")
apparence.append(pygame.image.load("maps/pic/gauche.png"))
apparence.append(pygame.image.load("maps/pic/gauche2.png"))
apparence.append(pygame.image.load("maps/pic/haut.png"))
apparence.append(pygame.image.load("maps/pic/haut2.png"))
apparence.append(pygame.image.load("maps/pic/droite.png"))
apparence.append(pygame.image.load("maps/pic/droite2.png"))
apparence.append(pygame.image.load("maps/pic/bas.png"))
apparence.append(pygame.image.load("maps/pic/bas2.png"))

pygame.key.set_repeat(10,200)

from load_map import*
from shop import*
from aff_perso import*

with open("maps/map_1.txt","r") as fichier:
    map_1 = fichier.read()

with open("maps/map_l2_1.txt","r") as fichier:
    map_1_l2 = fichier.read()


load_map(map_1 , tiles, fenetre)
load_map(map_1_l2, tiles_l2, fenetre)
pygame.image.save(fenetre, "map1.png")
fenetre.blit(fond, (0,0))
map1 = pygame.image.load("map1.png").convert()
map1_l2 = pygame.image.load("map1_l2.png").convert_alpha()
aff_perso(fenetre, map1, apparence, px, py)

perso = pygame.Rect(px, py, 32, 32)
while quitter == 0:

    for event in pygame.event.get():
            if event.type == KEYDOWN:
                if (event.key == K_UP or event.key == K_DOWN or event.key == K_LEFT or event.key == K_RIGHT):
                        fenetre.blit(map1,(0,0))            
                if event.key == K_UP and py > 0 and perso.collidelist(hitbox) != 0:
                        py -= 8
                        direction = 'haut'
                        aff_perso(fenetre, map1, apparence, px, py)
                if event.key == K_DOWN and py < 608  and perso.collidelist(hitbox) != 0:
                        py += 8
                        direction = 'bas'
                        aff_perso(fenetre, map1, apparence, px, py, direction)
                if event.key == K_RIGHT and px < 928  and perso.collidelist(hitbox) != 0:
                        px += 8
                        direction = 'dte'
                        aff_perso(fenetre, map1, apparence, px, py, direction)
                if event.key == K_LEFT and px > 0  and perso.collidelist(hitbox) != 0:
                        px -= 8
                        direction = 'gche'
                        aff_perso(fenetre, map1, apparence, px, py, direction)
            elif perso.collidelist(hitbox) == 0:
                    aff_perso(fenetre, map1, apparence, px, py, direction)
            perso = pygame.Rect(px, py, 32, 32)
            pygame.display.flip()
            if event.type == QUIT:
                    quitter = 1

