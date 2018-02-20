# Implementing Graph Search On A Grid

In this exercise you'll implement several versions of graph search in a simple maze, represented by a 2D grid. The grid has 3 kinds of squares: normal, trees, and walls. Wall squares cannot be traveled to, normal squares can be traveled to at a cost of 1, and trees can be traveled to at a cost of 2. Finally, there are two special values which occur exactly once each, and are always "normal" squares: the start and goal. Consider one such maze:

* S == Start
* G == Goal
* N == Normal
* T == Tree
* W == Wall

```
grid_world = [
 [S, N, N, N],
 [N, W, W, W],
 [N, T, T, T],
 [N, N, N, G]
]
```
> This maze is 4x4, and the "shortest path" is to go down 3 times, then left 3 times, avoiding all the trees in the 3rd row.

The goal of this exercise is to build and compare simple implementations of DFS, Dijkstra's Algorithm and A* over such grids. A sample implementation of BFS is provided for you.

## Getting Started

Several functions have been provided for you (mostly related to printing results), but they are worth reading before you start. In particular, examine the `get_successor_states` function -- this function accepts a grid (2D list) and a `(row, col)` tuple, and returns a list of `(row, col)` tuples; each tuple represents a neighboring square that can be reached from the input square. The `visualize_result` function prints a textual representation of the result of performing a search, as reconstructed from the `explored_list` that was created during the search process (and which must be returned by your implementations).

If you run the script it will attempt your implementations of graph search and visualize the results. If any implementations are not complete it will throw an error when trying to run that function. For example if you run the python script on the incomplete handout you will see:

```
python3 graph-search-incomplete.py
BFS
Nodes Explored: 16
Path Weight: 6

O| | |
o|#|#|#
o|^|^|^
o|o|o|O

========================
Traceback (most recent call last):
  File "graph-search-incomplete.py", line 209, in <module>
    main()
  File "graph-search-incomplete.py", line 16, in main
    little_world()
  File "graph-search-incomplete.py", line 91, in little_world
    compare(grid_world, starting_point, goal_point)
  File "graph-search-incomplete.py", line 132, in compare
    explored = DFS(grid_world, starting_point)
  File "graph-search-incomplete.py", line 71, in DFS
    raise NotImplementedError()
NotImplementedError
```

The output tells us that our implementation of BFS on the `little_world` grid found a path from start to goal by first traveling down 3 times, until it reached the edge; then it went right three times to the goal. The `o` character is a part of the path which did not pass through a tree, the `ô` character will appear if a part of the path did pass through a tree. For squares that were not a part of the solution `#` is a wall, `^` is a tree and a space indicates a normal square.

The Nodes Explored: 16 tells us that 16 nodes were explored before we found the goal node. Given that our grid is 4x4 == 16 nodes, this is not a very efficient search, we considered every possible square.

Your implementations of DFS, Dijkstras, and A* can function internally however you wish, but for the compare and visualize functions to work properly, they must all return an explored list the explored list in a particular format. The explored list must be a dictionary where the keys are `(row, col)` tuples, and the values are also `(row, col)` tuples such that the keys represent a grid square, and the values represent the square from which the value was reached. For example, in this simple grid world:

```
[['S', ' ', 'G']]
```

The explored list would contain three entries:

```
{
  (0,0): None,  # The starting location has no parent location
  (0,1): (0,0), # The location (0,1) was reached from the location (0,0)
  (0,2): (0,1)  # The goal location (0,2) was reached from the middle square (0,1)
}
```

As a guide, our reference solution produces the following output for the `big_world`, (it's fun to note the absurd path that DFS produced):

```
BFS
Nodes Explored: 32
Path Weight: 15

O|ô|ô|ô|#|O
 |^|^|ô|#|o
 |#|^|ô|ô|o
 | | | |^|
 |^| | | |
 |^| | | |

========================
DFS
Nodes Explored: 30
Path Weight: 41

O|ô|ô|ô|#|O
o|ô|ô|ô|#|o
o|#|ô|ô|ô|o
o|o|o|o|ô|
o|ô|o|o|o|
o|ô|o|o|o|

========================
Dijkstra's
Nodes Explored: 34
Path Weight: 12

O|^|^|^|#|O
o|^|^|^|#|o
o|#|^|^|^|o
o|o|o|o|ô|o
 |^| | | |
 |^| | | |

========================
A-Star
Nodes Explored: 21
Path Weight: 12

O|^|^|^|#|O
o|^|^|^|#|o
o|#|^|^|^|o
o|o|o|o|ô|o
 |^| | | |
 |^| | | |

========================
```

Finally, in main there is a commented out `random_world` function which will randomly generate grids. When your implementations are working, try visualizing the results on a few random worlds and comparing their behavior!
