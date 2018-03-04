"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
"""

def min_path_sum(triangle):
    last_min_idx = 0
    min_sum = triangle[0][0]
    for row in triangle[1:]:
        if row[last_min_idx] <= row[last_min_idx + 1]:
            min_sum += row[last_min_idx]
        else:
            min_sum += row[last_min_idx + 1]
            last_min_idx += 1

    return min_sum


print(min_path_sum([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]) == 11)

print(min_path_sum([[-1],[2,3],[1,-1,-3]]) == -1)
