#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import select

connexion_princ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_princ.bind(('', 57895))
connexion_princ.listen(5)

client_connectes = []

while True:
    should_send = False
    nouvelle_connexion,wlist,xlist = select.select([connexion_princ],[],[],0.05)

    for connexion in nouvelle_connexion:
        connexion_client, info_connexion = connexion.accept()
        client_connectes.append(connexion_client)
        print("Une nouvelle connexion vient d'avoir lieu")

    client_a_lire = []
    try:
        client_a_lire, wlist, xlist = select.select(client_connectes,[],[],0.05)
    except select.error:
        pass
    else:
        for client in client_a_lire:
            try:
                msg_recu = client.recv(1024)
                msg_recu = msg_recu.decode()
                print("Reçu")
                print(format(msg_recu))
                should_send = True
            except socket.error as err:
                print(err)
                client_connectes.remove(client)
                for client in client_connectes:
                    client.send(b"Un utilisateur vient de se déconnecter")
                continue

    if should_send:
        for client in client_connectes:
            client.send(msg_recu.encode())
