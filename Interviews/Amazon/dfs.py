#         0
#      /    |
#     1 ---- 2
#  /  |      |
# 3 - 4 -----


def dfs_recursive(root):
    print("vertex", root)
    for child in graph[root]:
        dfs_recursive(child)


# base condition
# while loo
graph = {'0': ['1', '2'],
         '1': ['3', '4'],
         '2': [],
         '3': [],
         '4': []}

cyclic_graph = {'0': ['1', '2'],
                '1': ['3', '4', '2', '0'],
                '2': ['1', '4'],
                '3': ['1', '4'],
                '4': ['2', 3]}

#         0
#      /    |                   stack [2,1]
#     1      2             1    stack [2, 4,3]
#  /  |                    3   stack [2, 4]
# 3   4                    4   stack [2]
#                          2   stack []

#                          0,1,3, 4, 2

visited = {'0': False, '1': False, '2': False, '3': False, '4': False, '5': False}


def dfs_iterative(start):
    print("vertex", start)
    childs = cyclic_graph[start][::-1]

    while childs != []:
        child = childs.pop(-1)
        print("vertex", child)
        grand_childrens = cyclic_graph[child]
        if grand_childrens != []:
            childs.extend(grand_childrens[::-1])
    print("well done!")


def dfs_handle_cycle_iterative(start):
    print("vertex", start)
    childs = graph[start][::-1]
    while childs != []:
        child = childs.pop(-1)  # 3 ##childs [2]
        print("vertex", child)
        grand_childrens = graph[child]  # '3', '4'
        if grand_childrens != []:
            childs.extend(grand_childrens[::-1])  ## childs []
    print("well done!")


# output 0, 1, 3, 4, 2
# expected output = 0, 1, 3, 4, 2
if __name__ == '__main__':
    # theory
    # nolinear DS
    # A Graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph. More formally a Graph can be defined as,
    # runtimes
    # time ->O(v+e)
    # space -> O(e) # explain how
    pass

    # arr = dfs_recursive('0')
    # print(arr)
    arr = dfs_iterative('0')
    # print(arr)

    # complexity??
