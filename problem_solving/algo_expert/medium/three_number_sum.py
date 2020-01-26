"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of
all these triplets. The numbers in each triplet should be ordered in ascending order, and the triplets themselves
should be ordered in ascending order with respect to the numbers they hold. If no three numbers sum up to the
target sum, the function should return an empty array.

Sample input: [12, 3, 1, 2, -6, 5, -8, 6], 0
Sample output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
"""


def threeNumberSum(array, targetSum):
    array.sort()
    l = len(array)
    res = []
    """going through last two elements won't make sense,
    since right will be atmost lth position
    consider l = 4
    for second last element 
    curr = 2
    left = 3
    right = 3
    hence not left < right, noops will be taken

    same for last element
    """

    for i in range(0, l - 2):
        curr = i
        left = i + 1
        right = l - 1
        while left < right:
            curr_sum = array[curr] + array[left] + array[right]
            if curr_sum == targetSum:
                res.append([array[curr], array[left], array[right]])
                left += 1
            elif curr_sum < targetSum:
                left += 1
            elif curr_sum > targetSum:
                right -= 1
    # since input array is already sorted, we don't want below steps
    # for sub_res in res:
    # 	sub_res.sort()
    # res.sort()
    return res
