"""
a graph
         0
      /    |
     1  -  2
  /  |
 3 -  4

 in order 0,1,3,4
 re order
 ost order

depth first spanning tree

   1/10     0
        /    |
   2/7  1      2 8/9
     /   |
 3/4 3    4 5/6


3                    4

3-4   5-6

1         3

2            7 -
    3 4 - child


breadth first spanning tree
         0
      /
     1  -  2
  /
 3  -  4
"""

# low[child] >= dfn[root]
#  art

# current 4
#  5
# 4 >= 3 =True ;l then 4 is an srticuklation oint or bottleneck

"""
#          1    
#       /  |  \  
#      2 - | - 3 
#       \  |  /  
#          4         low =    1-> default = dfn ; 2 ->  min of the low of all the connections except parent
           |  
#          5                 low 2;  min( 1, 1)
#                            low 4;
                                                     1 = (3, 1)
                              if visited -> take min(low(current), dfn[child])

# low {
   1 : 1
   4: 1
   3: 1
   2: 1
   
}

#          1    
#       /    
#      2 - - 3 
#       \     
#          4      
           |  
#          5             


       1
  (15)/  \ (20)
    2 - - 3
      (15)
      
  v = 3
  e = 3
  
  
  saannintree = grah with alll vertices connect using min number edges    
       1
    /     \         1   - 35
    2      3
    
    
       1
         \            2   - 35
    2 - - 3
  
       1                 3   - 30
     /   
    2 - - 3
  
  min number of edges = n-1 (n = vertices)
  
  maximum number of sannintree from a grah = n ^ (n-2)
         3 ^ 1 = 3 
         
   no cycle
         
         
         
minimum sanning treee


alications
   st   -  number ways to connect and choose one
   mst  - 
          
"""
graph3 = {
    "1": ['2', '3', '4'],
    "2": ['1', '3', '4'],
    "3": ['1', '2', '4'],
    "4": ['1', '2', '3', '5'],
    "5": ['4']
}

counter = 0
dfn = {'1': {'pre': 0, 'post': 0}, '3': {'pre': 0, 'post': 0}, '2': {'pre': 0, 'post': 0},
       '4': {'pre': 0, 'post': 0}}

visited = []
low = {}
articulation = {}
"""

#    (1/1)          1
#                 /
#    (2/2)       2
#              /  \
#    (3)      3    4 (4)
#                   |
#    (5)            5
"""


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


def biconnected_components(start_vertex: int, parent: int = '-1'):
    """
    * DFS the graph
    * find dfn, low along
        * dfn - just an incremental number (pre or post order number??)
        * low(u) = min{
            dfn(u),
            min{
            low(w) | w ∈ child of u in tree edges
            },
            dfn(x) | x is a grand parent/non tree edge or back edge
        }
    * find articulation points
    * find biconnected components
    :param start_vertex:
    :param parent:
    :return:
    """
    global num, dfn, low, visited, biconn_comps;
    if not visited[start_vertex]:
        num += 1
        dfn[start_vertex] = num
        low[start_vertex] = num
        visited[start_vertex] = True
    for adj in graph3[start_vertex]:
        biconn_comps.append((start_vertex, adj))
        # if adj != parent and dfn[adj]
        if not visited[adj]:
            num += 1
            dfn[adj] = num
            low[adj] = num
            visited[adj] = True
            biconnected_components(adj, start_vertex)
            low[start_vertex] = min(int(low[start_vertex]), int(low[adj]))
            if low[adj] >= dfn[start_vertex]:
                articulation_points.add(start_vertex)
                print("biconn_comps", biconn_comps)
                x,y = biconn_comps.pop()
                print(x,y)
                while not (x== start_vertex and y==adj):
                    x,y = biconn_comps.pop()
                    print(x,y)

        elif adj != parent:
            # grand parent/ backedge / non tree edge
            low[start_vertex] = min(int(low[start_vertex]), int(low[adj]))


if __name__ == '__main__':
    find_articulation_points('1')
    # pprint(dfn)
    # print(low)
    print(articulation)
    num = 0
    dfn = {v: 0 for v in graph3}
    low = {v: 0 for v in graph3}
    visited = {v: False for v in graph3}
    articulation_points = set()
    biconn_comps = []
    biconnected_components('1')
    # print(dfn)
    # print(low)
    # print("biconn_comps",biconn_comps)
    print("articulation_points", articulation_points)

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
