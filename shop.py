#!/usr/bin/env python
# -*- coding: utf-8 -*-
#fichier de la boutique 
#projet : RPG2000

#importation de la librairie pygame et initialisation
import pygame
from pygame.locals import*

pygame.init()

#activation du mode video
fenetre = pygame.display.set_mode((960,640))

bvn = pygame.image.load("maps/shop/bvn.png").convert_alpha()
forge = pygame.image.load("maps/shop/forge.jpg").convert()
armes = pygame.image.load("maps/shop/armes.png").convert()
bs = pygame.image.load("maps/shop/bs.png").convert_alpha()
cur = pygame.image.load("maps/shop/cur.png").convert_alpha()
conf = pygame.image.load("maps/shop/confirmation.png").convert_alpha()
fd = pygame.image.load("maps/shop/flech_d.png").convert_alpha()
fg = pygame.image.load("maps/shop/flech_g.png").convert_alpha()
fond = pygame.image.load("maps/shop/fond.png").convert()

#la boutique se résume à 1 grande fonction que l'on peut appeller à loisir
def shop(fenetre=pygame.display.set_mode((960,640))):

	global pseudo
	#affichage du message de bienvenue
	fenetre.blit(forge, (0,0))
	fenetre.blit(bvn, (42,465))
	pygame.display.flip()
	shop = 1
	selection = 0
	entree = 1
	
	fenetre.blit(forge, (0,0))
	fenetre.blit(bvn, (42,465))
	pygame.display.flip()
	
	buy = 0
	selection = 0
	confirmation = 0

#boucle infinie tant que l'on ne souhaite pas quitter
	while shop == 1:
		
		#boucle n°2, on attend que le joueur appuie sur une touche
		while entree == 1 and shop == 1:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					#une fois que c'est le cas on affiche l'écran
					#de selection des actions
					fenetre.blit(forge, (0,0))
					entree = 0
					selection = 1
					fenetre.blit(bs,(800,500))
					fenetre.blit(cur, (760,580))
					pygame.display.flip()
					pos = 0

		#boucle n°3, on choisit l'action à executer:
		#acheter, vendre ou quitter
		#chaque position correspond à une action(2,1,0)
		while selection == 1 and shop == 1:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					#on déplace le curseur vers le haut si le joueur appuie sur la touche haut, W, ou ZeroDivisionError
					#pour que ca marche en qwerty et azerty
					if (event.key == K_UP or event.key == K_w or event.key == K_z) and pos < 2:
						pos += 1
						fenetre.blit(forge, (0,0))
						fenetre.blit(bs,(800,500))
						fenetre.blit(cur, (760,600-(pos*40)-20))
						pygame.display.flip()
					#idem avec le bas
					if (event.key == K_DOWN or event.key == K_s) and pos > 0:
						pos -= 1
						fenetre.blit(forge, (0,0))
						fenetre.blit(bs,(800,500))
						fenetre.blit(cur, (760,600-(pos*40)-20))
						pygame.display.flip()
					#si le joueur appuie sur entree ou espace
					if event.key == K_RETURN or event.key == K_SPACE:
						#differentes actions selon la position du curseur
						if pos == 0:
						#si on est sur quitter on quitte simplement en fermant les boucles

							fenetre.blit(forge,(0,0))
							pygame.display.flip()
							selection = 0
							shop = 0
						if pos == 1:
							#ouverture de l'inventaire on verra plus tard
							rien = 'rien'
						if pos == 2:
						#si on est sur acheter, on passe à l'écran de selection des armes
							buy = 1
							pos = 0
							selection = 0
							fenetre.blit(forge,(0,0))
							fenetre.blit(armes,(0,0))
							fenetre.blit(cur,(0,590))	
							pygame.display.flip()

		#boucle n°4, on a un autre menu pour selectionner l'arme que l'on souhaite						
		while buy == 1 and shop == 1:
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					#on bouge le curseur vers la position souhaitee par le joueur
					if (event.key == K_UP or event.key == K_w or event.key == K_z) and pos < 12:
						pos = pos + 1
					if (event.key == K_DOWN or event.key == K_s) and pos > 0:
						pos = pos - 1

					fenetre.blit(forge,(0,0))
					fenetre.blit(armes,(0,0))

					#l'affichage du curseur est un peu bizarre mais c'est parce que
					#les armes ne sont pas toutes espacées de la même façon
					if pos in range(6,13):
						hauteur = (12-pos)*30+40
						fenetre.blit(cur,(0,hauteur))
						pygame.display.flip()
					if pos in range(3,6):
						hauteur = (5-pos)*30+290
						fenetre.blit(cur,(0,hauteur))
						pygame.display.flip()
					if pos == 2:
						hauteur = 420
						item = b"bois magique   40"
						fenetre.blit(cur,(0,hauteur))
						pygame.display.flip()
					if pos == 1:
						hauteur = 490
						item = b"arme interdite 200"
						fenetre.blit(cur,(0,hauteur))
						pygame.display.flip()
					if pos == 0:
						hauteur = 590
						fenetre.blit(cur,(0,hauteur))
						pygame.display.flip()

					if pos == 3:
						item = b"arc courbe   "
					if pos == 4:
						item = b"arc double   "
					if pos == 5:
						item = b"arc elfic    "
					if pos == 6:
						item = b"hache double "
					if pos == 7:
						item = b"hallebarde   "
					if pos == 8:
						item = b"masse d'arme "
					if pos == 9:
						item = b"marteau lourd"
					if pos == 10:
						item = b"espadon lourd"
					if pos == 11:
						item = b"epee legere  "
					if pos == 12:
						item = b"dague        "


					#si l'utilisateur appuie sur entree ou espace
					#on passe à l'écran de confirmation
					if event.key == K_RETURN or event.key == K_SPACE:
						confirmation = 1
						buy = 0
						cf = 'r' # variable du menu de confirmation
						fenetre.blit(forge,(0,0))
						fenetre.blit(armes,(0,0))
						fenetre.blit(cur,(0,hauteur))
						fenetre.blit(conf,(352,250))
						fenetre.blit(fd,(457,322))
						pygame.display.flip()

		#boucle n°5, on verifie si le joueur n'a pas cliqué par erreur
		while confirmation == 1 and shop == 1:
			for event in pygame.event.get():
				#on affiche un fleche pointant dans la
				#direction choisie par le joueur
				if event.type == KEYDOWN:
					if event.key == K_RIGHT or event.key == K_d:
						cf = 'r'
						fenetre.blit(forge,(0,0))
						fenetre.blit(armes,(0,0))
						fenetre.blit(cur,(0,hauteur))
						fenetre.blit(conf,(352,250))
						fenetre.blit(fd,(457,322))
						pygame.display.flip()
					if event.key == K_LEFT or event.key == K_a or event.key == K_q:
						cf = 'g'
						fenetre.blit(forge,(0,0))
						fenetre.blit(armes,(0,0))
						fenetre.blit(cur,(0,hauteur))
						fenetre.blit(conf,(352,250))
						fenetre.blit(fg,(457,322))
						pygame.display.flip()
					#lorsqu'il appuie sur entree, une action est effectuee
					#selon la direction vers laquelle pointait
					#la fleche
					if event.key == K_RETURN or event.key == K_SPACE:
						#paiement effectué
						#monnaie = monnaie - prix
						if cf == 'g' and pos != 0:
							connexion_avec_serveur.send(b"shop "+pseudo+b": buy "+item)
							confirmation = 0
						if cf == 'g' and pos == 0:
							confirmation = 0
							shop = 0
						if cf == 'r':
							fenetre.blit(forge,(0,0))
							fenetre.blit(armes,(0,0))
							fenetre.blit(cur,(0,hauteur))
							pygame.display.flip()
							confirmation = 0
							buy = 1
							shop = 1
	fenetre.blit(fond,(0,0))
	pygame.display.flip()
					
