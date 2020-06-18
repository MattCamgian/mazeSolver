import numpy as np
import random

import generator
from printer import printMaze

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

width = 3
height = 4

epsilon = 0.4
alpha = 0.1
gamma = 0.6

#setup the maze and the q-table
maze, start_x, start_y, end_x, end_y = generator.make_maze(width, height)
maze, start_x, start_y, end_x, end_y = generator.make_empty_env(width,height)
q_table = generator.create_q_table(width, height, start_x, start_y, end_x, end_y)

#perform q learning
for iterations in range(0, 100000):
    maze_copy = np.copy(maze)
    x = start_x
    y = start_y
    moves = 0

    #go until we reach the end or make 50 moves
    while not (x == end_x and y == end_y) and moves < 50:
        moves += 1
        if random.uniform(0, 1) < epsilon:
            action = int(random.uniform(0, 3))
        else:
            action = np.argmax(q_table[x][y])  # Exploit learned values

        if action == UP:
            new_x = x
            new_y = y -1
        elif action == DOWN:
            new_x = x
            new_y = y + 1
        elif action == LEFT:
            new_x = x - 1
            new_y = y
        else:
            new_x = x + 1
            new_y = y

        if new_y < 0 or new_y >= height * 2 + 1:
            new_y = y

        if new_x < 0 or new_x >= width * 2 + 1:
            new_x = x

        if maze_copy[new_x][new_y] != 0:
            new_x = x
            new_y = y

        old_value = q_table[x][y][action]
        next_max = np.max(q_table[new_x][new_y])

        if new_x == end_x and new_y == end_y:
            reward = 200
        else:
            reward = -1

        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[x][y][action] = new_value

        x = new_x
        y = new_y




#exploit the learned information to complete the maze and print the results
x = start_x
y = start_y
while not (x == end_x and y == end_y):

    action = np.argmax(q_table[x][y])  # Exploit learned values
    maze[x][y] = 2


    if action == UP:
        new_x = x
        new_y = y - 1
    elif action == DOWN:
        new_x = x
        new_y = y + 1
    elif action == LEFT:
        new_x = x - 1
        new_y = y
    else:
        new_x = x + 1
        new_y = y

    x = new_x
    y = new_y

maze[x][y] = 2
printMaze(maze)