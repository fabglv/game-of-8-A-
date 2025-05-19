import heapq
import time

from constants import GOAL, POS_GOAL, TIME_LIMIT
from board import legal_moves, move_tile

manhattan_dict = {'1': (0, 0), '2': (0, 1), '3': (0, 2),
                  '4': (1, 0), '5': (1, 1), '6': (1, 2), 
                  '7': (2, 0), '8': (2, 1), '_': (2, 2)}
# man_dict gives the correct position of each tile

def manhattan_distance(board):
    """Heuristic for A*."""
    
    total_dist = 0
    for i in range(3):
        for j in range(3):
            key = board[i][j]
            (ir, jr) = manhattan_dict[key]
            dist = abs(i-ir) + abs(j-jr)
            total_dist += dist
            
    return total_dist

class Node:
    
    def __init__(self, board, position, parent=None, depth=0):
        self.board = board
        self.position = position
        self.parent = parent
        self.depth = depth
        self.cost = self.depth + manhattan_distance(self.board)
        
    def list_children(self):
        children = []
        for move in legal_moves(self.position):
            new_board, new_pos = move_tile(self.board, self.position, move)
            children.append(Node(new_board, new_pos, self, self.depth + 1))
        return children
    
    def __lt__(self, other):
        return self.cost < other.cost
    
def A_star(start_board, start_pos):
    """Algorithm to solve the game."""

    start_time = time.time()
    
    open_heap = []
    visited = {} # board : cost
    
    start_node = Node(start_board, start_pos, depth=0)
    heapq.heappush(open_heap, start_node)
    visited[start_board] = start_node.cost
    
    while open_heap:
        if time.time() - start_time > TIME_LIMIT:
            print("Search aborted: time limit exceeded.")
            return None
        
        node = heapq.heappop(open_heap)
        
        if node.cost > visited.get(node.board, float('inf')):
            continue
        
        if node.board == GOAL:
            return reconstruct_path(node)
        
        for child in node.list_children():
                        
            if child.board not in visited or child.cost < visited[child.board]:
                visited[child.board] = child.cost
                heapq.heappush(open_heap, child)

def reconstruct_path(node):
    path = []
    while node:
        path.append(node)
        node=node.parent
    path.reverse()
    return path