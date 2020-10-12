from Interviews.Amazon.minimum_spanning_tree.data_structures import weighted_graph


def get_sorted_edges(graph):
    edges = []
    for k, v in graph:
        pass


def mst_using_kruskal_algo():
    """
    1. Sort all the edges in non-decreasing order of their weight.
    2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
    3. Repeat step#2 until there are (V-1) edges in the spanning tree.
    :return:
    """
    n = len(weighted_graph.keys())
    T = []

    cost = 0

    # get edges sorted based on cost in ascending order
    sorted_edges = get_sorted_edges(weighted_graph)

    while len(T) < (n - 1) and sorted_edges != []:
        # choose next least cost /smallest edge
        # delete from sorted edges
        # if not creating cycle then add it to T
        # T.add(edge)
        # else discard
        # rint("edge will make cycle so ignorign")
        pass

    if len(T) < n - 1:
        print("No spanning tree")
