#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import socket
import select
import time
import threading


#Fonction bien utile

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



#Demarrage du réseau
connexion_princ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_princ.bind(('', 57895))
connexion_princ.listen(5)

client_connectes = []
joueurs = []

#On envoie toutes les 0.1 secondes la position de tous les joueurs (thread)
class send_data(threading.Thread):
    def run(self):
        global joueurs
        global client_connectes
        while True:
            for client in client_connectes:
                client.send(json.dumps(joueurs))
            time.sleep(0.1)
send_data().start()


while True:

    #On attend 0.001 secondes pour voir si un joueur veut se connecter puis on accepte sa connexion et on l'ajoute dans la table client_connectes
    nouvelle_connexion,wlist,xlist = select.select([connexion_princ],[],[],0.001)
    for connexion in nouvelle_connexion:
        connexion_client, info_connexion = connexion.accept()
        client_connectes.append(connexion_client)
        print("Connexion d'un joueur")


    #On attend 0.001 secondes pour voir si un joueur veut nous envoyer des informations
    client_a_lire = []
    
    try:
        client_a_lire, wlist, xlist = select.select(client_connectes,[],[],0.001)
    except select.error:
        pass
    else:
        #Un client a quelque chose a nous dire:
        for client in client_a_lire:
            try:
                msg_recu = client.recv(1024)
                msg_recu = msg_recu.decode()
                if (gsub(msg_recu,0,10)== "Register: "):
                    joueurs.append(gsub(msg_recu,11,30))
                    joueurs.append(0)
                    joueurs.append(0)
                if (gsub(msg_recu,0,6)== "moove "):
                    nb_select_ply = detect_charactere(gsub(msg_recu,7,20),":")
                    select_ply = gsub(msg_recu,7,nb_select_ply)
                    if(gsub(msg_recu,9+nb_select_ply,30) == "moove_right"):
                        table_index = find_table_index(joueurs,select_ply)
                        joueurs[table_index+1] = joueurs[table_index+1] + 10
                    if(gsub(msg_recu,9+nb_select_ply,30) == "moove_left"):
                        table_index = find_table_index(joueurs,select_ply)
                        joueurs[table_index+1] = joueurs[table_index+1] - 10
                    if(gsub(msg_recu,9+nb_select_ply,30) == "moove_top"):
                        table_index = find_table_index(joueurs,select_ply)
                        joueurs[table_index+2] = joueurs[table_index+2] - 10
                    if(gsub(msg_recu,9+nb_select_ply,30) == "moove_bot"):
                        table_index = find_table_index(joueurs,select_ply)
                        joueurs[table_index+2] = joueurs[table_index+2] + 10
                #Il veut se deco proprement, on l'enleve de la table joueur.
                if(gsub(msg_recu,0,11) == "disconnect "):
                    table_index = find_table_index(joueurs,gsub(msg_recu,12,30))
                    del joueurs[table_index]
                    del joueurs[table_index]
                    del joueurs[table_index]
                    print("Un joueur vient de se deconnecter")
            #Il se deconnecte de force ou a crash:
            except socket.error as err:
                client_connectes.remove(client)
                continue

