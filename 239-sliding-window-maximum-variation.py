from collections import deque


class Solution:
    def minSlidingWindow(self, nums, k):
        dq = deque()
        res = []
        for i in range(len(nums)):
            """
            remove out of scope candidates from front
            add current candidate but just before that elminate candidate which are not fit from rear
            """
            while dq and dq[0] <= i - k:
                dq.popleft()
            while dq and nums[dq[-1]] >= nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k - 1:
                res.append(nums[dq[0]])
        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    res = Solution().minSlidingWindow(nums, k)
    print(res)
    assert res == [-1, -3, -3, -3, 3, 3]
    # print(Solution().maxSlidingWindow(nums, k))
    # nums = [1]
    # k = 1
    # print(Solution().maxSlidingWindow(nums, k))
    # nums = [1,-1]
    # k = 1
    # nums = [1, 3, 1, 2, 0, 5]
    # k = 3
