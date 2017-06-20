import matplotlib.pyplot as plt
import matplotlib
import time
import numpy as np

def display_grid(N, grid, paths, explored):
    data = grid[:]
    for i in range(N):
        for j in range(N):
            if (i,j) in explored:
                data[i][j] = 1
            else:
                data[i][j] = data[i][j]*3

    for i in range(N):
        for j in range(N):
            if (i,j) in paths:
                data[i][j]=2

    fig, ax = plt.subplots(1, 1, tight_layout=True)
    # make color map
    my_cmap = matplotlib.colors.ListedColormap(['white', 'grey', 'green', 'black'])
    # draw the grid
    for x in range(N + 1):
        ax.axhline(x, lw=2, color='k', zorder=5)
        ax.axvline(x, lw=2, color='k', zorder=5)
    # draw the boxes
    ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)
    # turn off the axis labels
    ax.axis('off')
    plt.show()


def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set()  # set of states we have visited
    frontier = [[start]]  # ordered list of paths we have blazed
    i=1
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        options = successors(s).items()
        for (state, action) in options:
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
        i += 1
    return []


def get_grid_frame(N, grid, paths, explored):
    data = grid[:]
    for i in range(N):
        for j in range(N):
            if (i, j) in explored:
                data[i][j] = 1
            else:
                #print(data[i][j])
                data[i][j] = 3 if data[i][j] == 1 or data[i][j] == 3 else 0

    for i in range(N):
        for j in range(N):
            if (i, j) in paths:
                data[i][j] = 2
    return data


def shortest_path_search_visualized(start, successors, is_goal, grid):
    N = len(grid)
    fig, ax = plt.subplots(1, 1, tight_layout=True)
    # make color map
    my_cmap = matplotlib.colors.ListedColormap(['white', 'grey', 'green', 'black'])
    # draw the grid
    for x in range(N + 1):
        ax.axhline(x, lw=2, color='k', zorder=5)
        ax.axvline(x, lw=2, color='k', zorder=5)
    # draw the boxes
    img = ax.imshow(get_grid_frame(N, grid, [], []), interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)
    # turn off the axis labels
    ax.axis('off')
    fig.show()
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set()  # set of states we have visited
    frontier = [[start]]  # ordered list of paths we have blazed
    i=1
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        options = successors(s).items()
        for (state, action) in options:
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                #print('showing grid with path: {0} and explore:{1}'.format(path_states(path2), explored))
                img.set_data(get_grid_frame(N, grid, path_states(path2), explored))
                fig.canvas.draw()
                fig.canvas.flush_events()
                time.sleep(.15)
                if is_goal(state):
                    return path2, explored
                else:
                    frontier.append(path2)
        i += 1
    return []



def path_states(path):
    "Return a list of states in this path."
    return path[0::2]


def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]


def test_ride():
    return 'test_ride passes'

"""
Grid is defined as shown below where 0 is passage, 1 is wall,
 0 0 0 0 0
 0 0 1 1 0
 0 0 0 1 0
 0 0 0 0 0
 0 0 0 0 0

 state: current position as (x, y) starting from (0,0) as top left
 goal: any cell given as (x,y) just like in state
 actions: top, down, right, left as seen by user
 successors: (next_state, action) pair that doesn't go into a wall
 helpers: get_paths(x, y, grid) : gives tuples of paths and actions

"""


def get_paths(row, col, grid):
    res = {}

    # top
    if row > 0:
        if grid[row-1][col] == 0:
            res[(row-1, col)] = 'top'

    # right
    if col < len(grid[0])-1:
        if grid[row][col+1] == 0:
            res[(row, col+1)] = 'right'

    # down
    if row < len(grid) - 1:
        if grid[row+1][col] == 0:
            res[(row+1, col)] = 'down'

    # left
    if col > 0:
        if grid[row][col - 1] == 0:
            res[(row, col - 1)] = 'left'

    return res


def generate_grid(N):
    return [[np.random.choice(2, 1, p=[0.8, 0.2])[0] for col in range(N)] for row in range(N)]


# grid = [[0, 1, 0, 0, 0],
#         [0, 0, 0, 1, 0],
#         [1, 0, 0, 1, 0],
#         [0, 0, 1, 0, 0],
#         [0, 0, 0, 0, 0]]

grid = generate_grid(10)


def grid_successors(pos): return get_paths(pos[0], pos[1], grid)


def is_goal_cell(pos):
    row, col = pos
    return row == len(grid)-1 and col == len(grid)-1


path, explored = shortest_path_search_visualized((0, 0), grid_successors, is_goal_cell, grid)
print(path)
print(explored)
