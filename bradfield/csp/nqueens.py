"""
Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""

class PositionManager:
    def __init__(self):
        self.positions = []

    def remove_last(self):
        self.positions.pop()

    def add(self, position):
        self.positions.append(position)

    def valid_placement(self, position):
        """
        check if same column and and in diagonals path
        row already accounted for
        """
        row, col = position

        if self._column_conflict(col):
            return False
        elif self._descending_diagnoal_conflict(row, col):
            return False
        elif self._ascending_diagonal_conflict(row, col):
            return False
        else:
            return True

    def all_queens_placed_for(self, num_queens):
        return len(self.positions) == num_queens

    def get_positions(self):
        return self.positions

    def _ascending_diagonal_conflict(self, row, col):
        return any((row + col) == (position[0] + position[1]) for position in self.positions)

    def _descending_diagnoal_conflict(self, row, col):
        return any((row - col) == (position[0] - position[1]) for position in self.positions)

    def _column_conflict(self, col):
        return any(col == filled_col for filled_col in self._get_cols())

    def _get_cols(self):
        return map(lambda position: position[1], self.positions)

class Solution:
    def solveNQueens(self, num_queens):
        """
        :type n: int
        :rtype: List[List[str]]

        Algorithm
        define base condition where if all queens are placed we have a solution
        check if solution exists starting at first row queen at next column
        """
        solutions = []
        position_manager = PositionManager()
        current_row = 0
        self.solveNQueensUtil(num_queens, solutions, position_manager, current_row)
        return solutions

    def solveNQueensUtil(self, num_queens, solutions, position_manager, current_row):
        if position_manager.all_queens_placed_for(num_queens):
            solutions.append(position_manager.get_positions().copy())
            return True

        for col in range(0, num_queens):
            current_position = (current_row, col)
            if position_manager.valid_placement(current_position):
                position_manager.add(current_position)
                self.solveNQueensUtil(num_queens, solutions, position_manager, current_row + 1)
                position_manager.remove_last()
        return False

solution = Solution()
print(solution.solveNQueens(4))
print(len(solution.solveNQueens(8)) == 92)
