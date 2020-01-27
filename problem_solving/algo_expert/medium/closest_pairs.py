"""
Write a function that takes in two non-empty arrays of integers. The function should find the pair of numbers
(one from the first array, one from the second array) whose absolute difference is closest to zero.
The function should return an array containing these two numbers, with the number from the first array in the
first position. Assume that there will only be one pair of numbers with the smallest difference.

Sample input: [-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]
Sample output: [28, 26]
"""

from math import inf


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    l1 = len(arrayOne)
    l2 = len(arrayTwo)

    left = 0
    right = 0
    pairs = []
    _min = inf

    while left < l1 and right < l2:
        curr_abs_diff = abs((arrayOne[left]) - (arrayTwo[right]))
        if curr_abs_diff == 0:
            pairs[0] = arrayOne[left]
            pairs[1] = arrayTwo[right]
            break

        if curr_abs_diff <= _min:
            _min = curr_abs_diff
            pairs = [arrayOne[left], arrayTwo[right]]

        if arrayOne[left] < arrayTwo[right]:
            left += 1
        else:
            right += 1
    return pairs
