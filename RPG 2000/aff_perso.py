import pygame
from pygame.locals import*

pygame.init()

def aff_perso(fenetre, back, liste, px=480, py=320, direction ='haut'):
	fenetre.blit(back,(0,0))
	if direction == 'haut':
		fenetre.blit(liste[4],(px,py)) # liste avec les sprites, l'index est la position
		pygame.display.flip()
		pygame.time.wait(100)
		fenetre.blit(back,(0,0))
		fenetre.blit(liste[3],(px,py))
		pygame.display.flip()

	if direction == 'dte':
		fenetre.blit(liste[6],(px,py))
		pygame.display.flip()
		pygame.time.wait(100)
		fenetre.blit(back,(0,0))
		fenetre.blit(liste[5],(px,py))
		pygame.display.flip()

	if direction == 'gche':
		fenetre.blit(liste[2],(px,py))
		pygame.display.flip()
		pygame.time.wait(100)
		fenetre.blit(back,(0,0))
		fenetre.blit(liste[1],(px,py))
		pygame.display.flip()

	if direction == 'bas':
		fenetre.blit(liste[8],(px,py))
		pygame.display.flip()
		pygame.time.wait(100)
		fenetre.blit(back,(0,0))
		fenetre.blit(liste[7],(px,py))
		pygame.display.flip()

