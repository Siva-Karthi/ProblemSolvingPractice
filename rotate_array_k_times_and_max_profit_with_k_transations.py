import math

"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


[1,2,3,4,]
5,6,7->1,2,3,4



1 -> 2 -> 3 -> 4-> 5 -> 6 -> 7->



head = 6
tail = 5

k - times
    6 -> 7-> 1 -> 2 -> 3 -> 4-> 5 ->

    5 -> 6 -> 7 -> 1 -> 2 -> 3 -> 4->

    n = 7
    k = 1000

    rot = k % n

"""


# LL node
class Node():
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


def rotate(arr, k):
    n = len(arr)
    res = []
    # todo : handle base cases

    # build doubly ll
    head = Node()
    prev = head  # todo : make sure head not changed
    for i in arr:
        node = Node(i)
        prev.next = node
        node.prev = prev
        prev = node

    tail = prev
    # rotate  head k times
    for i in range(k % n):
        # head  6
        # tail  5

        # head manipulation
        new_head = tail
        new_head.next = head
        new_head.prev = None
        head.prev = new_head
        head = new_head

        # manipulate tail
        new_tail = tail.prev
        new_tail.next = None
        tail = new_tail

    # make kth node as a new head # todo: is it necessary to do k iterations especially when k is large

    # build res array from ll
    node = head
    while node:
        res.append(node.val)
        node = node.next
    return res


"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


  7  1  5  3  6  4
1 0  0  0  0  0  0 
2 0 -6  4  2  

max(dp[i][j-1], max(past each buy and selling today) )  
max(4, max(-4, 2, -2))
max(4, 2)
"""


def max_profit(stock_prices):
    n = len(stock_prices)
    dp = [[0 for _ in range(n)] for _ in range(2)]
    for i in range(1, n):
        current_day_max_profit = -math.inf
        for j in range(1, i):  # each prev days
            current_day_max_profit = stock_prices[j] - stock_prices[i]
        dp[1][i] = max(dp[i - 1], current_day_max_profit)

    return dp[1][n - 1]


if __name__ == '__main__':
    pass
