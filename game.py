from constants import GOAL
from board import solvable_board, move_tile
from A_star import A_star
from ui import print_screen, get_move, AI_part, end_of_game

def play_single_match():
    """Plays a single match until the puzzle is solved or user quits."""
    
    (board, pos) = solvable_board()
        
    while True:
        print_screen(board)
        move = get_move(pos)
        if move == 'quit':
            break
        elif move == 'AI':
            path = A_star(board, pos)
            board = AI_part(path)            
        else:
            (board, pos) = move_tile(board, pos, move)
        if board == GOAL:
            print_screen(board, instructions = False)
            print("\n\nMatch won!")
            break
            
def play():
    """Runs the game loop, replaying matches until the player quits."""
    replay = True
    while replay:
        play_single_match()
        replay = end_of_game()
            
if __name__ == "__main__":    
    play()