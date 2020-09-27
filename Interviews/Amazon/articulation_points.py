"""
a graph
         0
      /    |
     1  -  2
  /  |
 3 -  4

depth first spanning tree

         0
      /    |
     1      2
  /   |
 3    4

breadth first spanning tree
         0
      /
     1  -  2
  /
 3  -  4
"""

"""
#         1    
#      /  |  \  
#     2 - | - 3 
#      \  |  /  
#         4      
          |  
#         5             

"""
graph3 = {
    "1": ['2', '3', '4'],
    "2": ['1', '3', '4'],
    "3": ['1', '2', '4'],
    "4": ['1', '2', '3', '5'],
    "5": ['4']
}

counter = 0
dfn = {'1': {'pre': 0, 'post': 0}, '0': {'pre': 0, 'post': 0}, '3': {'pre': 0, 'post': 0}, '2': {'pre': 0, 'post': 0},
       '4': {'pre': 0, 'post': 0}}

visited = []
low = {}
articulation = {}


def find_articulation_points(root, parent="-1"):
    print("vertex", root)
    visited.append(root)
    # pre order number
    global counter
    counter += 1
    dfn[root] = {'pre': counter}
    low[root] = counter
    articulation[root] = False
    for child in graph3[root]:
        if child not in visited:
            find_articulation_points(child, root)
            low[root] = min(low[root], low[child])
        elif child != parent:
            low[root] = min(low[root], dfn[child]["pre"])
        if low[child] >= dfn[root]["pre"]:
            articulation[root] = True
    # post order number
    counter += 1
    dfn[root]['post'] = counter


if __name__ == '__main__':
    find_articulation_points('1')
    print(dfn)
    print(low)
    print(articulation)

# **********************************************************************************************************************
"""
articulation points

check bi-connected?
if not print articulation points
how to make this graph bi-connected?

"""

"""

                      9
                      /
          1        5
       /    \   /  |  \
      4      2 --------7
       \    /  \   |  /
         3         8
      /   \
      10    9

"""

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
