import generator
from printer import printMaze

width = 6
height = 6
maze, start_x, start_y, end_x, end_y = generator.make_maze(width, height)

def move(x,y):
    maze[x][y] = 2

    if x == end_x and y ==end_y:
        return True

    if maze[x + 1][y] == 0:
        solved = move(x+1,y)
        if solved:
            return True
    if maze[x - 1][y] == 0:
        solved = move(x - 1, y)
        if solved:
            return True
    if maze[x][y + 1] == 0:
        solved = move(x,y + 1)
        if solved:
            return True
    if maze[x][y-1] == 0:
        solved = move(x,y-1)
        if solved:
            return True

    maze[x][y] = 3
    return False

move(start_x,start_y)
printMaze(maze)