# Compute number of shortest paths from top left to bottom right

def num_paths_recursive(height, width):
    """
    same problem of fib with O(2^N) time complexity and O(N) space
    """
    # Straight line can only ever have 1
    if height == 0 or width == 0:
        return 1
    else:
        return num_paths_recursive(height - 1, width) + num_paths_recursive(height, width - 1)

print(num_paths_recursive(2, 2) ==  6)

"""
Initial State
[
    [ 1, 1, 1 ],
    [ 1, 1, 1 ],
    [ 1, 1, 1 ],
]
Final State
[
    [ 1, 1, 1 ],
    [ 1, 2, 3 ],
    [ 1, 3, 6 ]
]
"""
def num_paths_dynamic(height, width):
    """
    solve subproblems of number of points to the left and above to derive how many paths to point
    left and top points by definition of problem have only 1 path to them
    """
    # Create matrix of height by width
    memo = [ [1] * (width + 1) for _ in range(height + 1) ]
    for row_idx, row in enumerate(memo):
        for col_idx, col in enumerate(row):
            # Skip leftmost col and top most row
            if row_idx == 0 or col_idx == 0:
                continue
            else: # Add top and left points
                memo[row_idx][col_idx] = memo[row_idx][col_idx - 1] + memo[row_idx - 1][col_idx]
    return memo[-1][-1]

print(num_paths_dynamic(2, 2) == 6)
