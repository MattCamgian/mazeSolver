#https://github.com/MattCamgian/mazeSolver
from pprint import pprint
from random import shuffle, randrange
import numpy as np


def make_maze(w=6, h=8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]
    maze = np.ones([h*2,w*2])
    for w_index in range(0, w*2, 2):
        for h_index in range(0, h * 2, 2):
            maze[h_index,w_index] = 0

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]: continue
            if xx == x:
                hor[max(y, yy)][x] = "+  "
                maze[min(y, yy)*2+1][x*2] = 0
            if yy == y:
                ver[y][max(x, xx)] = "   "
                maze[y * 2][min(x, xx) * 2+1] = 0
            walk(xx, yy)

    walk(randrange(w), randrange(h))
    maze = np.hstack([np.ones([h*2,1]),maze])
    maze = np.vstack([np.ones([1,w*2+1]),maze])
    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])

    start_x = 1
    start_y = 1
    end_x = h * 2 - 1
    end_y = w * 2 - 1

    return maze, start_x, start_y, end_x, end_y

def make_empty_env(w=6, h=8):
    env = np.ones([h * 2, w * 2])

    for w_index in range(1, w*2):
        for h_index in range(1, h * 2):
            env[h_index,w_index] = 0

    env = np.hstack([env, np.ones([h*2,1])])
    env = np.vstack([env, np.ones([1,w*2+1])])

    start_x = 1
    start_y = 1
    end_x = h * 2 - 1
    end_y = w * 2 - 1
    return env, start_x, start_y, end_x, end_y

def create_q_table(h, w, start_x, start_y, end_x, end_y):
    q_table = []
    for i in range(0,w*2+1):
        row = []
        for j in range(0,h*2+1):
            row.append([0.0,0.0,0.0,0.0])
        q_table.append(row)

    return np.array(q_table)
