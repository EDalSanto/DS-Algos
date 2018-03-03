"""
A knight's tour is a sequence of moves of a knight on a chessboard such that the knight visits every square only once.
If the knight ends on a square that is one knight's move from the beginning square (so that it could tour the board again immediately, following the same path), the tour is closed, otherwise it is open.

This solution below currently runs in O(k^n) time where k is the average branching factor and n is the number of squares on the board. Space complexity O(n^2) where n is the size of the board.
TODO Time complexity can be improved greatly by introducing a heuristic that priotizes moves with the fewest subsequent legal moves.
"""

def solve(board, path):
    """
    board: a 2D array representing the current board state
    path: spots visited along board starting with init
    """
    if all_visited(board):
        print(path)
        return True

    for move in movement_detective(board, path[-1]):
        make_move(board, path, move)
        solved = solve(board, path)
        if solved:
            return True
        else:
            backtrack(board, path)

    return False

def movement_detective(board, current_position):
    """
    Find all possible moves as offsets from current_position for knight
    """
    def legal_move_detective(offset):
        row_offset, col_offset = offset
        cur_x, cur_y = current_position
        move_x, move_y = cur_x + row_offset, cur_y + col_offset

        if 0 <= move_x < len(board) and 0 <= move_y < len(board):
            if not board[move_x][move_y]:
                return True
        else:
            return False

    return filter(legal_move_detective, MOVE_OFFSETS)

def make_move(board, path, move):
    """
    Mark current_position + move as True
    Return new_position
    """
    current_position = path[-1]
    new_x, new_y = current_position[0] + move[0], current_position[1] + move[1]
    board[new_x][new_y] = True
    path.append((new_x, new_y))

def backtrack(board, path):
    """
    actiones opposite of make move, but returns current_position still
    """
    x, y = path.pop()
    board[x][y] = False

def all_visited(board):
    """
    Check if all board has been visited
    """
    return all([boolean for row in board for boolean in row])

def create_board(initial_position, size):
    board = [[False] * size for row in range(size)]

    # Initialize initial position to True
    init_x, init_y = initial_position
    board[init_x][init_y] = True

    return board


MOVE_OFFSETS = (
              (-1, -2), ( 1, -2),
    (-2, -1),                     ( 2, -1),
    (-2,  1),                     ( 2,  1),
              (-1,  2), ( 1,  2),
)

initial_position = (0, 0)
current_position = initial_position
board = create_board(initial_position, 5)
path = [initial_position]
solve(board, path)
