def build(arr, segment_t, node, l, r):
    if l == r:
        segment_t[node] = arr[l]
        return
    mid = (l + r) // 2
    build(arr, segment_t, 2 * node, l, mid)
    build(arr, segment_t, 2 * node + 1, mid + 1, r)
    segment_t[node] = segment_t[2 * node] + segment_t[2 * node + 1]


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = len(arr)
segment_t = [0] * (4 * n)
build(arr, segment_t, 1, 0, n - 1)
print("segment_tree =", segment_t)


def range_sum(arr, segment_t, node, l, r, ql, qr):
    print(ql, l)
    if ql > r or qr < l:  # No overlap
        return 0
    # elif (l == ql )and (r == qr):
    #     return segment_t[node]
    if ql <= l and r <= qr:  # Total overlap
        return segment_t[node]
    mid = (l + r) // 2
    lres = range_sum(arr, segment_t, 2 * node, l, mid, ql, qr)
    rres = range_sum(arr, segment_t, 2 * node + 1, mid + 1, r, ql, qr)
    res = lres + rres
    return res


print("range sum =", range_sum(arr, segment_t, 0, 0, n, 2, 5))
# todo : practise update element and make it as class based and try also pointer based apporach

# def build_binary_tree(arr, index=0, bt_array=None):
#     if bt_array is None:
#         bt_array = []
#
#     # Base case: If the index exceeds the array length, return
#     if index >= len(arr) or arr[index] is None:
#         return
#
#     # Add the current node value to the binary tree array
#     bt_array.append(arr[index])
#
#     # Recursively build the left and right subtrees
#     build_binary_tree(arr, 2 * index + 1, bt_array)  # Left child index
#     build_binary_tree(arr, 2 * index + 2, bt_array)  # Right child index
#
#     return bt_array


# bottom up
# def build_binary_tree_bottom_up(arr, index=0, bt_array=None):
#     if bt_array is None:
#         bt_array = [None] * len(arr)  # Initialize an array to hold the binary tree nodes
#
#     # Base case: If the index exceeds the array length, return
#     if index >= len(arr) or arr[index] is None:
#         return
#
#     # Recursively build the left and right subtrees first
#     build_binary_tree_bottom_up(arr, 2 * index + 1, bt_array)  # Left child index
#     build_binary_tree_bottom_up(arr, 2 * index + 2, bt_array)  # Right child index
#
#     # After the left and right subtrees are built, assign the current node
#     bt_array[index] = arr[index]
#
#     return bt_array

# Example usage
# arr = [1,2,3,4]
# bt_array = build_binary_tree(arr)

# Print the array representation of the binary tree
# print("Binary Tree Array:", bt_array)

# bst = [None] * (4*n)
# def bst(sorted_arr, bst, node, l, r):
#     if l == r:
#         segment_t[node] = arr[l]
#         return
#     mid = (l + r) // 2
#     build(arr, segment_t, 2 * node, l, mid)
#     build(arr, segment_t, 2 * node + 1, mid + 1, r)
#     segment_t[node] = segment_t[2 * node] + segment_t[2 * node + 1]


# Example usage

# sorted(arr)
# bst(arr, segment_t, 1, 0, n - 1)

# """
# why?
#
# """
# # [0,3,1,2,0,0,0,0] 4*n
# # l_sum = 2*l = 0
# # r_sum = 2*r = 2
# # sum = 2 * l + 2 * r
# # cases:
# # completely left
# # completely right
# # overlap in the tree?
#     # divide and conquer

# root = 0
# """
# if n
#     then arr[n] = node
# """
# def build(arr, l, r, node, segment_t):
#     if l==r: # leaf node
#         # set leaf value
#         segment_t[node] = arr[l]
#     mid = (l+r)//2
#     build(arr, l, mid, node,segment_t)
#     build(arr, mid+1,r, node+1, segment_t)
#     # set parent
#     segment_t[node] = segment_t[2*node] + segment_t[2*node+1]
# # # def get_sum(l,r):
# # #     pass
# arr = [1,2]
# n = len(arr)
# # array based implmentation of segment tree
# segment_t = [0] * 4 * n # usually 4 * n values
# build(arr, 0,n, 0, segment_t)
# print("segment_tree = ", segment_t)
