"""
Write a function that takes in a sorted array of integers as well as a target integer.
The function should use the Binary Search algorithm to find if the target number is contained in the array and
should return its index if it is, otherwise -1.

Sample input: [0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33
Sample output: 3
"""


def helper(array, target, L, R):
    if R >= L:
        mid = int(int(L + R) / 2)
        index = mid
        root = array[index]
        if target == root:
            return index
        elif target < root:
            return helper(array, target, L, index - 1)
        elif target > root:
            return helper(array, target, index + 1, R)
    return -1


def binarySearch(array, target):
    return helper(array, target, 0, len(array))
