from helpers import read_maze, offset, is_legal_path, get_path
from stack import myStack

def dfs(maze, start, goal):
    stack = myStack()
    stack.push(start)
    predecessors = {
        start: None
    }
    
    while not stack.is_empty():
        current_cell = stack.pop()
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        for direction in ["up", "down", "left", "right",]:
            row_offset, col_offset = offset[direction]
            neighbor = (current_cell[0] + row_offset , current_cell[1] + col_offset )
            if is_legal_path(maze, neighbor) and neighbor not in predecessors:
                stack.push(neighbor)
                predecessors[neighbor] = current_cell
    return None
                