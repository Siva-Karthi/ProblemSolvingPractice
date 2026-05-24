"""
Given an integer array nums and an integer k, split nums into k non - empty subarrays such that the largest sum of any
subarray is minimized.

Return the minimized largest sum of the split.

A subarray is a contiguous part of the array.

Example 1:
Input: nums = [7, 2, 5, 10, 8], k = 2
Output: 18

"""
from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        low = max(nums)
        high = sum(nums)
        ans = high

        while low <= high:
            mid = (low + high) // 2

            if self.can_split(nums, mid):
                # optimal_val = current_val
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def can_split(self, nums, max_sum):
        subarrays = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > max_sum:
                subarrays += 1
                current_sum = num
            else:
                current_sum += num

        return subarrays <= k


if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    k = 2
    obj = Solution()
    res = obj.splitArray(nums, k)
    print(f"res = {res}")
