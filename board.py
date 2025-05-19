import random

from constants import GOAL, POS_GOAL, DIRECTIONS

def legal_moves(pos):
    """Returns a list with the possible moves from a given position."""
    
    moves = ['up','down','left', 'right']
    if pos[0] == 0:
        moves.remove('up')
    elif pos[0] == 2:
        moves.remove('down')
    if pos[1] == 0:
        moves.remove('left')
    elif pos[1] == 2:
        moves.remove('right')
        
    return moves

def move_tile(board, pos, move):
    """Returns a new board and new empty tile position."""
    i, j = pos
    di, dj = DIRECTIONS[move]
    ni, nj = i + di, j + dj

    # Convert to mutable
    new_board = [list(row) for row in board]
    new_board[i][j], new_board[ni][nj] = new_board[ni][nj], new_board[i][j]

    # Convert back to tuple of tuples
    return tuple(tuple(row) for row in new_board), (ni, nj)

def solvable_board():
    """Generates a board that is solvable."""
    
    board = [list(row) for row in GOAL]
    pos = POS_GOAL
    for _ in range(10_000):
        move = random.choice(legal_moves(pos))
        i, j = pos
        di, dj = DIRECTIONS[move]
        ni, nj = i + di, j + dj
        board[i][j], board[ni][nj] = board[ni][nj], board[i][j]
        pos = (ni, nj)

    # Convert to tuple of tuples before returning
    return tuple(tuple(row) for row in board), pos