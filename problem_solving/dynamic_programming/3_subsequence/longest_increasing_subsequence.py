"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: [2,3,7,101]
"""


def lis(nums):
    n = len(nums)
    dp = [1 for i in range(n)]
    max_len = 1
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
        max_len = max(max_len, dp[i])
    return max_len


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(lis(nums))

# optimization of runtime from O(n^2) to O(n log n)
