# Modules

import time
import os
import platform
from Acts.actzero import *

# Clear Function

def clear():
    if platform.system() == 'Linux':
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

# Title Screen

print("Satisfaction - A little game about hope")
print("")
print("")
print("Type 'r' and then press 'ENTER' / 'RETURN' to start the game.")
print("Do anything else to quit.")

start_prompt=input("> ")

if start_prompt == "r":
    print("Starting game...")
    time.sleep(2)
    clear()
    actzero()
else:
    print("Thanks for considering to play.")
    time.sleep(2)
    exit()


