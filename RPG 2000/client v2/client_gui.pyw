import pygame
import threading
import socket
import json
import time

from pygame.locals import *
pygame.init()

pseudo = b"Pseudo2"
joueurs = []

execute = True

#Fonction bien utilse faite par moi-meme :=)
def gsub(mot,debut,fin):
    count = 0
    valeur_return = ""
    if debut < 1:
        for lettre in mot:
            count += 1
            if (count <= fin):
                valeur_return = valeur_return+lettre
    else:
        if (debut<=fin):
            for lettre in mot:
                count += 1
                if (count >= debut):
                    if (count <= (fin+debut)-1):
                        valeur_return = valeur_return+lettre
    return valeur_return

def find_table_index(table,value):
    count = -1
    value_return = False
    for i in table:
        count += 1
        if(i==value):
            value_return = count
    return value_return

def detect_charactere(string,cara):
    count = -1
    value_return = False
    for i in string:
        count += 1
        if(i==cara):
            value_return = count
            break
    return value_return


# Thread pour recevoir les informations du serveur:
class Receive_Server_Part(threading.Thread):
    def run(self):
        global joueurs
        while execute:
            msg_recu = connexion_avec_serveur.recv(1024)
            msg_recu = msg_recu.decode()
            if(msg_recu == ""):
                break
            else:
                detect = detect_charactere(msg_recu,"]")
                json_str = gsub(msg_recu,0,detect+1)
                cache = json.loads(json_str)
                if((len(cache)-2)%3 == 1):
                    joueurs = json.loads(json_str)
                else:
                    print("Erreur de réception de la position des joueurs")



#PARTIE CONNEXION
                
try:
    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect(("relaxrp.fr", 57895))
    print("Connexion au serveur réalisé avec succès !")
    #Demarrage du thread pour recevoir en permanence les informations du serveur.
    Receive_Server_Part().start()
    #Envoi au serveur de nous ajouter a la table joueurs
    connexion_avec_serveur.send(b"Register: "+pseudo)
    
except socket.error as err:
    print("Impossible de se connecter au serveur !")





# Generation des joueurs en fonction de la table joueurs
def SetPosPly():
    global joueurs
    count = 0
    try:
        for value in joueurs:
            count += 1
            if(count%3 == 1):
                x = joueurs[count]
                y = joueurs[count+1]
                nouveau_joueur = pygame.image.load("images/characters_nude.png").convert_alpha()
                fenetre.blit(nouveau_joueur, (x, y))
    except:
        print("Je bliterais une autre fois :)")

# Thread pour executer en permanance un raffraichissement des joueurs et de l'écran
class AlwaysFlipScreen(threading.Thread):
    def run(self):
        while execute:
            fenetre.blit(fond, (0,0))
            SetPosPly()
            pygame.display.flip()


fenetre = pygame.display.set_mode((640, 480))


#Importation des images
fond = pygame.image.load("images/background.jpg").convert()
ply_picture = pygame.image.load("images/characters_nude.png").convert_alpha()


fenetre.blit(fond, (0,0))

# Demerrage du thread pour le raffraichissement de l'ecran
AlwaysFlipScreen().start()



pygame.key.set_repeat(1, 50)

while execute:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if(event.type == KEYDOWN):
            if event.key == 275:
                connexion_avec_serveur.send(b"moove "+pseudo+b": moove_right")
            if event.key == 276:
                connexion_avec_serveur.send(b"moove "+pseudo+b": moove_left")
            if event.key == 274:
                connexion_avec_serveur.send(b"moove "+pseudo+b": moove_bot")
            if event.key == 273:
                connexion_avec_serveur.send(b"moove "+pseudo+b": moove_top")
        if(event.type == QUIT):
            connexion_avec_serveur.send(b"disconnect "+pseudo)
            execute = False
