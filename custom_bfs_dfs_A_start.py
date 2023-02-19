
from queue import Queue
from queue import PriorityQueue

# dfs implementation using stack 

def dfs(maze,start_pos,goal):
    # in python list has a similar functinality as stack
    discoverd = []
    predecessors = dict()
    
    offset = {
        "up":(-1,0),
        "right":(0,1),
        "down":(1,0),
        "left":(0,-1)
    }
    
    discoverd.append(start_pos) # appending the element to the end (right) of the list
    predecessors[start_pos] = None
    
    while len(discoverd) != 0: # discoverd not empty
        visited_cell = discoverd.pop() # it pops the last (right) item
        if visited_cell == goal:
            # bingo return the path
            path = list()
            curr_cell = goal
            while curr_cell != start_pos:
                try:
                    path.append(curr_cell)
                    curr_cell = predecessors[curr_cell]
                except: raise KeyError("predecessors key is missing")
            path.append(start_pos)
            path.reverse()
            return path
        for direction in ["up","right","down","left"]:
            row_offset, col_offset = offset[direction]
            nieghbor = (visited_cell[0]+row_offset, visited_cell[1]+col_offset)
            row, col = nieghbor
            
            # check if the cell is valid
            if (0<=row<len(maze)) and (0<=col<len(maze[0])) and maze[row][col] !="*" and nieghbor not in predecessors:
                discoverd.append(nieghbor)
                predecessors[nieghbor]=visited_cell
    return None

# bfs implementation using queue.Queue
def bfs (maze,start_pos,goal):
    discoverd = Queue()
    predecessors=dict()
    offset = {
        "up":(-1,0),
        "right":(0,1),
        "down":(1,0),
        "left":(0,-1)
    }
    discoverd.put(start_pos)
    predecessors[start_pos] = None

    while not discoverd.empty():
        visited_cell = discoverd.get()
        if visited_cell == goal:
            #bingo get the path
            path = []
            curr_cell = goal
            while curr_cell != start_pos:
                    path.append(curr_cell)
                    curr_cell = predecessors[curr_cell]
            path.append(start_pos)
            path.reverse()
            return path
        for direction in ["up","right","down","left"]:
            row_offset, col_offset = offset[direction]
            nieghbor = (visited_cell[0]+row_offset, visited_cell[1]+col_offset)
            row, col = nieghbor
            #check to see nieghbor is a valid cell
            if (0<=row<len(maze)) and (0<=col<len(maze[0])) and maze[row][col] != "*" and nieghbor not in predecessors:
                discoverd.put(nieghbor)
                predecessors[nieghbor] = visited_cell
    return None
                
            
    
    


maze_default = [[" "," ","*"," "],
                [" "," "," "," "],
                [" ","*"," ","*"],
                [" "," "," "," "]]
#maze = read_maze("./mazes/diagonal_23x23.txt")
dfs_path = dfs(maze_default, (0,0),(3,3))
bfs_path = bfs(maze_default, (0,0),(3,3))

print(f"bfs route: {bfs_path}" + '\n'*2)
print(f"dfs route: {dfs_path}" + '\n'*2)

assert (bfs(maze_default, (0,0),(3,3))) == [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2), (3, 2), (3, 3)]
