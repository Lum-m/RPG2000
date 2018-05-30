#######################
#	              #
#generateur de map 2.0#
#		      #
#######################


!!!!!!!!!!!!!!!!!!!!!!!!
attention avant d'utiliser la fonction load_map()
vous devez au préalable importer le fichier .py associé
il faut donc ecrire au debut : import load_map(.py)
dans ce cas il faudra ecrire:
load_map.load_map()
on peut alors faire :
from load_map import*
pour ne pas avoir ce soucis et pouvoir simplement
ecrire load_map()





le generateur de map est une fonction permettant l'affichage d'un
tableau à la fois
pour chaque tableau, il est possible d'afficher une infinité de layers
les layers sont des couches d'images que l'ont peut afficher les
unes sur les autres.

il y a de definies dans la fonction load_map()
deux listes d'éléments : 
les elements sur lesquels le joueur peut marcher: la liste tiles[]
les elements sur lesquels le joueur ne peut marcher : la liste tiles_l2[]

les fichiers textuels comportant le contenu des maps sont de la forme suivante:
15 chiffres de long avec ou sans espace entre chaque
10 chiffres de haut SANS ESPACES ENTRE LES LIGNES

ex:

0 00 0 0 0 0 0 0 0 0 0 0 0 0
000 000 00 0 00 00 00
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
00 000 00 00 0 0 00 00
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
000 00 0000 00 000 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0000 0000 000 0000
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
00000 000 0 0 000 00


le generateur de map fonctionne de la facon suivante:

il a besoin de connaitre le fichier contenant la map
il a besoin de connaitre la liste d'images associée au fichier
il a besoin d'une surface sur laquelle afficher la map
car il ya deux listes d'images actuellement

exemple:


import pygame
from pygame.locals import*

pygame.init()

fenetre = pygame.display.set_mode((500,500))

with( open "layer_1.txt" as fichier):
	contenu = fichier.read()
load_map(contenu,tiles, fenetre)
