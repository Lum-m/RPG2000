#!/usr/bin/env python
# -*- coding: utf-8 -*-
## Demo de RPG multijoueur pour un projet d'ISN
import pygame
from pygame.locals import*
import load_map as load
from shop import*
from fonctions import*
import threading
import socket
import json
import random
from menu_ import menu_

#import txt


pygame.init()

pseudo = b"titidhdh"
Hote = "relaxrp.fr"
Port = 57895


#pygame.time.Clock().tick(1)

nouveau_joueur = pygame.image.load("maps/pic/character0.png").convert_alpha()
execute = True
shop_ = 0
joueurs = []
position_joueurs = []
joueurs_avt = []
direction = []
son = []

menu_()

pygame.mixer.music.load("son/Root.wav")
pygame.mixer.music.play()

for i in range(1,4):
    son.append(pygame.mixer.Sound("son/grass"+str(i)+".wav"))
son.append(pygame.mixer.Sound("son/shop.wav"))
# Thread pour recevoir les informations du serveur et calcul des positions:
class Receive_Server_Part(threading.Thread):
    def run(self):
        global joueurs
        global joueurs_avt
        global direction
        while execute:
            msg_recu = connexion_avec_serveur.recv(1024)
            msg_recu = msg_recu.decode()
            if(msg_recu == ""):
                break
            else:
                detect = detect_charactere(msg_recu,"]")
                json_str = gsub(msg_recu,0,detect+1)
                try:
                    cache = json.loads(json_str)
                except:
                    print("Erreur de conversion en JSON, cela arrive souvent quand on déplace trop longtemps la fenetre.")
                if((len(cache)-2)%3 == 1):
                    joueurs_avt = joueurs
                    joueurs = cache
                    if int(len(joueurs)/3) > len(direction):
                        direction.append(0)
                    if int(len(joueurs)/3) < len(direction):
                        del direction[-1]
                    if joueurs_avt != [] and len(joueurs)==len(joueurs_avt):
                        for i in range(0,int(len(joueurs)/3)):
                            if joueurs[i*3+1] < joueurs_avt[i*3+1]:
                                if direction[i] == 4:
                                    direction[i] = 5
                                else:
                                    direction[i] = 4
                            elif joueurs[i*3+1] > joueurs_avt[i*3+1]:
                                if direction[i] == 2:
                                    direction[i] = 3
                                else:
                                    direction[i] = 2

                            if joueurs[i*3+2] < joueurs_avt[i*3+2]:
                                if direction[i] == 6:
                                    direction[i] = 7
                                else:
                                    direction[i] = 6
                            elif joueurs[i*3+2] > joueurs_avt[i*3+2]:
                                if direction[i] == 0:
                                    direction[i] = 1
                                else:
                                    direction[i] = 0
                else:
                    print("Erreur de reception de la position des joueurs")

        

#PARTIE CONNEXION
                
try:
    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect((Hote, Port))
    print("Connexion au serveur réalisée avec succès !")
    #Demarrage du thread pour recevoir en permanence les informations du serveur.
    Receive_Server_Part().start()
    #Envoi au serveur de nous ajouter a la table joueurs
    connexion_avec_serveur.send(b"Register: "+pseudo)
    
except socket.error as err:
    print("Impossible de se connecter au serveur !")


# Generation des joueurs en fonction de la table joueurs


def SetPosPly():
    global joueurs
    global nouveau_joueur
    global shop_
    
    nbr_joueurs = int(len(joueurs)/3)
    if shop_ == 1:
        pygame.mixer.music.pause()
    for i in range(0,int(nbr_joueurs)):
        try:
            nouveau_joueur = pygame.image.load("maps/pic/character"+str(direction[i])+".png").convert_alpha()
            x = joueurs[i*3+1]
            y = joueurs[i*3+2] 
            fenetre.blit(nouveau_joueur, (x, y))
        except:
            print("echec de blitage")
            print("x=",x,"y=",y)
            print("nj=",nouveau_joueur)
                
class AlwaysFlipScreen(threading.Thread):
    def run(self):
        global joueurs
        global execute
        global shop_
        while execute and shop_ == 0:
            fenetre.blit(map1, (0,0))
            #print(joueurs)
            SetPosPly()
            pygame.display.flip()

fenetre = pygame.display.set_mode((960,640))

pygame.key.set_repeat(1,100)

with open("maps/map_0-0_l1.txt","r") as fichier:
    map_1 = fichier.read()

with open("maps/map_0-0_l2.txt","r") as fichier:
    map_1_l2 = fichier.read()

load.load_map(map_1 , load.tiles, fenetre)
load.load_map(map_1_l2, load.tiles_l2, fenetre)
pygame.image.save(fenetre, "map1.png")
#fenetre.blit(fond, (0,0))
map1 = pygame.image.load("map1.png").convert()

perso = pygame.Rect(0, 0, 32, 32)
# Demerrage du thread pour le raffraichissement de l'ecran
AlwaysFlipScreen().start()


while execute:
    for event in pygame.event.get():
            if event.type == KEYDOWN:
                rand = random.randint(0,2)

                if event.key == K_UP or event.key == K_DOWN or event.key == K_RIGHT or event.key == K_LEFT:
                    son[rand].play()
                if event.key == K_UP:
                        connexion_avec_serveur.send(b"moove "+pseudo+b": moove_top")
                if event.key == K_DOWN:
                        connexion_avec_serveur.send(b"moove "+pseudo+b": moove_bot")
                if event.key == K_RIGHT:
                        connexion_avec_serveur.send(b"moove "+pseudo+b": moove_right")
                if event.key == K_LEFT:
                        connexion_avec_serveur.send(b"moove "+pseudo+b": moove_left")

                if event.key == K_c:
                        shop_ = 1
                        pygame.mixer.music.pause()
                        son[3].play()
                        shop()
                        son[3].stop()
                        shop_ = 0
                        AlwaysFlipScreen().start()
                        pygame.mixer.music.unpause()
            if(event.type == QUIT):
                connexion_avec_serveur.send(b"disconnect "+pseudo)
                execute = False
