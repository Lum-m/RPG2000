#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Fonction bien utilse faite par moi-meme :=)
def gsub(mot,debut,fin):
    """gsub prend fin caracteres dans mot, en commencant
       au debutieme caractere
       /!\ l'index commence a 1, si debut==0 la fonction
           se comporte comme si debut==1
       /!\ remplacable par string[nombre:nombre]"""
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
