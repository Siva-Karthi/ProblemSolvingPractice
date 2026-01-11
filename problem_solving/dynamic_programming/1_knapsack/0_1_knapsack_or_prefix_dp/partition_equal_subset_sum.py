"""
Partition Equal Subset Sum: Can you split an array into two subsets such that the sum of elements in both subsets is equal?
"""
from typing import List


class Solution:
    # def canPartition(self, nums: List[int]) -> bool:
    #     """
    #     solution
    #         going to calc the subset sum for the total array sum / 2 which is the target sum.
    #         If able to get a subset to the target sum.
    #         Then, its proved that there exist another subset with the target sum and return True else False
    #     """
    #     n = len(nums)
    #     total = sum(nums)
    #     # If the total sum is odd, we can never split it into two equal integers
    #     if total % 2 != 0:
    #         return False
    #
    #     target_sum = total // 2
    #     dp = [[0 for i in range(target_sum + 1 )] for i in range(n + 1)]
    #
    #     for i in range(1, n + 1):
    #         curr = nums[i - 1]
    #         for j in range(1, target_sum + 1):
    #             # Option A: Don't take the number
    #             res = dp[i - 1][j]
    #
    #             # Option B: Take the number (if it fits in current capacity j)
    #             if curr <= j:
    #                 # We take curr + whatever the best was for the REMAINING capacity (j - curr)
    #                 res = max(res, curr + dp[i - 1][j - curr])
    #
    #             dp[i][j] = res
    #
    #     if dp[-1][-1] == target_sum:
    #         return True
    #     else:
    #         return False

    # space optimised
    # def canPartition(self, nums: List[int]) -> bool:
    #     """
    #     solution
    #         going to calc the subset sum for the total array sum / 2 which is the target sum.
    #         If able to get a subset to the target sum.
    #         Then, its proved that there exist another subset with the target sum and return True else False
    #     """
    #     n = len(nums)
    #     total = sum(nums)
    #     # If the total sum is odd, we can never split it into two equal integers
    #     if total % 2 != 0:
    #         return False
    #
    #     target_sum = total // 2
    #     last =  [0 for i in range(target_sum + 1 )]
    #     latest = [0 for i in range(target_sum + 1 )]
    #
    #     for i in range(1, n + 1):
    #         curr = nums[i - 1]
    #         for j in range(1, target_sum + 1):
    #             # Option A: Don't take the number
    #             res = last[j]
    #
    #             # Option B: Take the number (if it fits in current capacity j)
    #             if curr <= j:
    #                 # We take curr + whatever the best was for the REMAINING capacity (j - curr)
    #                 res = max(res, curr + last[j - curr])
    #
    #             latest[j] = res
    #         last = list(latest)
    #     if latest[-1] == target_sum:
    #         return True
    #     else:
    #         return False

    # space further optimised - use same row but use backward iteration as the values are getting updated the current values would be corrupted while check the same value for the upcoming values those would receive new value

    """
    explain The Fix: Iterate Backwards mpore clearly with some diagrams

To understand why we iterate backwards, you have to visualize how the 1D array (dp) behaves like a "memory" of the previous row.

The "Overwriting" Problem (Forward Iteration)
When you iterate forwards, you update values in the array and immediately use those newly updated values for the rest of the same row. This is what caused your code to use the number 2 twice to reach the sum 4.

Imagine we are processing the number 2 with a target of 4:

Initial state: dp = [T, F, F, F, F] (Indices 0, 1, 2, 3, 4)

At j=2: We see dp[2-2] is True. We update dp[2] to True.

At j=4: We look at dp[4-2]. Because we just updated index 2 to True, index 4 now becomes True.

This effectively says: "I used a 2 to get to sum 2, and then I used another 2 to get from sum 2 to sum 4."

The Fix: Backwards Iteration
When you iterate backwards, you look "to your left" at values that have not been updated yet. They are still "old" values from the previous item.

Let's look at the same example (curr = 2) but moving backwards:

Initial state: dp = [T, F, F, F, F] (Indices 0, 1, 2, 3, 4)

At j=4: We check dp[4-2]. Index 2 is currently False (it hasn't been touched yet). Index 4 stays False.

At j=2: We check dp[2-2]. Index 0 is True. Index 2 becomes True.

By the time we updated index 2, we had already finished checking index 4. The "new" information didn't have a chance to leak into larger sums. This guarantees each number is used exactly once.

Summary of the Logic
Backwards: You are looking at the "Previous Row" (0/1 Knapsack).

Forwards: You are looking at the "Current Row" (Unbounded Knapsack).

    """

    def canPartition(self, nums: List[int]) -> bool:
        """
        solution
            going to calc the subset sum for the total array sum / 2 which is the target sum.
            If able to get a subset to the target sum.
            Then, its proved that there exist another subset with the target sum and return True else False
        """
        n = len(nums)
        total = sum(nums)
        # If the total sum is odd, we can never split it into two equal integers
        if total % 2 != 0:
            return False

        target_sum = total // 2
        dp = [0 for i in range(target_sum + 1)]

        for i in range(1, n + 1):
            curr = nums[i - 1]
            # for j in range(1, target_sum + 1):
            for j in range(target_sum, curr - 1, -1):
                # Option A: Don't take the number
                res = dp[j]

                # Option B: Take the number (if it fits in current capacity j)
                if curr <= j:
                    # We take curr + whatever the best was for the REMAINING capacity (j - curr)
                    res = max(res, curr + dp[j - curr])

                dp[j] = res
        return dp[target_sum] == target_sum


if __name__ == '__main__':
    inp = [1, 5, 11, 5]
    # inp = [3, 3, 3, 4, 5]
    # inp = [1,2,5]

    print(Solution().canPartition(inp))

# optimised
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total = sum(nums)
#         if total % 2:
#             return False
#
#         target = total // 2
#         possible = 1  # bit i==1 means sum i is achievable
#
#         # keep only the bits up to target to avoid unnecessary growth
#         mask = (1 << (target + 1)) - 1
#         for num in nums:
#             possible |= possible << num  # add num to every previously achievable sum
#             if possible >> target & 1:  # early exit when target is already reachable
#                 return True
#
#                 possible &= mask
#
#         return False

# Another variation
# k equal subset
