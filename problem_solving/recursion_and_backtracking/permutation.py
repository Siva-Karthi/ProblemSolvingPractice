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
    if not array:
        return res
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
        # choose an option
        current.append(i)
        selected[i] = True
        helper(array, current, selected, res)  # proceed further
        # undo the selection
        selected[i] = False
        current.pop()


def combine(n, k):
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return
        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result
print(permutation_recursion_backtracking_framework([1, 2, 3]))
print("Combinations of 4 choose 2:", combine(4, 2))


def my_permutaion(arr):
    res = []
    if not arr:
        return res
    selected = {i: False for i in arr}
    my_helper(arr, selected, [], res)
    return res


def my_helper(arr, selected, current, res):
    # base
    if len(current) == len(arr):
        res.append(current[:])
    # explore choices
    for i in arr:
        #  validate and select choices
        if selected[i]:
            continue
        selected[i] = True
        current.append(i)
        # select 1 option and then unselect
        my_helper(arr, selected, current, res)
        # unselect
        selected[i] = False
        current.pop()


print("my_permutaion = ", my_permutaion([1, 2, 3]))


def my_powset(arr):
    res = []
    my_powset_helper(arr, 0, [], res)
    return res


def my_powset_helper(arr, idx, current, res):
    # base condition
    if idx == len(arr):
        res.append(current[:])
        return
    # explore options
    # validate and select - here include
    current.append(arr[idx])
    my_powset_helper(arr, idx + 1, current, res)
    # unselect - here exclude
    current.pop()
    my_powset_helper(arr, idx + 1, current, res)


print("my_powset_helper = ", my_powset([1, 2, 3]))
