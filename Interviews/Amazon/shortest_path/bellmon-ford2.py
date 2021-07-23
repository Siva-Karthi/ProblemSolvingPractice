from pprint import pprint
import math

"""
#           1
#   (10) /   |   \ (10)
#      2 -  |  - 3                           -> (2,3) =30 and (1,4) = 40
#  (-7)  \   |   / (20)
#           4
#   (10)     |
#           5
"""


def get_edges(graph):
    edges_with_weights = {}
    for k, vertices in graph.items():
        for v in vertices:
            if tuple([k, v[0]]) not in edges_with_weights and tuple([v[0], k]) not in edges_with_weights:
                edges_with_weights[tuple([k, v[0]])] = v[1]
    return edges_with_weights


# Time complexity O(V-1*E) | Space complexity O(V) to store distances
def bellmon_ford(start="1"):
    """
    concept : for n-1 times relax the edges.

    relaxing of an edge(u,v) 
    if dist[w] + cost[w,v] < dist[v] 
       dist[v] = dist[w] + cost[w,v]
    ------
    consider a graph G with edges e∈E and vertices v∈V

    shortest path b/w `v` to `u` with P can have atmost k-1 edges only (since we can connect n vertices with n-1 edges)

    so two cases
        1. dist^k[u] = dist^k-1[u] with atmost k, k>0 and no more than k-1 [consider k as n]
        2. exactly k edges the it might be comprised of the a path from v to any vertex j and j to u. path length of v to j is
            dist^k-1[j] all vertices i such that <i,u> in the graph are candidates for j. since we are focused
            on only shortest path i that minimizes dist^k-1[i]+length[i][u] is the correct value for j. This leads to the
            following formula

            dist^k[u] = min {
                                dist^k-1[u] ,
                                min {dist^k-1[i] + length[i][u] for each edges j to u }
                            }


    Also it Can find if there's any negative weight cycles
    :return:
    """
    weighted_graph = {
        "1": [('2', 10), ('3', 10), ('4', 40)],
        "2": [('1', 10), ('3', 30), ('4', -7)],
        "3": [('1', 10), ('2', 30), ('4', 20)],
        "4": [('1', 40), ('2', -7), ('3', 20), ('5', 10)],
        "5": [('4', 10)]
    }
    n = len(weighted_graph.keys())
    vertices = weighted_graph.keys()
    edges = get_edges(weighted_graph)
    # pprint(edges)
    
    # init
    dist = {k:math.inf for k in weighted_graph}
    dist[start] = 0

    for i in range(n-1):
        for edge, cost in edges.items():
            v = edge[0]
            u = edge[1]
            if dist[u] > dist[v] + cost:
                dist[u] = dist[v] + cost
    pprint(dist)

    for edge, cost in edges.items():
        u = edge[0]
        v = edge[1]
        # check edge
        if dist[u] + cost < dist[v]:
            pprint("ATTENTION : graph has a cycle with negative weights so above is incorrect value")

if __name__ == '__main__':
    bellmon_ford()

"""
Improvements 
    1. if none changed in a iteration then stop even before n-1 iterations , Maintain a queue of vertices whose dist changed blah blah
    
"""

# print paths? - # predecessor graph?
# how iteration differs?
# single destination shortest path?