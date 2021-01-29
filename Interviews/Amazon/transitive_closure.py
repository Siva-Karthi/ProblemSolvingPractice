"""
Transitive Closure
Consider a directed graph G and we need to determine is there any path from i to j for all i and j
    * if the path length is positive then its Transitive Closure -  A+
    * if the path length is >=0 then its Reflexive Closure - A*

Consider the graph is represented using an adjacency matrix
    * One wasy is to find All pair shortest path use the logic to set 1 0r 0 instead of updating path length - O(n^3) (k times matrix traversal)
    * Second optimized wasy is to find All pair connected components and mark them 1 in the 0-valued matrix - O(n^2) (for DFS for all vertices)

Reflexive closure is simple just add 1 in diagonal of the transitive closures\

Real world applications:
Consider social network b/w A,B,C
    friend
A  -------> B

    friend
B  -------> c


  transitive
  closure
A ------> C (we can suggest A to C and vice versa this is at 1 level)

Related interesting problems
1. find mutual friends
    B - is the mutual friend

2. How do you make this bi-connected and how many edges needed?

"""
import math
from pprint import pprint


def get_transitive_using_allpair(graph):
    vertices_count = len(graph) # using column size
    for k in range(0,vertices_count):
        for i in range(0,vertices_count):
            for j in range(0, vertices_count):
                graph[i][j] = graph[i][j] or (graph[i][k] and graph[k][j])
                # if graph[i][k] + graph[k][j] < graph[i][j]:
                #     graph[i][j] = graph[i][k] + graph[k][j]
        return graph


def get_transitive_using_connected_components(graph):

    return transitive

if __name__ == '__main__':
    """
#           1
#   (1) /   |   \ (10)
#      2 -  |  - 3                           -> (2,3) =30 and (1,4) = 40
#  (1)  \   |   / (20)
#           4
#   (1)     |
#           5
    """
    graph = [[0,   1,  10,  40,  0],
             [1,   0,  30,   1,  0],
             [10, 30,   0,  20,  0],
             [40,  1,  20,   0,  1],
             [0,   0,   0,   1,  0]
             ]
    pprint(graph)

    # graph = [[math.inf, 1,  1,  1,  math.inf],
    #          [1,  math.inf, 1,  1,  math.inf],
    #          [1,  1,  math.inf, 1,  math.inf],
    #          [1,  1,  1,  math.inf, 1],
    #          [math.inf, math.inf, math.inf, 1,  math.inf]
    #          ]

    transitive = [[math.inf, 1,  1,  1,  math.inf],
                 [1,  math.inf, 1,  1,  math.inf],
                 [1,  1,  math.inf, 1,  math.inf],
                 [1,  1,  1,  math.inf, 1],
                 [math.inf, math.inf, math.inf, 1,  math.inf]
                 ]

    distance = get_transitive_using_allpair(graph)
    # for i in range(len(graph)):
    #     for j in range(len(graph)):
    #         if distance[i][j] < math.inf:
    #             transitive[i][j] = 1

    pprint(transitive)
    pprint(distance)