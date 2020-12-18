"""
#           1
#   (1) /   |   \ (10)
#      2 -  |  - 3                           -> (2,3) =30 and (1,4) = 40
#  (1)  \   |   / (20)
#           4
#   (1)     |
#           5
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


def get_next_non_visited_min(vertices, visited, distances):
    _min = math.inf
    _next = None
    for vertex in vertices:
        if not visited[vertex] and distances[vertex] < _min:
            _min = distances[vertex]
            _next = vertex
    assert _next != None
    return _next


def djikstra(start="1"):
    """
    concept : take a source vertex and check choose another vertex not visited near by vertex and for all the other
     vertices if the distance is
            * less if passed via the selected vertex then change distance
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
    pprint(edges)

    visited = {i: False for i in weighted_graph.keys()}

    distance = {i: math.inf for i in weighted_graph.keys()}
    for adj in weighted_graph["1"]:
        distance[adj[0]] = adj[1]

    # init vertex
    visited[start] = True
    distance[start] = 0

    print("visited")
    pprint(visited)

    print("distance")
    pprint(distance)

    for i in range(1, n - 1):
        u = get_next_non_visited_min(visited=visited, distances=distance, vertices=vertices)
        # next_vertex = get_next_non_visited_min(visited, distance, edges)
        visited[u] = True
        for w in range(1, n + 1):
            if not visited[str(w)]:
                # what is no edge? handle
                if (u, str(w)) in edges:
                    if (distance[u] + edges[(u, str(w))] < distance[str(w)]):
                        distance[str(w)] = distance[u] + edges[(u, str(w))]
    pprint("shortest distance")
    pprint(distance)


def djikstra2(start="1"):
    """
    concept : take a source vertex and check choose another adjacent vertex which is not visited and cost is min and then for all the other
     vertices(or the adjacent of min) if the cost/distance is
            * less than its cost then update cost--------if passed via the selected vertex then change distance
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
    pprint(edges)

    visited = {i: False for i in weighted_graph.keys()}

    distance = {i: math.inf for i in weighted_graph.keys()}
    for adj in weighted_graph["1"]:
        distance[adj[0]] = adj[1]

    # init vertex
    visited[start] = True
    distance[start] = 0

    print("visited")
    pprint(visited)

    print("distance")
    pprint(distance)

    for i in range(1, n - 1):
        u = get_next_non_visited_min(visited=visited, distances=distance, vertices=vertices)
        visited[u] = True
        for adj in weighted_graph[u]:
            w = adj[0]
            cost = adj[1]
            if (distance[u] + cost < distance[w]):
                distance[w] = distance[u] + cost

    pprint("shortest distance")
    pprint(distance)


if __name__ == '__main__':
    djikstra()
    djikstra2()
