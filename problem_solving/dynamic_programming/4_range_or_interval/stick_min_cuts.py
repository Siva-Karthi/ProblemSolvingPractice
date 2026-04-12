# import math
# from pprint import pprint
# from typing import List
# import bisect
#
#
# class Solution:
#     def minCost(self, n: int, cuts: List[int]) -> int:
#
#         if not cuts:
#             return 0
#
#         # 🔥 ONLY IMPORTANT FIX #1: add boundaries
#         cuts = [0] + sorted(cuts) + [n]
#         m = len(cuts)
#
#         # DP over cut indices
#         dp = [[math.inf for _ in range(m)] for _ in range(m)]
#
#         # base case
#         for i in range(m - 1):
#             dp[i][i + 1] = 0
#
#         def get_cuts_in_range(l, r):
#             left = bisect.bisect_right(cuts, l)
#             right = bisect.bisect_left(cuts, r)
#             return cuts[left:right]
#
#         # 🔥 interval DP (your same structure idea)
#         for l in range(2, m):
#             for i in range(m - l):
#                 j = i + l
#
#                 possible_cuts = get_cuts_in_range(cuts[i], cuts[j])
#
#                 for k in possible_cuts:
#
#                     stick_len = cuts[j] - cuts[i]   # FIXED (correct cost)
#
#                     cost = stick_len
#
#                     ki = cuts.index(k)  # minimal necessary mapping fix
#
#                     cost += dp[i][ki] + dp[ki][j]
#
#                     dp[i][j] = min(dp[i][j], cost)
#
#         return dp[0][m - 1]
#
#
# if __name__ == '__main__':
#     n = 7
#     cuts = [1, 3, 4, 5]
#     obj = Solution()
#     print(obj.minCost(n, cuts))
from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        # Add boundary points and sort
        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)

        # dp[i][j] = minimum cost to cut between cuts[i] and cuts[j]
        dp = [[0] * m for _ in range(m)]

        # Build up from shorter segments to longer ones
        # length = j - i
        for length in range(2, m):  # at least 2 apart to have a cut in between
            for i in range(m - length):
                j = i + length
                best = float('inf')
                # Try all possible intermediate cuts
                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j] + (cuts[j] - cuts[i])
                    best = min(best, cost)
                dp[i][j] = best

        return dp[0][m - 1]
