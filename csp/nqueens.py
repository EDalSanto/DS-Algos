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

    def reset_positions(self):
        self.positions = []

    def get_positions(self):
        return self.positions

    def remove_last(self):
        self.positions.pop()

    def add(self, position):
        self.positions.append(position)

    def valid_placement(self, position):
        """
        check same column and diagonals
        row already accounted for
        """
        row, col = position

        if any(col == position[1] for position in self.positions):
            return False
        elif any((row - col) == (position[0] - position[1]) for position in self.positions):
            return False
        elif any((row + col) == (position[0] + position[1]) for position in self.positions):
            return False
        else:
            return True

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]

        Algorithm
        define base condition where if len(positions) == n we have a solution
        check if solution exists starting at first row queen at next column
        """
        solutions = []
        position_manager = PositionManager()
        current_row = 0
        self.solveNQueensUtil(n, solutions, position_manager, current_row)
        return solutions

    def solveNQueensUtil(self, n, solutions, position_manager, current_row):
        if len(position_manager.get_positions()) == n:
            solutions.append(position_manager.get_positions())
            return True
        for col in range(0, n):
            current_position = (current_row, col)
            if position_manager.valid_placement(current_position):
                position_manager.add(current_position)
                solved = self.solveNQueensUtil(n, solutions, position_manager, current_row + 1)
                if solved:
                    return True
                else:
                    position_manager.remove_last()
        return False


solution = Solution()
print(solution.solveNQueens(4))
