"""
Burst Balloons:
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it
 represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins.
If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.



Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167


Example 2:
Input: nums = [1,5]
Output: 10



5 2

(1 * 2 * 5 ) + (1 * 5 * 1)
10 + 5 = 15

(1 * 5 * 2) + (1 * 2 * 1)
10 + 2  =12


5 2 1


"""
from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = [1] + nums + [1]
        n = len(nums)
        if n == 1:
            return nums[0]
        elif n == 2:
            return max(
                (1 * nums[0] * nums[1]) + (nums[1]),
                ((nums[0] * nums[1] * 1) + nums[0])
            )
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            try:
                _prev = nums[i - 1]
            except IndexError:
                _prev = 1

            try:
                _next = nums[i + 1]
            except IndexError:
                _next = 1

            dp[i][i] = _prev * nums[i] * _next
        for l in range(2, n + 1):
            for start_index in range(0, n - l + 1):  # 3-2 +1 = 2
                end_index = start_index + l - 1  # 0 + 2 - 1 = 1, 1 + 2 - 1 = 2
                print(f"l={l}, start_index={start_index}, end_index={end_index} - "
                      f"comparing [{start_index - 1},{end_index}]"
                      f" and [{start_index}][{end_index - 1}]")
                # dp[start_index][end_index] = l

                dp[start_index][end_index] = 0
                for k in range(start_index + 1, end_index):
                    dp[start_index][end_index] = max(
                        dp[start_index][end_index],
                        dp[start_index][k] +
                        nums[start_index] * nums[k] * nums[end_index] +
                        dp[k][end_index]
                    )

        return dp[0][n - 1]


if __name__ == '__main__':
    inp = []
    inp = [5]
    # inp = [5,2]
    inp = [5, 2, 1]
    inp = [7, 9, 8, 0, 7, 1, 3, 5, 5, 2, 3]
    inp = [8, 2, 6, 8, 1]

    s = Solution()
    print(s.maxCoins(inp))
