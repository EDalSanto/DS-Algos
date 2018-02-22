# -*- coding: utf-8 -*-

from collections import deque
import copy
import heapq
from pprint import pprint
import random
import pdb

# Constants for readability
START = S = 'S'
GOAL = G = 'G'

NORMAL = N = ' '
WALL = W = '#'
TREE = T = '^'

def main():
    little_world()
    big_world()
#    random_world(40, 40)

# Get's all nodes with edges to location as long as not wall
def get_successor_states(grid, location):
    row, col = location
    neighbors = []

    up = (row - 1, col)
    down = (row + 1, col)
    left = (row, col - 1)
    right = (row, col + 1)

    if (col + 1) < len(grid[row]) and grid[row][col + 1] != WALL:
        neighbors.append(right)

    if (row + 1) < len(grid) and grid[row-1][col] != WALL:
        neighbors.append(down)

    if (row - 1) >= 0 and grid[row-1][col] != WALL:
        neighbors.append(up)

    if (col - 1) >= 0 and grid[row][col - 1] != WALL:
        neighbors.append(left)

    return neighbors


def BFS(grid, starting_point):
    frontier = deque()
    explored = {}
                      # (0,0)
    frontier.append((starting_point, None)) # Startng point has no 'from'

    while len(frontier) > 0:
        current_location, parent = frontier.popleft()
        row, col = current_location

        if current_location in explored:
            continue
        elif grid[row][col] == GOAL:
            explored[current_location] = parent
            return explored

        neighbors = get_successor_states(grid, current_location)
        for neighbor in neighbors:
            if neighbor not in explored:
                frontier.append((neighbor, current_location))

        explored[current_location] = parent

    return explored

def DFS(grid, starting_point):
    # identical to BFS except frontier will behave like stack
    frontier = []
    # keeps track of nodes explored from parent
    explored = {}

    # add initial node to frontier with no from
    frontier.append((starting_point, None))

    # while still nodes left to explore
    while len(frontier) > 0:
        # get current_location and parent
        current_location, parent = frontier.pop()
        row, col = current_location

        # check to see if:
        # location already explored
        if current_location in explored:
            continue # in which case skip
        elif grid[row][col] == GOAL: # Goal node found
            # set final explored node
            explored[current_location] = parent
            # returns path taken
            return explored

        # otherwise look get neighbors not yet explored and add to frontier
        neighbors = get_successor_states(grid, current_location)
        for neighbor in neighbors:
            if neighbor not in explored:
                frontier.append((neighbor, current_location))

        # marks current_location as visited
        explored[current_location] = parent

    return explored

# just like BFS but using priority queue for frontier
#   priority queue => queue sorted by weight
def dijkstras(grid, starting_point):
    # Create dictionary for weights at O(V)
    weights = {}
    for ridx, row in enumerate(grid):
        for cidx, col in enumerate(row):
            # Each node represented by coordinates
            weights[(ridx, cidx)] = float("infinity")

    # Starting point has weight 0 from itself
    weights[starting_point] = 0

    # Nodes to visit
    frontier = []
    # Add initial node to frontier
    #   each element is (weight, current_location, from_location(previous))
    heapq.heappush(frontier, (0, starting_point, None)) # No from for initial node

    # All the nodes we have explored
    # explored[current_location] = parent
    explored = {}

    # while still unvisited nodes
    while len(frontier) > 0:
        # heappop => log(N)
        current_weight, current_location, parent = heapq.heappop(frontier)
        row, col = current_location

        if current_location in explored:
            continue
        elif grid[row][col] == GOAL:
            explored[current_location] = parent
            return explored

        neighbors = get_successor_states(grid, current_location)
        for neighbor in neighbors:
            # instead of checking if neighbor hasn't been visited
            # check if new path to location is
            # better than previous (i.e., less weight)
            nrow, ncol = neighbor
            if grid[nrow][ncol] == NORMAL:
                weight = weights[current_location] + 1
            elif grid[nrow][ncol] == TREE:
                weight = weights[current_location] + 2

            # new distance from starting_point to neighbor node costs less?
            if weight < weights[neighbor]:
                # Update shortest distance to neighbor
                weights[neighbor] = weight
                # Add to priority queue - also log(N)
                heapq.heappush(frontier, (weight, neighbor, current_location))

        # Mark current location as visited
        explored[current_location] = parent

    return explored

def a_star(grid, starting_point, goal_location):
    raise NotImplementedError()

# Setup code below this point, you should not need to modify any code below:
def little_world():
    grid_world = [
     [S, N, N, N],
     [N, W, W, W],
     [N, T, T, T],
     [N, N, N, G]
    ]

    starting_point = (0, 0)
    goal_point = (3, 3)
    compare(grid_world, starting_point, goal_point)

def big_world():
    grid_world = [
        [S, T, T, T, W, G],
        [N, T, T, T, W, N],
        [N, W, T, T, T, N],
        [N, N, N, N, T, N],
        [N, T, N, N, N, N],
        [N, T, N, N, N, N]
    ]

    starting_point = (0, 0)
    goal_point = (0, 5)
    compare(grid_world, starting_point, goal_point)


def random_world(rows, cols):
    starting_point = (0, 0)
    goal_point = (random.randint(0, rows-1), random.randint(0, cols-1))
    types = [NORMAL, WALL, TREE]
    grid_world = []
    for i in range(rows):
        grid_world.append([None] * cols)
        for j in range(cols):
            if (i, j) == starting_point:
                grid_world[i][j] = START
            elif (i, j) == goal_point:
                grid_world[i][j] = GOAL
            else:
                grid_world[i][j] = random.choice(types)

    compare(grid_world, starting_point, goal_point)


def compare(grid_world, starting_point, goal_point):
    # BFS
    explored = BFS(grid_world, starting_point)
    visualize_result(grid_world, explored, goal_point, "BFS")

    # DFS
    explored = DFS(grid_world, starting_point)
    visualize_result(grid_world, explored, goal_point, "DFS")

    # Dijkstra's
    explored = dijkstras(grid_world, starting_point)
    visualize_result(grid_world, explored, goal_point, "Dijkstra's")

    ## A*
    #explored = a_star(grid_world, starting_point, goal_point)
    #visualize_result(grid_world, explored, goal_point, "A-Star")

# For pretty printing
class color:
   BLACK = '\033[30m'
   CYAN = '\033[96m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def visualize_result(original_grid, explored, goal_location, algorithm_name):
    # Extract the found path
    path = set()
    path_cost = 0
    current_loc = goal_location

    if goal_location in explored:
        while current_loc != None:
            row, col = current_loc
            path.add(current_loc)
            if original_grid[row][col] == TREE:
                path_cost += 2
            elif original_grid[row][col] != START:
                path_cost += 1
            current_loc = explored[current_loc]

    # Colorize the visgrid
    vis_grid = copy.deepcopy(original_grid)
    for i, row in enumerate(vis_grid):
        for j, item in enumerate(row):
            stylized = color.UNDERLINE

            # Nodes in the path
            if (i, j) in path:
                if original_grid[i][j] == TREE:
                    stylized += color.CYAN + 'ô'
                elif original_grid[i][j] == START:
                    stylized += color.YELLOW + 'O'
                elif original_grid[i][j] == GOAL:
                    stylized += color.RED + 'O'
                else:
                    stylized += color.CYAN + 'o'
            # Non-path nodes
            else:
                if item == WALL:
                    stylized += color.BOLD + color.YELLOW + item
                elif item == TREE:
                    stylized += color.GREEN + item
                else:
                    stylized += item
            stylized += color.END
            vis_grid[i][j] = stylized

    print(algorithm_name)
    print("Nodes Explored: {}\nPath Weight: {}".format(len(explored), path_cost))
    if goal_location not in explored:
        print("Goal could not be reached from starting location")
    print()

    for row in vis_grid:
        print('|'.join(row))
    print("\n========================")

if __name__ == "__main__":
    main()
