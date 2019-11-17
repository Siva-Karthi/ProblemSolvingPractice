# import math
#
# closer = math.inf
#
#
# def inorderTraversal(root, target):
#     if root:
#         inorderTraversal(root.left, target)
#         print(root.value)
#         curr_diff = abs((root.value) - (target))
#         if curr_diff < closer:
#             closer = root.value
#         inorderTraversal(root.right, target)
#
#
# def goCloser(tree, target, prev_closer=math.inf, supp=1):
#     root_dist = abs(target - tree.value)
#     left = tree.left
#     right = tree.right
#     left_distance = None
#     right_distance = None
#
#     if not (left and right) or root_dist == 0:
#         return tree.value
#
#     close_map = {root_dist: tree.value}
#
#     if left:
#         left_distance = abs((target) - (left.value))
#         close_map[left_distance] = left.value
#     if right:
#         right_distance = abs((target) - (right.value))
#         close_map[right_distance] = right.value
#
#     curr_closer = min(close_map.keys())
#     print("tree", tree.value, tree.left.value, tree.right.value)
#     print("x=>", root_dist, tree.value, left_distance, left.value, right_distance, right.value, target)
#     print("curr_closer", curr_closer, close_map)
#
#     if curr_closer > prev_closer or close_map[curr_closer] == tree.value:
#         return close_map[curr_closer]
#     elif close_map[curr_closer] == tree.left:
#         return goCloser(tree.left, target, curr_closer, supp=supp)
#     else:
#         return goCloser(tree.right, target, curr_closer, supp=supp)
#
#
# def findClosestValueInBst(tree, target):
#     # Write your code here.
#     # supp = 1 if target >= 0 else -1
#     # closer = goCloser(tree, target, math.inf, supp = 1)
#     print(closer)
#     inorderTraversal(tree, target)
#     print(closer)
#     return closer

# After explanation
import math

# Average : O(Log(n)) time | O(1) space
# Worst : O(n) time | O(1) space
def findClosestValueInBst(tree, target):
    root = tree
    closer = root.value
    distance = math.inf
    while root:
        curr_distance = abs((root.value) - (target))
        if curr_distance < distance:
            distance = curr_distance
            closer = root.value
        if root.value < target:
            root = root.right
        elif root.value > target:
            root = root.left
        elif root.value == target:
            break
    return closer

# note recursive is
# Average : O(Log(n)) time |  O(Log(n)) space
# Worst : O(n) time | O(n) space . but I'll say thats max recursion depth exceeded. but how do you handle ?
# https://www.geeksforgeeks.org/python-handling-recursion-limit/ # set increased recursion limit where as defaujlt is 10^4
# dynamic programming ? memozation

