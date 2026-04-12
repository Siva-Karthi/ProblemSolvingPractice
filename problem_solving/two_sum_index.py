"""

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]


nums = [2, 7, 11, 15]
target = 13
obj = Solution()
res = obj.twoSum(nums, target)
print(res)


# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?


class OptimizedSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        sorted_arr = [i for i in nums]
        sorted(sorted_arr)
        index_map = {}
        for i in range(n):
            index_map[nums[i]] = i
        i = 0
        j = n - 1
        while i < j:
            temp_sum = sorted_arr[i] + sorted_arr[j]
            if temp_sum == target:
                return [index_map[sorted_arr[i]], index_map[sorted_arr[j]]]
            elif temp_sum > target:
                j -= 1
            else:
                i += 1


obj = OptimizedSolution()
res = obj.twoSum(nums, target)
print(res)


def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i


res = twoSum(nums, target)
print(res)
