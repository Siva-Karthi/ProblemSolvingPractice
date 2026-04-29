"""
piles = [2,5,7]
h = 6
k = ? (eating k per hour)

2 + 2 + 2
ans = 3 ?

k = 1 to 7
1
2
3
4
5
6
7


"""

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        mid = high
        optimal_k = mid

        while low <= high:
            mid = (low + high) // 2
            if self.isValid(piles, mid, h):
                optimal_k = mid
                high = mid - 1
            else:
                low = mid + 1
        return optimal_k

    def isValid(self, piles, mid, h):
        h_needed = 0
        for pile in piles:
            h_needed += math.ceil(pile / mid)
        return h_needed <= h


if __name__ == '__main__':
    obj = Solution()

    # piles = [2, 5, 7]
    # h = 6

    piles = [30, 11, 23, 4, 20]
    h = 6
    print(obj.minEatingSpeed(piles=piles, h=h))
