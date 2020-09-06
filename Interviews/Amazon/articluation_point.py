# create dfs spannning tree
# find articulation points
# remove articulation points
# how biconnected components in a graph

# find dfn and low for each vertex, dfn = {}, low = {}
# verify two biconnected comonet of a same grah have no more than 1 edge in common

# what is biartite grah?
# comletye grajhj with n vertices, show thatthe number of sanning tree is atlleast 2^n-1 - 1

# proerties


# connected_undirected_graph
# use mocks

# spanning tree of the abve graph

"""
input =
           A
      /    |     \
    B      C      D
 /   \          /
 E    F        G
    /   \        \
   H    I         J

output DFS = A, B, E, F ,H, I, C, D, G, J
output BFS = A, B, C, D, E , F, G, H, I, J

exercise : find where to BFS
"""


class Vertex(object):
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Vertex(name))
        return self


A = Vertex("A")
B = Vertex("B")
C = Vertex("C")
D = Vertex("D")
E = Vertex("E")
F = Vertex("F")
G = Vertex("G")
H = Vertex("H")
I = Vertex("I")
J = Vertex("J")

A.addChild("B")
A.addChild("C")
A.addChild("D")

# B
A.children[0].addChild("E")
A.children[0].addChild("F")

# D
A.children[2].addChild("G")

# F
A.children[0].children[1].addChild("H")
A.children[0].children[1].addChild("I")

# G
A.children[2].children[0].addChild("J")


def dfs_recursive(root, arr=[]):
    # print("node,", root.name)
    arr.append(root.name)
    for child in root.children:
        dfs_recursive(child, arr=arr)
    return arr


def bfs(root, arr=[]):
    childs = root.children
    arr.append(root.name)
    while childs:
        next_ = childs.pop(0)
        arr.append(next_.name)
        if next_.children:
            childs.extend(next_.children)
    return arr


def bfs_recursive(root, arr=[], childs=[]):
    arr.append(root.name)
    if root.children:
        childs.extend(root.children)
    if childs:
        bfs_recursive(childs.pop(0), arr, childs)
    return arr


"""
vertex - n 
e      - n-1
 
input graph = 

        0
     /    | 
    1 ---- 2 
 /  |      |
3 - 4 ----- 

output DFS = 0, 1, 3, 4, 2
output BFS = 0, 1, 3,4
"""

#
# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}

graph = {'0': ['1', '2'],
         '1': ['0', '3', '4'],
         '2': ['0'],
         '3': ['1'],
         '4': ['2', '3']}

visited = {str(i): False for i in range(5)}


# DFS algorithm
def dfs_connected_undirected(start):
    print(start)
    visited[start] = True
    for next in graph[start]:
        if not visited[next]:
            dfs_connected_undirected(next)
    return visited


# """
# input graph =
#                   0    (1 - 1)
#               /    |
# (2 - )       1 ---- 2    (5)
#            /  |     |
# (3 - )    3 - 4 ----
#               (4 - )
# output =
#
# """
# visited = {str(i): False for i in range(5)}
# dfn = {str(i): -1 for i in range(5)}
# low = {str(i): -1 for i in range(5)}
# def dfn_and_low(start, parent, idx = 0):
#     """
#     dfn[i] just num++
#     low = min
#
#     """
#     print(start)
#     visited[start] = True
#
#     dfn[start] = idx+1
#     low[start] = idx+1
#
#     for next in graph[start]:
#         if not visited[next]:
#             dfn_and_low(next,start,idx+1)
#             low[start] = min(low[start], low[next])
#         else:
#             if next != parent:
#                 low[start] = min(low[start], dfn[next])

if __name__ == '__main__':
    # theory
    # nolinear DS
    # A Graph is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph. More formally a Graph can be defined as,
    # runtimes
    # time ->O(v+e)
    # space -> O(e) # explain how

    arr = dfs_recursive(A)
    print(arr)
    # arr = bfs_recursive(A)
    # print(arr)
    # arr = bfs(A)
    # print(arr)
    # **********************#

    # dfs_connected_undirected('0')
    # ***

    #
    # Why this class - value added purpose for this group
    # I have started this and I don't want waste your time and go empty handed
    #
    # Take aways
    # Basic idea on graph
    # whats next?
    # references and relevant graph problems to practice

# process and plan to prepare for the interview on FANG(experimental and not proved)

# Why are processes important? They are important because they describe
# how things are done and then provides the focus for making them better
# and how they are done determines how successful the outcomes will be.
# If you focus on the right processes, in the right way, you can design your way to success.

#


# Discussiing ideas if any
# polls in slack
# 30 | 30
# check the problems sheet
