# """
# https://leetcode.com/problems/shortest-bridge/description/
#
# You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
#
# An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
#
# You may change 0's to 1's to connect the two islands to form one island.
#
# Return the smallest number of 0's you must flip to connect the two islands.
#
#
#
# Example 1:
#
# Input: grid = [ [0,1],
# 				[1,0]]
# Output: 1
# Example 2:
#
# Input: grid = [ [0,1,0],
# 				[0,0,0],
# 				[0,0,1]
# 				]
# Output: 2
# Example 3:
#
# Input: grid = [[1,1,1,1,1],
#                [1,0,0,0,1],
#                [1,0,1,0,1],
#                [1,0,0,0,1],
#                [1,1,1,1,1]]
# Output: 1
#
#
# Input: grid = [ [1,0,1],
# 				[0,0,1],
# 				[0,0,1]
# 				]
#
#
# Input: grid = [ [1,0,0],
# 				[0,0,0],
# 				[0,0,1]
# 				]
#
#
#
# Input: grid = [ [1,0,0],
# 				[0,0,0],
# 				[0,0,0],
# 				[0,0,1]
# 				]
#
#
#
#
# Constraints:
#
# n == grid.length == grid[i].length
# 2 <= n <= 100
# grid[i][j] is either 0 or 1.
# There are exactly two islands in grid.
#
#
#
# """
from pprint import pprint
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        island_one = []
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_one.append((i, j))
                    break
            if island_one:
                break
        # get the island one
        print("island_one", island_one)
        visited = {}
        pprint(grid)
        self.bfs(n, island_one, grid, visited)

        print("island_one", island_one, visited)
        pprint(grid)

        steps = 0
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i in range(len(island_one)):
            island_one[i] = (island_one[i][0], island_one[i][1], 0)

        while island_one:
            print("island_one", island_one)
            r, c, step = island_one.pop(0)
            print("r, c, step ", r, c, step)
            visited[(r, c)] = True
            for dr, dc in dirs:
                print(r, dr)
                nr = r + dr
                nc = c + dc

                if (0 <= nr <= n - 1) and (0 <= nc <= n - 1) and (nr, nc) not in visited:
                    if grid[nr][nc] == 1:
                        return step
                    island_one.append((nr, nc, step + 1))
        return -1

    def bfs(self, n, island_one, grid, visited):
        child = [island_one[0]]

        while child:
            r, c = child.pop(0)
            visited[(r, c)] = True
            island_one.append((r, c))
            grid[r][c] = 2
            # left
            try:
                print("check left", r - 1, c)
                if (0 <= r - 1 <= n - 1) and (r - 1 >= 0) and (c <= n - 1) and (r - 1, c) not in visited and \
                        grid[r - 1][c] == 1:
                    child.append((r - 1, c))
            except IndexError as e:
                print(f"Ignore IndexError: list index out of range - {r - 1, c}")

            # right
            try:
                print("check right", r + 1, c)
                if (0 <= r + 1 <= n - 1) and (r + 1, c) not in visited and grid[r + 1][c] == 1:
                    child.append((r + 1, c))
            except IndexError as e:
                print(f"Ignore IndexError: list index out of range - {r + 1, c}")

            # up
            try:
                print("check up", r, c - 1)
                if (0 <= c - 1 <= n - 1) and (r, c - 1) not in visited and grid[r][c - 1] == 1:
                    child.append((r, c - 1))
            except IndexError as e:
                print(f"Ignore IndexError: list index out of range - {r, c - 1}")

            # down
            try:
                print("check down", r, c + 1)
                if (0 <= c + 1 <= n - 1) and (r, c + 1) not in visited and grid[r][c + 1] == 1:
                    child.append((r, c + 1))
            except IndexError as e:
                print(f"Ignore IndexError: list index out of range - {r, c + 1}")


#
# from collections import deque
# from typing import List
#
#
# class Solution:
#     def shortestBridge(self, grid: List[List[int]]) -> int:
#         n = len(grid)
#         queue = deque()
#
#         # Step 1: Find first island
#         found = False
#
#         for i in range(n):
#             if found:
#                 break
#
#             for j in range(n):
#                 if grid[i][j] == 1:
#                     self.dfs(i, j, grid, queue, n)
#                     found = True
#                     break
#
#         # Step 2: Multi-source BFS
#         steps = 0
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
#         while queue:
#
#             for _ in range(len(queue)):
#
#                 r, c = queue.popleft()
#
#                 for dr, dc in directions:
#
#                     nr = r + dr
#                     nc = c + dc
#
#                     if 0 <= nr < n and 0 <= nc < n:
#
#                         # reached second island
#                         if grid[nr][nc] == 1:
#                             return steps
#
#                         # expand into water
#                         if grid[nr][nc] == 0:
#                             grid[nr][nc] = 2
#                             queue.append((nr, nc))
#
#             steps += 1
#
#         return -1
#
#     def dfs(self, r, c, grid, queue, n):
#
#         if r < 0 or c < 0 or r >= n or c >= n:
#             return
#
#         if grid[r][c] != 1:
#             return
#
#         # mark visited
#         grid[r][c] = 2
#
#         # add all first island cells into queue
#         queue.append((r, c))
#
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#
#         for dr, dc in directions:
#             self.dfs(r + dr, c + dc, grid, queue, n)


if __name__ == '__main__':
    grid = [[0, 1], [1, 0]]
    grid = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 1, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]

    grid = [[1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1]]
    obj = Solution()
    print("res = ", obj.shortestBridge(grid))
