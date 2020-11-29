"""
dynamic programming framework

1.what is the objective function
2.identify base cases
3.write down the recurrence relation
4.order of exec
5.where to find answers
"""
import math
from pprint import pprint

def get_edges(graph):
    edges_with_weights = {}
    for k, vertices in graph.items():
        for v in vertices:
            if tuple([k, v[0]]) not in edges_with_weights and tuple([v[0], k]) not in edges_with_weights:
                edges_with_weights[tuple([k, v[0]])] = v[1]
    return edges_with_weights

def all_pair_shortest_path():
    """
    concept : use dynamic programming method to find shortest path source to destination by allowing k edges at a time
    :return:

    #           1
    #   (1) /   |   \ (10)
    #      2 -  |  - 3                           -> (2,3) =30 and (1,4) = 40
    #  (1)  \   |   / (20)
    #           4
    #   (1)     |
    #           5
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
    pprint(edges)
    distances = [[math.inf for i in vertices] for i in vertices]
    # base cases
    # k=0

    # 1.what is the objective function f(n)= number ways to to reach top of n steps by
    #                                        hopping 1 or 2 steps at a time
                                        # f(n)shortest path length from s to d
    # 2.identify base cases
    #     when k == 1, ans = cost[s][d]
    #     when k ==0 , ans = cost[s][s]
    #     when k<0 , ans = 0??? // wont occur
    # 3.write down the recurrence relation
    #     shortest(s,d) when k==n = min((shortest(s,k) + shortest(k,d)),shortest(s,d))
    # 4.order of exec
    #  bottom up
    # 5.where to find answers
        # distance array
    for edge,cost in edges.items():
        distances[int(edge[0])-1][int(edge[1])-1] = cost
    pprint(distances)

    for k in range(1, n): # n-1 edges enough to connect n edges so 
        for i in range(0,n):
            for j in range(0, n):
                if distances[i][k] + distances[k][j] <  distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    pprint(distances)



if __name__ == '__main__':
    all_pair_shortest_path()