#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time
import os
import sys
from Color import *

def clearThisShit():
    os.system('clear')

def menu():
    clearThisShit()
    hashtag = '###########################'
    tabulation = 80
    print(hashtag, end='\n')
    print('Bienvenue sur "GuessGame" !', end='\n')
    print(hashtag, end='\n')
    print('Sélectionnez un mode de jeu :')
    print('\n\t 1. Joueur vs IA (Vous devrez trouver le nombre)')
    print('\t 2. IA vs Joueur (L\'IA devra trouver votre nombre)')
    print('\t 3. Quitter le jeu...')
    choix = input('\nVotre choix (1-2-3) :\n> ')

    if choix == '1':
        playerIsUser()
    elif choix == '2' :
        clearThisShit()
        playerIsIA()
    elif choix == "3":
        clearThisShit()
        print(Color.YELLOW + 'MERCI D\'AVOIR JOUÉ')
        time.sleep(2)
        clearThisShit()
        sys.exit()
    else :
        clearThisShit()
        print('Tu te crois malin...')
        time.sleep(2)
        menu()

def menuReplay(x):
    choix = input('Voulez vous rejouer (1) ou retourner au menu (2)? \n> ')
    if choix == "1":
        if x == 0:
            playerIsUser()
        else :
            playerIsIA()
    elif choix == "2":
        menu()
    else :
        clearThisShit()
        print(Color.BOLD + Color.RED + 'Tu te crois malin...' + Color.END)
        time.sleep(2)
        menu()

def userPlay():
    return input('Devine le nombre (entre 1 et 100)\n> ')

def playerIsUser():
    #rand = random.randint(1,100)
    clearThisShit()
    rand = 50
    user_input = userPlay()
    coup = 0
    x = 0

    while rand != user_input:
        coup = coup + 1
        try :
            value = int(user_input)
        except ValueError:
            coup = coup + 1
            print("Ce n'est pas un nombre... +1 coup !")
        else :
            if value>100 or value<0:
                print("ENTRE 1 et 100... TU SAIS PAS LIRE OU QUOI? +1 coup !")
                coup = coup + 1
                user_input = userPlay()
            if int(user_input) > rand:
                print("C'est plus petit que %s" %user_input)
            elif int(user_input) < rand :
                print("C'est plus grand que %s" %user_input)
            else :
                print("BRAVO, REUSSI EN %d coup(s)\n" %coup)
                menuReplay(x)

        user_input = userPlay()

def iaPlay() :
    return input('Quel sera le nombre que l\'IA devra deviner ? \n> ')


def playerIsIA():
    x = 1
    min = 1
    max = 100
    coup = 0
    userNbr = 1
    iaNbr = 0
    clearThisShit()
    user_input = iaPlay()

    while  iaNbr != userNbr:
        try :
            userNbr = int(user_input)
            if userNbr>100 or userNbr<1:
                raise ValueError
        except ValueError:
            print("J'ai demandé un" + Color.BOLD + " NOMBRE ENTRE 1 ET 100" + Color.END)
            user_input = iaPlay()
        else :
            iaNbr = random.randint(min,max)
            coup = coup + 1
            time.sleep(1)
            if iaNbr > userNbr:
                print('IA propose : %d' %iaNbr )
                print('C\'est plus PETIT')
                max = iaNbr-1
            elif iaNbr < userNbr:
                print('IA propose : %d' %iaNbr )
                print('C\'est plus GRAND')
                min = iaNbr+1
            else :
                print('IA propose : %d' %iaNbr)
                print('IA à trouvé en %d coups'  %coup)
                menuReplay(x)

menu()

#TODO Vérifier si l'input de l'user est un nombre !
#Il existe un moyen de définir le type en python type(input)
