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
# outut : 2
                     9
                    / 
#         1        5
#      /    \   /  |  \
#     4      2 --------7
#      \    /  \   |  /
#        3         8 
       /   \
#     10    9           
# outut :
 
"""

# graph2 = {'1': ['4', '2'],
#          '1': ['0', '3', '4', '2'],
#          '2': ['0', '1'],
#          '3': ['1', '4'],
#          '4': ['1', '3'],
#          '5': ['6'],
#          '6': ['5'],
#          '7': ['8'],
#          '8': ['7']}

counter = 0
dfn = {'1': {'pre': 0, 'post': 0}, '0': {'pre': 0, 'post': 0}, '3': {'pre': 0, 'post': 0}, '2': {'pre': 0, 'post': 0},
       '4': {'pre': 0, 'post': 0}}

visited = []
low = {}


def dfs_iterative_handle_cycle(start):
    print("vertex=>", start)
    childs = graph[start][::-1]
    visited = [start]
    global counter

    counter += 1
    dfn[start] = {'low': counter}

    while childs != []:
        child = childs.pop(-1)
        counter += 1
        dfn[child] = {'low': counter}

        # print("vertex", child, "visited", visited, "child", child,"childs,", childs)
        visited.append(child)
        grand_childrens = graph[child]
        if grand_childrens != []:
            childs.extend([i for i in grand_childrens[::-1] if (i not in visited) and (i not in childs)])
        counter += 1
        dfn[child]['high'] = counter

    counter += 1
    dfn[start]['high'] = counter

    print("well done!")


def dfs_recursive(root):
    print("vertex", root)
    visited.append(root)
    # pre order number
    global counter
    counter += 1
    dfn[root] = {'pre': counter}

    for child in graph[root]:
        if child not in visited:
            dfs_recursive(child)
    # post order number
    counter += 1
    dfn[root]['post'] = counter


def art(root, parent="-1"):
    print("vertex", root)
    visited.append(root)
    # pre order number
    global counter
    counter += 1
    dfn[root] = {'pre': counter}
    low[root] = counter
    for child in graph[root]:
        if child not in visited:
            art(child, root)
            low[root] = min(low[root], low[child])
        elif child != parent:
            low[root] = min(low[root], dfn[child])
    # post order number
    counter += 1
    dfn[root]['post'] = counter


if __name__ == '__main__':
    art('0')
    print(dfn)
    print(low)

"""
articulation points

check bi-connected?
if not print articulation points
how to make this graph bi-connected?
"""
