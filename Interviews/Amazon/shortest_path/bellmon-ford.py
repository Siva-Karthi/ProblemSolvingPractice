from pprint import pprint
import math

"""
#           1
#   (10) /   |   \ (-10)
#      2 -  |  - 3                           -> (2,3) =30 and (1,4) = 40
#  (-7)  \   |   / (20)
#           4
#   (8)     |
#           5
"""


def get_edges(graph):
    edges_with_weights = {}
    for k, vertices in graph.items():
        for v in vertices:
            if tuple([k, v[0]]) not in edges_with_weights and tuple([v[0], k]) not in edges_with_weights:
                edges_with_weights[tuple([k, v[0]])] = v[1]
    return edges_with_weights


def bellmon_ford(start="1"):
    """
    concept : for n-1 times relax the edges.

    relaxing of an edge(u,v) 
    if dist[w] + cost[w,v] < dist[v] 
       dist[v] = dist[w] + cost[w,v]

    :return:
    """
    weighted_graph = {
        "1": [('2', 1), ('3', 10), ('4', 40)],
        "2": [('1', 1), ('3', 30), ('4', 1)],
        "3": [('1', 10), ('2', 30), ('4', 20)],
        "4": [('1', 40), ('2', 1), ('3', 20), ('5', 1)],
        "5": [('4', 1)]
    }
    n = len(weighted_graph.keys())
    vertices = weighted_graph.keys()
    edges = get_edges(weighted_graph)
    # pprint(edges)
    
    # init 
    dist = {v:math.inf for v in vertices}
    dist[start] = 0

    # k-1 times
    for k in range(2,n):
        for edge, cost in edges.items():
            u = edge[0]
            v = edge[1]
            # check edge            
            if dist[u] + cost < dist[v]:
                dist[v] = dist[u] + cost
    
    pprint(dist)
    for edge, cost in edges.items():
        u = edge[0]
        v = edge[1]
        # check edge            
        if dist[u] + cost < dist[v]:
            pprint("ATTENTION : graph has a cycle with negative weights so above is incorrect value")
    


if __name__ == '__main__':
    bellmon_ford()