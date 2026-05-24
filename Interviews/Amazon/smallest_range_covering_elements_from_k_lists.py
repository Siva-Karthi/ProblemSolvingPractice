"""
https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/description/


632. Smallest Range Covering Elements from K Lists
Hard
Topics
premium lock icon
Companies
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.



Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation:
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].
Example 2:

Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
Output: [1,1]


Constraints:

nums.length == k
1 <= k <= 3500
1 <= nums[i].length <= 50
-105 <= nums[i][j] <= 105
nums[i] is sorted in non-decreasing order.

"""

import heapq
import math
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        hp = [(nums[i][0], i, 0) for i in range(len(nums))]
        mx = max([i[0] for i in nums])
        mn = -1
        b_mx = -1
        heapq.heapify(hp)
        glbl_rnge = math.inf
        while True:
            hp_elem = heapq.heappop(hp)
            cur_mn = hp_elem[0]
            nums_idx = hp_elem[1]
            elem_idx = hp_elem[2]

            lcl_rnge = mx - cur_mn

            if lcl_rnge < glbl_rnge:
                glbl_rnge = lcl_rnge
                mn = cur_mn
                b_mx = mx

            # try shrinking
            try:
                nxt_mn = nums[nums_idx][elem_idx + 1]
                heapq.heappush(hp, (nxt_mn, nums_idx, elem_idx + 1))
                if nxt_mn > mx:
                    mx = nxt_mn
            except IndexError as e:
                break

        return [mn, b_mx]


if __name__ == '__main__':
    # nums = [[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]]
    nums = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
    obj = Solution()
    print(obj.smallestRange(nums))
