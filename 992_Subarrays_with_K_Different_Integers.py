"""
https://leetcode.com/problems/subarrays-with-k-different-integers/description/

992. Subarrays with K Different Integers

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.



Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i], k <= nums.length



"""

from typing import List


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        cnt = 0
        n = len(nums)
        res = []
        for strt in range(0, n + 1 - k):
            # print("start", strt)
            sub_l = k
            subset = set()
            while sub_l <= n and strt + sub_l <= n:
                subset = set(nums[strt:strt + sub_l])
                if len(subset) > k:
                    break
                if len(subset) == k:
                    # print("\tsub_l", sub_l, nums[strt:strt + sub_l])
                    cnt += 1
                    res.append(nums[strt:strt + sub_l])
                sub_l += 1

        # print("res", res)
        return cnt


if __name__ == '__main__':
    obj = Solution()
    nums = [1, 2, 1, 3, 4]
    k = 3
    print(obj.subarraysWithKDistinct(nums, 3))
