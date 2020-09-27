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
"""

counter = 0
dfn = {}
visited = []


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


if __name__ == '__main__':
    dfs_iterative_handle_cycle('0')
    print(dfn)

"""
articulation points

check bi-connected?
if not print articulation points
how to make this graph bi-connected?
"""
