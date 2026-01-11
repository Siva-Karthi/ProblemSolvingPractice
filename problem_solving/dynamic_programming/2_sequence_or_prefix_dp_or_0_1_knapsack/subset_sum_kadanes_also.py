"""

Given an array nums[], find the maximum sum of a contiguous subarray.

⚡ Important: subarray must be contiguous (unlike subset).

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Best subarray = [4, -1, 2, 1]
Sum = 6
"""


# def kadane(nums):
#     n = len(nums)
#     dp = [0] * n
#     dp[0] = nums[0]
#
#     for i in range(1, n):
#         if dp[i-1] + nums[i] > nums[i]:
#             dp[i] = dp[i-1] + nums[i]
#         else:
#             dp[i] = nums[i]
#
#     return max(dp)

def kadane(nums):
    n = len(nums)
    res = nums[0]
    last = nums[0]
    for i in range(1, n):
        last = max(last + nums[i], nums[i])
        res = max(res, last)
    return res


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(kadane(nums))
