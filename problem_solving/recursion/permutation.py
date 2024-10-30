# def backtrack(arr, path, used):
#     if len(path) == len(arr):
#         print(path)
#         return
#     for i in range(len(arr)):
#         if used[i]:
#             continue
#         # Include arr[i] in the current permutation
#         used[i] = True
#         backtrack(arr, path + [arr[i]], used)
#         used[i] = False  # Backtrack
#
# def permute_backtracking(arr):
#     used = [False] * len(arr)
#     backtrack(arr, [], used)
#
# # Example usage
# arr = [1, 2, 3]
# permute_backtracking(arr)

# def getPermutations(array):
#     results = []
#     stack = [(array, [])]  # Start with the full array and an empty path
#
#     while stack:
#         current_array, current_perm = stack.pop()  # Get the current state
#
#         if not current_array:  # If no elements left to add
#             results.append(current_perm)  # Save the complete permutation
#         else:
#             for i in range(len(current_array)):
#                 # Create a new state by removing the current element
#                 new_array = current_array[:i] + current_array[i + 1:]
#                 new_perm = current_perm + [current_array[i]]
#                 stack.append((new_array, new_perm))  # Add the new state to the stack
#
#     return results
#
#
# # Example usage
# arr = [1, 2, 3]
# permutations = getPermutations(arr)
# print(permutations)

def permutation_recursion_backtracking_framework(array):
    res = []
    selected = {i: False for i in array}
    helper(array, [], selected, res)
    return res


def helper(array, current, selected, res):
    # goal - base condition
    if len(current) == len(array):
        res.append(current[:])
    # explore choices
    for i in array:
        if selected[i]:
            continue
        current.append(i)  # choose an option
        selected[i] = True
        helper(array, current, selected, res)  # proceed further
        # undo the selection
        selected[i] = False
        current.pop()


print(permutation_recursion_backtracking_framework([1, 2, 3]))
