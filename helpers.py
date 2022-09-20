
def read_maze(filename = "./mazes/modest_maz.txt")->list:
    """_summary_
    read maze function reads a maze map from a file and return it as a 2D lists, also
    inside the function there is checker to make sure that maze grid is rectangular

    Args:
        filename (str, optional): _description_. Defaults to "./mazes/modest_maz.txt".

    Raises:
        SystemExit: _description_
        there is two possible senarios to get a Raises. first is to try read from file
        that dosen't exist. Second is when the read maze's grid is not rectangular
        means the sub arrays lentghts dosen't match.

    Returns:
        list: return a 2D lists contains the maze map as a grid system 
    """
    try:
        with open(filename) as mazeFile:
            mazeList2D =  [[char for char in line.strip('\n')] for line in mazeFile]
            baseLength = len(mazeList2D[0])
            for i in range(1, len(mazeList2D)):
                if len(mazeList2D[i]) != baseLength: # check maze maze is rectangular
                    SystemExit()
                    raise("maze map not a rectangular",SystemExit)
                mazeFile.close()
                return mazeList2D
    except OSError as E: 
        print (E)
        raise SystemExit


offset = {
    "right" :(0, 1),
    "left"  :(0, -1),
    "up"    :(-1, 0),
    "down"  :(1, 0)
}

def is_legal_path(maze: list, pos: tuple)-> bool:
    """_summary_
    to check that current postation is free of obstcls and is in reach

    Args:
        maze (list): _description_
        pos (tuple): _description_

    Returns:
        bool: _description_
    """
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    
    return 0<= i < num_rows and 0<= j <num_cols and maze [i][j] !="*"

def get_path(predecessors: dict, start: chr , goal :chr)-> list:
    """_summary_

    Args:
        predecessors (dict): _description_
        start (chr): _description_
        goal (_type_): _description_

    Returns:
        list: _description_
    """
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path