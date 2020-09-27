#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import random
enemy = ''
rand = random.randint(1, 3)
if rand == 1:
    enemy = 'thanos'
elif rand == 2:
    enemy = 'Galactious'
elif rand == 3:
    enemy = 'Loki'


def message(message):
    print (message)
    time.sleep(2)


def intro():
    message("This is called 'The Hero Revenges' game.")
    message("Let's imagine that there's a superhero"
            " called 'thor' in a multiuniverse"
            " and his planet is called 'asgard'."
            )
    message("He left his planet to see his"
            " friend 'iron man' in another planet"
            " to see his friend 'iron man' in another planet."
            )
    message("He suddenly recieves a message that"
            " is planet has exposed to an"
            "invasion from a titan called " + enemy + '.')
# ______________________________________________________________________________
# _____________________________________________________________________________


def chasing_func():
    chasing = input('''Now, fight him or run ,
[fight/run]
''')

    if 'run' in chasing:
        message("you`ve sucessfuly escaped i think"
                "its time for getting help"
                )
        after_intro()
    elif 'fight' in chasing:
        message('You are trying to kill ' + enemy + '...')
        message('you was about to kill ' + enemy +
                ' but he got you down'
                )
        message(enemy + ' is chasing you!!')
        message('he is a titan!,he killed you!!!\n You lost')
    else:
        chasing_func()


# _______________________________________________________________________________

def alone_func():
    message('You decided to go alone ')
    message("you shocked that " + enemy +
            " is stronger than you,"
            "you can`t defeat him"
            )
    chasing_func()


# _____________________________________________________________________________
# ______________________________________________________________________________

def help_func():
    message('You asked iron man for a help,He accepted')
    message('you reached the planet of asgard\n')
    message("it's a true violent war there!!")
    message("it's the final chance now and iron man is facing " + enemy)
    attack_func()
# ______________________________________________________________________________


def attack_func():
    attack = input('you should help him [Yes/No]\n').lower()

    if 'no' in attack:
        message("iron man tried his best but"
                "he got killed," + enemy + " is tired"
                )
        message('now you got angry and killed ' + enemy +
                " .\nSad Victory!")
    elif 'yes' in attack:

        message("Both of you attacked " + enemy + " at same time")
        message("He couldn`t beat both of you,"
                "You killed " + enemy + '\n,Victory!')
    else:

        attack_func()


# _________________________________________________________________________________
# _________________________________________________________________________________


# i`ve made this to allow you continue when you run


def after_intro():
    while True:
        decide = input('so now, decide to go back to kill ' + enemy +
                       ' alone or you call firend for a  help ?'
                       '(please enter alone or help)'
                       ).lower()
        if 'alone' in decide:
            alone_func()
            break
        elif 'help' in decide:
            help_func()
            break
        else:
            message("please enter 'alone' or 'help")


# ____________________________________________________________________
# __________________________________________________________________


# no i will make a play again function sets on user`s choice

def play_again():
    while True:
        again = input('Would you like to play again ! \n [Yes/No]').lower()
        if 'yes' in again:
            print ('Excellant,Game is restarting....')
            start_game()
            break
        elif 'no' in again:
            print ('thank you for playing....')
            break
        else:
            message(again)


def start_game():
    intro()
    after_intro()
    play_again()

start_game()
