import os
import time

from constants import MOVES, ANIMATION_DELAY
from board import legal_moves

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_board(board):
    """Prints the board with the correct alignments."""
    
    for row in board:
        print("   ", end = "")
        for val in row:
            print("{:3}".format(val), end = " ")
        print()

def get_move(pos):
    """Gets move from keyboard."""
    move_accepted = False
    while not move_accepted:
        key = input().lower()
        if key in ('a','s','d','w','q','e'):
            move = MOVES[key]
            if move in legal_moves(pos) or move in ('quit','AI'):
                move_accepted = True
            else:
                print("This move is not allowed.")
        else: 
            print("Key not allowed.")
            
    return move

def title():
    """Prints title of the game"""
    
    print("   _____                      ___  ___ ")
    print("  / ___/__ ___ _  ___   ___  / _/ ( _ )")
    print(" / (_ / _ `/  ' \/ -_) / _ \/ _/ / _  | ")
    print(" \___/\_,_/_/_/_/\__/  \___/_/   \___/ ")
    print()
    
def print_screen(board, instructions=True):
    """Refreshes and prints everything that is needed."""
    
    clear_screen()
    title()
    print_board(board)
    if instructions:
        prompt = ("\nPress a key + ENTER"
                  "\n Moves     Keys\n"
                  "-------   ------\n"
                  " Left      a\n"
                  " Right     d\n"
                  " Up        w\n"
                  " Down      s\n"
                  "-------   ------\n"
                  "Quit       q\n"
                  "Let the AI play       e")   
        print(prompt)  
    
def end_of_game():
    """Asks for another round, returns boolean answer."""
    
    print("\nDo you want to play again? (y/n)")
    replay = input()
    if replay.lower() == 'y':
        return True
    else:
        return False

def AI_part(path):
    """Prints the path, returns last board."""
    
    i, arrow = 0, 0
    k=len(path)/10
    
    for node in path:
        print_screen(node.board, instructions=False)
        # Progress Bar
        i += 1
        arrow = int(i/k)
        
        print("\n\n Progress:")
        print(' |'+arrow*'-'+'>'+(10-arrow)*' '+'|')
        print('\n Total moves: ', i-1)
        
        time.sleep(ANIMATION_DELAY)

    return node.board