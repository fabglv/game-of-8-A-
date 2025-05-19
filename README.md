# game-of-8-A*

A Python implementation of the classic 8-puzzle sliding tile game with an AI solver using the A* algorithm.

## Description

The 8-puzzle is a sliding puzzle that consists of a frame of numbered square tiles in random order with one tile missing.
In this implementation, the goal is to move the empty tile in order to arrange the numbered tiles from 1 to 8, with the empty space ending up in the bottom-right corner.
```
1 2 3
4 5 6
7 8 _
```

This implementation includes:
- Command-line interface to play the game
- AI solver using the A* algorithm with Manhattan distance heuristic
- Visualization of the AI solution


## Project Structure

```
constants.py               # Game constants
board.py                   # Board representation and operations
solver.py                  # A* algorithm implementation
ui.py                      # User interface functions
game.py                    # Main game logic and flow
```
