#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Fonctions pour l'affichage des textes et menus
# Projet : RPG2000
import time

import pygame
from pygame.locals import *

#class Player:  # Toutes les variables d'un joueur ou ennemi
# def __init__(self, hp, atk, defense):
#       hp = 2
#       atk = 2
#       defense = 2

#class Battle:  # Toutes les fns pour gerer un combat
# def get_first_player(self, player_stats, enemy_stats): # Inutile pour l'instant
#     global player_first
#     if player_stats[3] > enemy_stats[3]:
#         player_first = 1
#     else:
# player_first = 0

## On va definir les differentes attaques disponibles ##

#   def simple_atk(attaquant, defenseur): # Le fonctionnement de l'attaque simple
#       if attaquant.atk == defenseur.defense:
#           return attaquant.hp, (defenseur.hp - 1)
#       elif attaquant.atk < defenseur.defense: # Si atk<def, ont laisse une chance
#           if randint(0,1):
#               return attaquant.hp, (defenseur.hp - 1)
#           else:
#               return attaquant.hp, defenseur.hp
#       else:
#           return attaquant.hp, (defenseur.hp-(attaquant.atk-defenseur.defense)*2) # On avantage tout de meme le fait d'avoir beaucoup d'atk

#   def self_damage(attaquant, defenseur):
#       # affichage(attaquant,defenseur)
#       hp1 = attaquant.hp - attaquant.atk
#       hp2 = defenseur.hp - attaquant.atk
#       return hp1, hp2

#class UI:
#    def affichage(ally, enemy):
#        print("PV du joueur:", str(ally.hp), "PV de l'ennemi:", str(enemy.hp), sep='\n')
#    def hpbar(hp):
#        if hp<1:
#            print("M O R T")
#        else:
#            print(hp, end = ' ')
#            for i in range(0,hp-1):
#                print("▓", end = ' ')
#            print('▓') # Parcequ'on veut un \n a la fin
#    def menugraphique(optionlist): # Pour que le joueur choisisse son attaque ou n'importe quoi d'autre
#        fenetre = pygame.display.set_mode((960,640))
#        return choice
#
#def mainfn(playerhp,playeratk,playerdef,enemyhp,enemyatk,enemydef):
#    while not exit:
#        prout()

fenetre = pygame.display.set_mode((960, 640))
fond = pygame.image.load("maps/shop/fond.png").convert()
fenetre.blit(fond, (0, 0))


def yves(txt='err', lettres='lettres', top_left=(0, 0), bot_right=(960, 640)):
    # pygame.init()
    char_img_width = 24
    char_img_height = 40
    total_width = bot_right[0] - top_left[0]
    collumn_number = total_width // char_img_width
    # total_height = bot_right[1] - top_left[1]
    # line_number = total_height // char_img_height

    print('top : ' + str(top_left[1]) + '\nbot : ' + str(bot_right[1]))

    def loadimage(name, letter=0):
        if name == '/':
            return pygame.image.load(lettres + '/' + letter).convert_alpha()
        else:
            return pygame.image.load(lettres + name).convert_alpha()

    def splitlist(liste, line_end, newline):
        ret_list = ['', '', '', '', '', '', '', '', '', '', '']
        line = 0
        char_horiz_pos = 0
        for char in liste:
            ret_list[line] += char
            # newline indique que l'on veut un retour a la ligne
            # et on est oblige de le faire si on atteint la fin de ligne
            if char == newline or char_horiz_pos == line_end:
                line += 1  # On passe a une nouvelle ligne...
                char_horiz_pos = 0  # donc on remet le compteur horizintal a 0
            else:
                char_horiz_pos += 1
        return ret_list

    txt = splitlist(txt, collumn_number, '\\')
    # accents = ['é', 'è', 'ê', 'à', 'ù']
    y = 0
    for mot in txt:  # On prend les strings dans la liste
        x = 0
        for i in mot:  # Puis les chars dans chaque string
            if i.isalpha():  # Vérifie qu'on a une lettre
                current_char_img = loadimage('/', i)
            elif i == ".":
                current_char_img = loadimage('/dot')
            elif i == " ":
                current_char_img = loadimage('/space')
            elif i == ",":
                current_char_img = loadimage('/comma')
            elif i == "!":
                current_char_img = loadimage('/exclam')
            elif i == "\\":
                current_char_img = None
            if current_char_img:
                xpos = top_left[0] + x * char_img_width
                ypos = top_left[1] + y * char_img_height
                fenetre.blit(current_char_img, (xpos, ypos))
            pygame.display.flip()
            # delay = 0.05
            # time.sleep(delay)
            x += 1
        y += 1


def menu(options=['nada', 'niet'],
         fonctions=["print('test0')", "print('test1')"],
         l=0,
         r=920):

    for i in range(0, len(options)):
        top = (l + 36, i * 40)
        bot = (r, i * 40 + 40)
        print(top)
        print(bot)
        yves(options[i], 'lettres', top, bot)

    cursor_pos = 0
    check = True
    # On affiche le curseur
    yves('x', 'lettres', (l, cursor_pos * 40),
            (l + 36, cursor_pos * 40 + 40))
    while check:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key in [K_UP, K_w, K_z]:
                    if cursor_pos == 0:
                        cursor_pos = len(options) - 1
                    else:
                        cursor_pos -= 1
                if event.key in [K_DOWN, K_s]:
                    if cursor_pos == len(options) - 1:
                        cursor_pos = 0
                    else:
                        cursor_pos += 1
                if event.key in [K_RETURN, K_RIGHT, K_d]:
                    exec (fonctions[cursor_pos])
                # On reblit si on a appuye sur une touche pour enlever l'ancien curseur
                global fenetre
                global fond
                fenetre.blit(fond, (0, 0))
                for i in range(0, len(options)):
                    top = (l + 36, i * 40)
                    bot = (r, i * 40 + 40)
                    print(top)
                    print(bot)
                    yves(options[i], 'lettres', top, bot)

                yves('x', 'lettres', (l, cursor_pos * 40),
                     (l + 36, cursor_pos * 40 + 40))

            if event.type == QUIT:
                check = False
        # print(cursor_pos)


if __name__ == "__main__":
    # yves("paix a ton ame,\yves. tu etait un grand homme")
    a = 'a'
    menu(l=60, r=920)
    # eval("print('test')")
    execute = True
    # while execute:
    # for event in pygame.event.get():
    #     if event.type == QUIT:
    #         execute = False
# j=Player()
# e=Player()
# j.hp=8
# e.hp=4
# UI.affichage(j,e)
# j.hp, e.hp = Battle.simple_atk(j,e)
# UI.affichage(j,e)
# UI.hpbar(j.hp)
# UI.hpbar(e.hp)
# lol=input()
