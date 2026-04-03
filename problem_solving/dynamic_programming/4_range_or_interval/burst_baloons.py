# """
#
# https://leetcode.com/problems/burst-balloons/description/
#
# You are given n balloons, indexed from 0 to n - 1.
# Each balloon is painted with a number on it represented by an array nums.
# You are asked to burst all the balloons.
#
# If you burst the ith balloon,
# you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
# If i - 1 or i + 1 goes out of bounds of the array,
# then treat it as if there is a balloon with a 1 painted on it.
#
# Return the maximum coins you can collect by bursting the balloons wisely.
#
#
#
# Example 1:
# [3,5]
#
# max(15 + 5 , 15 +3) =   20
#
# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
# Example 2:
#
# Input: nums = [1,5]
# Output: 10
# """
from pprint import pprint
from typing import List


#
#
# class Solution:
#     def maxCoins(self, nums: List[int]) -> int:
#         # base case
#         if not nums:
#             return 0
#         elif len(nums) == 1:
#             return nums[0]
#         elif len(nums) == 2:
#             return nums[0] * nums[1]
#         padded_nums = [1] + nums + [1]
#         n = len(padded_nums)
#         dp = [[0 for i in range(n)] for i in range(n)]
#         """
#         for each length 1 to n
#             solve the sub problem to maximize the coins of the cur length
#                 by making use of the solved sub problems thats it
#
#         """
#         for i in range(n):
#             dp[i][i] = padded_nums[i]
#         from pprint import pprint
#         pprint(dp)
#         # solve for the len 2 to n of the input nums
#         for l in range(2,n):
#             for i in range(0, n - l + 1 ): # 0 - 2 (0,1) , (1,2), (2,3)
#                 start = i
#                 end = start + l - 1
#                 dp[start][end] = 0
#                 # maximize
#                 for k in range(start,end+1):
#                     # consider each k is getting burst at last
#                     res = dp[k+1][end] *  padded_nums[k] *  dp[start][k-1]
#                     dp[start][end] = max(dp[start][end], res)
#
#         pprint(dp)
#         return dp[1][n-2]
#
#
#
#
#

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # base case
        if not nums:
            return 0
        # elif len(nums) == 1:
        #     return nums[0]
        # elif len(nums) == 2:
        #     return nums[0] * nums[1]
        padded_nums = [1] + nums + [1]
        print(padded_nums)
        n = len(padded_nums)
        dp = [[0 for i in range(n)] for i in range(n)]
        for i in range(n):
            dp[i][i] = padded_nums[i]
        pprint(dp)
        for length in range(2, n):
            print(f"\t {length}")
            for i in range(n - length):
                print(f"\t\t start = {i}")
                j = i + length  # 0-2
                print(f"\t\t end = {j}")

                for k in range(i + 1, j):
                    print(f"\t\t\t k = {k}")
                    print(f"\t\t\t check current = {dp[i][j]}")
                    print(f"\t\t\t check sub dp[{i}][{k}] = {dp[i][k]}")
                    print(f"\t\t\t check cost padded_nums[i] * padded_nums[k] * padded_nums[j] -"
                          f" dp[{i}][{k}] + padded_nums[{i}]* padded_nums[{k}] * padded_nums[{j}] + dp[{k}][{j}]  = {dp[i][k] + padded_nums[i] * padded_nums[k] * padded_nums[j] + dp[k][j]}")
                    print(f"\t\t\t check sub dp[{k}][{j}] = {dp[k][j]}")

                    # coins = (dp[i][k] +
                    #          (padded_nums[i] * padded_nums[k] * padded_nums[j]) +
                    #          dp[k][j])
                    #
                    # dp[i][j] = max(dp[i][j], coins)

                    # dp[i][j] = max(dp[i][j],
                    #                dp[i][k-1] +
                    #                dp[i][k-1] * padded_nums[k] * dp[k+1][j]
                    #                + dp[k+1][j]
                    #                )
                    dp[i][j] = max(dp[i][j],
                                   dp[i][k] +
                                   padded_nums[i] * padded_nums[k] * padded_nums[j]
                                   + dp[k][j]
                                   )
        pprint(dp)
        return dp[0][n - 1]


if __name__ == '__main__':
    # nums = [3,1,5,8]
    nums = [3, 5]
    obj = Solution()
    res = obj.maxCoins(nums)
    print(res)
