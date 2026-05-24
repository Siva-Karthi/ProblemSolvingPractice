# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         if not nums or not k:
#             return None
#
#         n = len(nums)
#
#         if n <= k:
#             return [max(nums)]
#         dq = deque(sorted(range(k), key=lambda i: nums[i]))
#         res = [max(nums[:k])]
#         for i in range(k, n):
#             evict_idx = i - k
#             temp_stk = []
#             # slide through next indices
#             if nums[i] >= nums[dq[-1]]:
#                 dq.append(i)
#                 while dq:
#                     idx = dq.popleft()
#                     if idx == evict_idx:
#                         break
#                     temp_stk.append(idx)
#                 while temp_stk:
#                     dq.appendleft(temp_stk.pop(-1))
#             else:
#                 idx_added = False
#                 while dq:
#                     idx = dq.popleft()
#                     if idx == evict_idx:
#                         break
#                     temp_stk.append(idx)
#                 while temp_stk:
#                     idx = temp_stk.pop(-1)
#                     if not idx_added and nums[i] > nums[idx]:
#                         dq.appendleft(i)
#                         idx_added = True
#                     dq.appendleft(idx)
#                 if not idx_added:
#                     dq.appendleft(i)
#                     idx_added = True
#             res.append(nums[dq[-1]])
#         return res


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        res = []

        for i in range(len(nums)):
            print(dq, [nums[i] for i in dq])
            # remove out-of-window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # remove smaller elements
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    # print(Solution().maxSlidingWindow(nums, k))
    # nums = [1]
    # k = 1
    # print(Solution().maxSlidingWindow(nums, k))
    # nums = [1,-1]
    # k = 1
    # nums = [1, 3, 1, 2, 0, 5]
    # k = 3
    print(Solution().maxSlidingWindow(nums, k))
