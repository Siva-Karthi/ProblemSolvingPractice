"""
Write a function that takes in an array of integers and returns a sorted array of the three largest integers in
the input array. Note that the function should return duplicate integers if necessary; for example,
it should return [10, 10, 12] for an input array of [10, 5, 9, 10, 12].

Sample input: [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
Sample output: [18, 141, 541]
"""


def findThreeLargestNumbers(array):
    import heapq
    heap = array
    heapq.heapify(heap)
    res = heapq.nlargest(3, heap)
    res = sorted(res)
    return res

# findThreeLargestNumbers([55, 43,11, 3, -3, 10])
# ans = [11, 43, 55]
