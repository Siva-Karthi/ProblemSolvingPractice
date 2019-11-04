# def bin_search(array, item):
#     lent = len(array)
#     mid = int(array / 2)
#     mid_element = array[mid]
#     if item == mid_element:
#         return item
#     elif item < mid_element:
#         return bin_search(array[:mid], item)
#     elif item > mid_element:
#         return bin_search(array[mid + 1:], item)
#
#
# def twoNumberSum(array, targetSum):
#     # Write your code here.
#     sorted_array = list(sort(array))
#     for i in sorted_array:
#         my_pair = abs(targetSum - i)
#         if bin_search(sorted_array, my_pair):
#             return list(sort([my_pair, i]))
#     return []
#
#
# Q
#
# list.sort and sorted?

def twoNumberSum_(array, targetSum):
    for i, elem in enumerate(array):
       for j,another_elem in enumerate(array):
            if elem != another_elem:
                curr_sum = elem+another_elem
                print(elem, another_elem, curr_sum)
                if curr_sum == targetSum:
                    return list(sorted([elem,another_elem]))
    return []


def twoNumberSum_1(array, targetSum):
    total = len(array)
    for i in range(total):
        print(array[i])
        for j in range(i+1,total):
            print(array[j])
            print(array[i],array[j])
            print("\n\n\n")
    return []

#
# def twoNumberSum2(array, targetSum):
#     """
#     check matrix multiplication
#     :param array:
#     :param targetSum:
#     :return:
#     """
#     for elem in array:
#         pair = targetSum - elem
#         if pair != elem:
#             if pair in array: # O(n)
#                 return list(sorted([elem, pair]))
#     return []

#
# def twoNumberSum3(array, targetSum):
#     ref = {}
#     for i in array:
#         ref[i] = None
#
#     for elem in array:
#         pair = targetSum - elem
#         if pair != elem:
#             if pair in ref:
#                 return list(sorted([elem, pair]))
#     return []

def solution1(array, targetSum):
    ref = {}
    for elem in array:
        pair = targetSum - elem
        if pair in ref:
            return list(sorted([elem, pair]))
        else:
            ref[elem] = None
    return []


#OPTIMAL
def solution2(array, targetSum):
    """
    based on 2 pointerrs but is it correctly implemented?? need to check how to implement pointers in python
    :param array:
    :param targetSum:
    :return:
    """
    len_ = len(array)
    p1 = 0
    p2 = len_ - 1

    pairs = []
    sorted_array = sorted(array)

    while True:
        elem = sorted_array[p1]
        pair = sorted_array[p2]
        curr_sum = elem + pair
        if curr_sum == targetSum:
            pairs = [elem, pair]
            break
        elif curr_sum < targetSum:
            p1  = p1+1
        else:
            p2 = p2-1
    return pairs


# explantions from algoexpert


# # O(n^2) time | O(1) space
# def twoNumberSum(array, targetSum):
#     for i in range(len(array) - 1):
#         firstNum = array[i]
#         for j in range(i+1, len(array)):
#             secondNum = array[j]
#             if firstNum + secondNum == targetSum:
#                 # my doubt don't we need to sort it?
#                 return [firstNum, secondNum]
#     return []

# # O(n) time | O(n) space
# def twoNumberSum(array, targetSum):
#     nums = {}
#     for num in array:
#         potentialMatch = targetSum - num
#         if potentialMatch in nums:
#             # my doubt don't we need to sort it?
#             return [potentialMatch,num]
#         else:
#             nums[num] = True
#     return []

def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [array[left] , array[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []


if __name__ == '__main__':
    arr = [1,2,4,5]
    s = 30
    print(twoNumberSum(arr, s))