#!/usr/bin/env python3

import time
import sys
from ludo.cli import CLIGame

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    print("Install colorama with 'pip install colorama' for colored output.")
    Fore = Style = lambda x: ''

def loading_animation(text='Loading', dots=3, delay=0.4):
    for i in range(dots):
        sys.stdout.write(f'\r{text}{"." * (i + 1)}')
        sys.stdout.flush()
        time.sleep(delay)
    print('\n')

def launch_ludo():
    print(Fore.CYAN + Style.BRIGHT + "\n🎲 Welcome to the Legendary CLI Ludo Game! 🎲")
    print(Fore.YELLOW + "Get ready to roll the dice and dominate the board!\n")
    
    loading_animation("Summoning Ludo Lords")
    
    game = CLIGame()
    game.start()

if __name__ == '__main__':
    launch_ludo()
