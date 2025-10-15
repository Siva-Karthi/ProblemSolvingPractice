"""
Given a N*N board with the Knight placed on the first block of an empty board.
Moving according to the rules of chess knight must visit each square exactly once.
Print the order of each cell in which they are visited.
"""


class Solution:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        """
        check the start index if not 0  - return False
        maintain current  i-th move starting 0
        check all  possibilites (8) and
        if not any one is matching the step return false
            if anyone if negative - immediately return false
        """

        n = len(grid)

        if n < 3:
            return False
        elif grid[0][0] != 0:
            return False

        res = self.helper(grid, n, 0, 0, step=0)
        return res

    def helper(self, grid, n, r=0, c=0, step=0):
        print("\n\n")
        next_r, next_c = None, None
        possibilities = []
        x = [2, 2, -2, -2, 1, 1, -1, -1]
        y = [1, -1, 1, -1, 2, -2, 2, -2]
        for i in range(8):
            if (x[i] + r < n) and (x[i] + r > 0) and (y[i] + c < n) and (y[i] + c > 0):
                possibilities.append((x[i] + r, y[i] + c))

        # base case - stop iteration
        if step == n * n:
            return True
        print("possibilities for", r, c, "are ", possibilities)
        for x, y in possibilities:
            print("current step = ", step, " next = ", step + 1, "but got", grid[y][x], "at", y, x, "\n")
            if grid[y][x] == step + 1:
                next_r = x
                next_c = y
            elif grid[y][x] < 0:  # case - invalid config
                print("return in # case - invalid config ")
                return False
        # case - invalid config
        if next_r == None or next_c == None:
            print("return in next")
            return False
        return self.helper(grid, n, next_r, next_c, step + 1)
# link - https://leetcode.com/problems/check-knight-tour-configuration/
