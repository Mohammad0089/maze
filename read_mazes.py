def read_maze(fileName = "./mazes/diagonal_23x23.txt")->list[list]:
    try:
        with open(fileName) as mazeFile:
            # 2D list 
            maze = [[char for char in line.strip('\n')] for line in mazeFile]
            # check it is a recangular 2D lists len of all sub list should be same
            firstList = maze[0]
            for lst in range(1,len(maze)):
                if len(maze[lst]) != len(firstList):
                    raise("the maze is not rectangular", SystemExit)
            mazeFile.close()
            return maze
            
    except OSError as e:
        raise("there is a problem with the file you have selected", SystemExit)



if __name__=="__main__":
    maze = read_maze()
    for row in maze:
        print(row)