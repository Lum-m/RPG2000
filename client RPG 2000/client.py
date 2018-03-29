import socket
import threading


class recevoir(threading.Thread):
    def run(self):
        while True:
            msg_recu = connexion_avec_serveur.recv(1024)
            msg_recu = msg_recu.decode()
            print("--MESSAGE RECU--")
            print(format(msg_recu))
            print("----------------")

try:
    connexion_avec_serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connexion_avec_serveur.connect(("Relaxrp.fr", 57895))
    print("Connexion au serveur réalisé avec succès !")
    recevoir_message = recevoir()
    recevoir_message.start()

    msg_a_envoyer = ""
    while msg_a_envoyer != b"fin":
        msg_a_envoyer = input()
        # Peut planter si vous tapez des caractères spéciaux
        msg_a_envoyer = msg_a_envoyer.encode()
        # On envoie le message
        connexion_avec_serveur.send(msg_a_envoyer)

    print("Fermeture de la connexion")
    connexion_avec_serveur.close()
    
except socket.error as err:
    print("Impossible de se connecter au serveur !")
