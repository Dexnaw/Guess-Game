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

def menuReplay():
    choix = input('Voulez vous rejouer (1) ou retourner au menu (2)? \n> ')
    if choix == "1":
        playerIsUser()
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
                menuReplay()

        user_input = userPlay()

def playerIsIA():
    min = 1
    max = 100
    coup = 0;
    value = 0
    user_input = input('Quel sera le nombre que l\'IA devra deviner ? \n> ')

    while  value!= user_input:
        try :
            value = int(user_input)
        except ValueError:
            print("Veuillez entrer un nombre !")
        else :
            rand = random.randint(min,max)
            coup = coup + 1
            if rand > value:
                max = rand
            elif rand < value:
                min = rand
            else :
                print('IA en %d' %coup)
menu()

#TODO Vérifier si l'input de l'user est un nombre !
#Il existe un moyen de définir le type en python type(input)
