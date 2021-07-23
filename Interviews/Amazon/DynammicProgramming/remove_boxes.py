# def remove_boxes(input):
#     """
#     start with 0
#         check consecutive numbers, if changed keep occurance and end
#         if ended:
#             profit = max(profit ,occ * occ)
#         else:
#             profit = max(profit, (0, end), (end, len), occ * occ)
#
#     :param input:
#     :return:
#     """
#     if len(input) == 0:
#         return 0
#     elif len(input) == 1:
#         return 1
#
#     profit = 0
#     start = 0
#     end = 0
#     while start < len(input):
#         consec_occurance = 0
#         while (end < len(input)) and (input[start] == input[end]):
#             end +=1
#             consec_occurance +=1
#
#         if end == len(input):
#             profit = max(profit, consec_occurance*consec_occurance)
#         else:
#             profit = max(
#                 profit,
#                 consec_occurance * consec_occurance,
#                 remove_boxes(input[0:start]),
#                 remove_boxes(input[end:len(input)])
#             )
#
#         start = end
#     return profit
from pprint import pprint
from typing import List


class Solution:
    def remove_boxes(self, boxes: List[int]) -> int:
        #Define DP
        n = len(boxes)
        dp = [[[0] * n for _ in range(n)] for _ in range(n)]

        def cacl_point(boxes, l, r, k):
            """"
            Calculate points
            Args:
            Boxes: sequences
            l: The starting position of the sequence
            r: The end of the sequence
            k: Number of boxes with the same color as boxes [R] after r
            Returns:
            Returns the maximum integral of the strategy in the sequence
            """
            if l > r:
                return 0

            #Prevent double counting
            if dp[l][r][k] != 0:
                return dp[l][r][k]

            #First find the box with the same color as boxes [R]
            while l < r and boxes[r] == boxes[r-1] :
                r -= 1
                k += 1

            #Strategy 1 (see article for description)
            dp[l][r][k] = cacl_point(boxes, l, r-1, 0) + (k+1)*(k+1)
            #Strategy 2 (see article for description)
            for x in range(l, r-1):
                if boxes[x] == boxes[r]:
                    #Here, the larger value is directly compared to maintain and update
                    dp[l][r][k] = max(dp[l][r][k], cacl_point(boxes, x+1, r-1, 0)+cacl_point(boxes, l, x, k+1))
            pprint(dp)
            pprint("-----")
            return dp[l][r][k]
        return cacl_point(boxes, 0, n-1, 0)

if __name__ == '__main__':
    input = [1,3,2,3,3] # 6
    # max_profit = remove_boxes(input)
    max_profit = Solution().remove_boxes(input)
    print("max_profit for input {} is {}".format(input, max_profit))