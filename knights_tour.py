"""
A knight's tour is a sequence of moves of a knight on a chessboard such that the knight visits every square only once.
If the knight ends on a square that is one knight's move from the beginning square (so that it could tour the board again immediately, following the same path), the tour is closed, otherwise it is open.
"""

def solve(board, initial_position, current_position, path):
    """
    board: a 2D array representing the current board state
    initial_position: an x, y coordinate for where the knight started
    current_position: an x, y coordinate for where the knight currently is
    """
    if all_visited(board):
        print(path)
        return True

    for move in movement_detective(board, current_position):
        current_position = make_move(board, current_position, move)
        path.append(current_position)
        solved = solve(board, initial_position, current_position, path)
        if solved:
            return True
        else:
            path.pop()
            current_position = backtrack(board, current_position, move)

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

def make_move(board, current_position, move):
    """
    Mark current_position + move as True
    Return new_position
    """
    new_x, new_y = current_position[0] + move[0], current_position[1] + move[1]
    board[new_x][new_y] = True
    return (new_x, new_y)

def backtrack(board, current_position, move):
    """
    actiones opposite of make move, but returns current_position still
    """
    new_x, new_y = current_position[0] - move[0], current_position[1] - move[1]
    board[new_x][new_y] = False
    return (new_x, new_y)

def all_visited(board):
    """
    Check if all board has been visited
    """
    return all([boolean for row in board for boolean in row])

def create_board(initial_position):
    board = [[False] * 8 for row in range(8)]

    # Initialize initial position to True
    init_x, init_y = initial_position
    board[0][0] = True

    return board


MOVE_OFFSETS = (
              (-1, -2), ( 1, -2),
    (-2, -1),                     ( 2, -1),
    (-2,  1),                     ( 2,  1),
              (-1,  2), ( 1,  2),
)

initial_position = (0, 0)
current_position = initial_position
board = create_board(initial_position)
path = [(0,0)]
solve(board, initial_position, current_position, path)
