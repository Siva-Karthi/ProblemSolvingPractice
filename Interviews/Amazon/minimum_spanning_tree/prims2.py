import math


def get_next_least_cost_adjacent(TV, edges):
    next = None
    min_cost = math.inf
    for edge, cost in edges.items():
        u = edge[0]
        v = edge[1]
        if u in TV and v not in TV and cost < min_cost:
            min_cost = cost
            next = edge
    assert next !=None
    return next


def get_edges(graph):
    edges_with_weights = {}
    for k, vertices in graph.items():
        for v in vertices:
            if tuple([k, v[0]]) not in edges_with_weights and tuple([v[0], k]) not in edges_with_weights:
                edges_with_weights[tuple([k, v[0]])] = v[1]
    return edges_with_weights


def mst_using_prims_algo():
    """
    * T = []
    * TV = {}
    * until there are (V-1) edges in the spanning tree.
        2. Take the least weight edge where <u,v> where as u belongs to TV and not belongs to v


    :return:

      1
    /
   2  -- 3
    """

    ""

    # n   = vertices in a graph
    # n-1 = edges in spanning tree
    # weighted_graph["1"] -> [('2', 1), ('3', 10), ('4', 40)]
    #           1
    #   (1) /
    #      2

    #           1
    #   (1) /   |   \ (10)
    #      2 -  |  - 3(30)
    #  (1)  \   |
    #           4 (40)

    ""

    weighted_graph = {
        "1": [('2', 1), ('3', 10), ('4', 40)],
        "2": [('1', 1), ('3', 30), ('4', 1)],
        "3": [('1', 10), ('2', 30), ('4', 20)],
        "4": [('1', 40), ('2', 1), ('3', 20), ('5', 1)],
        "5": [('4', 1)]
    }

    n = len(weighted_graph.keys())
    T = []
    edges = get_edges(weighted_graph)
    # print(edges)

    # 1. choose next from edges with minimal weight....
    # 2. chosen vertex shouldn't form a cycle and should connect TO ALREADY vertices in the tree
    #           1
    #   (1) /   |   \ (10)
    #      2 -  |  - 3                           -> (2,3) =30 and (1,4) = 40
    #  (1)  \   |   / (20)
    #           4
    #   (1)     |
    #           5
    TV = ["1"]  # starting from vertex-1
    while len(T) < (n - 1):
        next_edge = get_next_least_cost_adjacent(TV, edges)
        if not next_edge:
            break
        T.append(next_edge)
        TV.append(next_edge[1])

    if len(T) < n - 1:
        print("No spanning tree")
    else:
        print(T)


if __name__ == '__main__':
    mst_using_prims_algo()
