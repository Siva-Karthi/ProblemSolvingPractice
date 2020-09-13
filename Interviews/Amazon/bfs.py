"""
           A
      /    |     \
    B      C      D
 /   \          /
 E    F        G
    /   \        \
   H    I         J

#         0
#      /    |
#     1      2
#  /  |
# 3    4
  |
  5
outut : 0, 1, 2, 3, 4
"""
graph = {'0': ['1', '2'],
         '1': ['3', '4'],
         '2': [],
         '3': ['5'],
         '4': [],
         '5': []}


def bfs_recursive(root, child_queue=[]):
    print(root)
    # get childrens
    childs = graph[root]  # 1,2
    child_queue.extend(childs)  # child_queue [1,2]
    if child_queue != []:
        root = child_queue.pop(0)
        bfs_recursive(root, child_queue)


def bfs(root):
    print(root)
    # get childrens
    childs = graph[root]
    child_queue = childs  # [1,2]
    while child_queue:
        child = child_queue.pop(0)
        print(child)
        # resenrve grand children
        grand_childs = graph[child]
        if grand_childs != []:
            child_queue.extend(grand_childs)


if __name__ == '__main__':
    bfs('0')
