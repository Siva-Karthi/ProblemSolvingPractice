#
#
#
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # handle base cases
#         if not list:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         elif len(nums) == 2:
#             return nums[0] if nums[0] > nums[1] else nums[1]
#         n = len(nums)
#         dp = [0 for i in range(n)]
#         dp[0] = nums[0]
#         dp[1] = nums[1]
#         for i in range(2,n):
#             temp = 0
#             for j in range(0, i-1):
#                 if dp[j] + nums[i] > temp:
#                     temp = dp[j] + nums[i]
#             dp[i] = max(dp[i-1],temp)
#
#         return dp[-1]
from typing import List


#
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         # handle base cases
#         if not list:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         elif len(nums) == 2:
#             return nums[0] if nums[0] > nums[1] else nums[1]
#         n = len(nums)
#         dp = [0 for i in range(n)]
#         dp[0] = nums[0]
#         # dp[1] = nums[1]
#         dp[1] = max(nums[0], nums[1])
#         for i in range(2,n):
#             dp[i] = max(dp[i-1],dp[i-2]+nums[i])
#         return dp[-1]


class Solution:
    def rob(self, nums: List[int]) -> int:
        # handle base cases
        if not list:
            return 0
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return nums[0] if nums[0] > nums[1] else nums[1]
        n = len(nums)
        second_last = nums[0]
        last = max(nums[0], nums[1])
        res = 0
        for i in range(2, n):
            res = max(last, second_last + nums[i])
            second_last = last
            last = res
        return res
