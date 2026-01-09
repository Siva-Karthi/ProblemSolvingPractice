#!/bin/python3


#
# Complete the 'reachTheEnd' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER maxTime
#

def reachTheEnd(grid, maxTime):
    n = len(grid)
    # base validations - n vs maxTime
    if maxTime < n:
        return 'No'

    visited = [[0 for _ in range(n)] for _ in range(n)]
    return traverse_helper(grid, maxTime, visited, 0, 0, 0, n)


def traverse_helper(grid, maxTime, visited, x, y, cur_time, n):
    """
    explore each option
        select the current option
        validate the constraint
            if satisfied
                return 'Yes'
        unselect the current option
    return 'No'
    """

    # validate the constraints
    print(x, y)
    if x == n - 1 and y == n - 1:
        if cur_time <= maxTime:
            return 'Yes'
        else:
            return 'No'
    # if x < 0 or y < 0 or x >= n or y >= n:
    #     return

    if visited[x][y] == 0:
        visited[x][y] = 1
        # explore each option
        # top
        if y - 1 > 0 and y - 1 <= n - 1:
            traverse_helper(grid, maxTime, visited, x, y - 1, cur_time + 1, n)
            visited[x][y - 1] = 0
        # left
        if x - 1 > 0 and x - 1 <= n - 1:
            traverse_helper(grid, maxTime, visited, x - 1, y, cur_time + 1, n)
            visited[x - 1][y] = 0
        # right
        if x + 1 > 0 and x + 1 <= n - 1:
            traverse_helper(grid, maxTime, visited, x + 1, y, cur_time + 1, n)
            visited[x + 1][y] = 0
        # bottom
        if y + 1 > 0 and y + 1 <= n - 1:
            traverse_helper(grid, maxTime, visited, x, y + 1, cur_time + 1, n)
            visited[x][y + 1] = 0

    # return 'No'


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # grid_count = int(input().strip())
    #
    # grid = []
    #
    # for _ in range(grid_count):
    #     grid_item = input()
    #     grid.append(grid_item)
    #
    # maxTime = int(input().strip())
    #
    # result = reachTheEnd(grid, maxTime)
    #
    # fptr.write(result + '\n')
    #
    # fptr.close()
    grid = [['.', '.'],
            ['.', '.']]
    maxTime = 3
    print(reachTheEnd(grid, maxTime))
