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

    # 1.what is the objective function f(n)=  f(n)shortest path length from s to d using only k edges
    # 2.identify base cases
    #     when k == 1, ans = cost[s][d]
    #     when k ==0 , ans = cost[s][s]
    #     when k<0 , ans = 0??? // wont occur
    # 3.write down the recurrence relation
    #     shortest(s,d) when at k, k<n = min((shortest(s,k)^k-1 + shortest(k,j))^k-1,shortest(j,d)) // check s-d < [s to all each other vertex(k) + that k to d]
    # 4.order of exec
    #  bottom up
    # 5.where to find answers
        # distance array at k-1th step (since k time and integer vertices it bacame easy)

    for edge, cost in edges.items():
        s = edge[0]
        d = edge[1]
        distances[int(s) -1 ][int(d) -1] = cost
        # print("s", s)
        # print("d", d)
        # distances[int(s)][int(d)] = cost

    # for ktimes in range(n):
    #     random_vertex = ktimes+1

    for k in range(1,n):
        for s in range(0,n):
            for d in range(0,n):
                print(s,d, k)
                if distances[s][k] + distances[k][d] < distances[s][d]:
                    distances[s][d] = distances[s][k] + distances[k][d]
    pprint("distances")
    pprint(distances)
if __name__ == '__main__':
    all_pair_shortest_path()