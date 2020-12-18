graph = {'0': ['1', '2'],
         '1': ['0', '3', '4', '2'],
         '2': ['0', '1'],
         '3': ['1', '4'],
         '4': ['1', '3'],
         '5': ['6'],
         '6': ['5'],
         '7': ['8'],
         '8': ['7']}
"""
#         0
#      /    |
#     1  -  2
#  /  |     
# 3 -  4    
#                
# 5    7  - 8
# |
# 6
# output : 3
"""


def dfs_iterative_handle_cycle(start):
    print("vertex", start)
    childs = graph[start][::-1]
    visited = [start]
    while childs != []:
        child = childs.pop(-1)
        # print("vertex", child, "visited", visited, "child", child,"childs,", childs)
        visited.append(child)
        grand_childrens = graph[child]
        if grand_childrens != []:
            childs.extend([i for i in grand_childrens[::-1] if (i not in visited) and (i not in childs)])
    print("well done!")


visited = []


def dfs_recursive(root):
    print("vertex", root)
    visited.append(root)
    for child in graph[root]:
        if child not in visited:
            dfs_recursive(child)


if __name__ == '__main__':
    dfs_iterative_handle_cycle('0')

    # # connected components and count
    # cc = 0
    #
    # for vertex in graph:
    #     if vertex not in visited:
    #         print("calling", vertex, "\n")
    #         dfs_recursive(vertex)
    #         cc = cc + 1
    #         print("***")
    # print("number of connected components = ", cc)

# how to mutual friends
