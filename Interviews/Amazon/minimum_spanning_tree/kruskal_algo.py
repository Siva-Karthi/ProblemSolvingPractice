class DisjointSet(object):
    """
    data = [1,2,3]
    parents = []
    by rank - yet to be done
    path compression - yet to be done
    """
    data = []
    parent = {}

    def make_set(self, subsets: list):
        self.data = subsets
        self.parent = {i: i for i in subsets}  # initially parent are self only

    def union(self, subset1, subset2):
        self.parent[subset2] = subset1

    def find(self, element):
        if self.parent[element] == element:
            return element
        return self.find(self.parent[element])

    def is_cyclic(self, edge):
        # if both are in same set then cyclic else not
        parent_of_subset1 = self.find(edge[0])
        parent_of_subset2 = self.find(edge[1])
        if parent_of_subset1 == parent_of_subset2:
            return True
        return False


def get_sorted_edges(graph):
    edges_with_weights = {}
    for k, vertices in graph.items():
        for v in vertices:
            # if str(k) + "-" + str(v[0]) not in edges_with_weights and str(v[0])+ "-" + str(k)  not in edges_with_weights:
            #    edges_with_weights[str(k) + "-" + str(v[0])] = v[1]
            if tuple([k, v[0]]) not in edges_with_weights and tuple([v[0], k]) not in edges_with_weights:
                edges_with_weights[tuple([k, v[0]])] = v[1]
    print(edges_with_weights)
    sorted_edges = sorted(edges_with_weights, key=lambda k: edges_with_weights[k])
    print("sorted_edges", sorted_edges)
    return sorted_edges

def mst_using_kruskal_algo():
    """
    1. Sort all the edges in non-decreasing order of their weight.
    2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.
    3. Repeat step#2 until there are (V-1) edges in the spanning tree.
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
    T = []

    ds = DisjointSet()
    ds.make_set(weighted_graph.keys())
    cost = 0

    # get edges sorted based on cost in ascending order
    sorted_edges = get_sorted_edges(weighted_graph)

    while len(T) < (n - 1) and sorted_edges != []:
        # choose next least cost /smallest edge
        # delete from sorted edges
        least_cost_edge = sorted_edges.pop(0)
        # if not creating cycle then add it to T
        if not ds.is_cyclic(least_cost_edge):
            ds.union(least_cost_edge[0], least_cost_edge[1])
            # T.add(edge)
            T.append(least_cost_edge)
        else:  # else discard
            print("edge {} will make cycle so ignoring".format(least_cost_edge))
    if len(T) < n - 1:
        print("No spanning tree")
    else:
        print(T)


if __name__ == '__main__':
    mst_using_kruskal_algo()
