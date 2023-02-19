from queue_custom import Queue

from helpers import offset, is_legal_path, get_path

def bfs(maze, start_pos, goal):
    discovered = Queue()
    discovered.enqueue(start_pos)
    predecessors = dict()
    predecessors[start_pos] = None
    
    while not discovered.is_empty():
        curr_cell = discovered.dequeue()
        if curr_cell == goal:
            return get_path(predecessors, start_pos, goal)
        else:
            for direction in ["up","right","down","left"]:
                row_offset, col_offset = offset[direction]
                nieghbor = (curr_cell[0]+row_offset, curr_cell[1]+col_offset)
                if is_legal_path(maze, nieghbor) and nieghbor not in predecessors:
                    discovered.enqueue(nieghbor)
                    predecessors[nieghbor] = curr_cell
    return None 


maze_default = [[" "," ","*"," "],
                [" "," "," "," "],
                [" ","*"," ","*"],
                [" "," "," "," "]]

path = bfs(maze_default,(0,0),(3,3))

print(path)