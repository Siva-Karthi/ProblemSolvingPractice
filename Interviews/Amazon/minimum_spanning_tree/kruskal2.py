# DisjoinSet

class DisjointSet(object):

    """
    get vertices set each as parent of itself initially

    find find parent if parent == self then return
    union set `a` as parent of 'b'

    union - maintain rank array - set parent in such a way that it rank wont increase
    union - path compression -  save parent after find
    """
    def __init__(self, vertices):
        self.parent = {v:v for v in vertices}
        self.rank =  {v:0 for v in vertices}

    def union(self, parent, child):
        self.parent[child] = parent

    def find(self, vertex):
        # while self.parent[vertex] != vertex:
        #     return self.find(self.parent[vertex]) # send parent
        # return vertex

        # if self.parent[vertex] != vertex:
        #     return self.find(self.parent[vertex]) # send parent
        # return vertex

        if self.parent[vertex] == vertex:
            return vertex
        return self.find(self.parent[vertex])


    def find_and_path_compression(self, vertex):
        temp_parent = self.parent[vertex]
        if temp_parent != vertex:
            temp_parent = self.parent[temp_parent]
        #
        # # return vertex
        # if (self.parent[vertex] != vertex):
        #     self.parent[vertex] = self.find_and_path_compression(self.parent[vertex] );
        # self.parent[vertex] = temp_parent
        return temp_parent

    def union_by_rank(self, parent, child):
        if self.rank[parent] > self.rank[child]:
            self.parent[child] = parent
        elif self.rank[parent] < self.rank[child]:
            self.parent[parent] = child
        else: # incase of same rank, make anyone as parent and increase rank of that :)
            self.parent[child] = parent
            self.rank[parent] +=1

    def is_cyclic(self, edge):
        # if both are in same set then cyclic else not
        print("finding parent_of_subset1",edge[0])
        parent_of_subset1 = self.find(edge[0])
        print(" parent_of_subset1",parent_of_subset1)
        print("finding parent_of_subset2",edge[1])
        parent_of_subset2 = self.find(edge[1])
        print(" parent_of_subset2",parent_of_subset2)
        if parent_of_subset1 == parent_of_subset2:
            return True
        return False

    def is_cyclic_using_path_compression(self, edge):
        # if both are in same set then cyclic else not
        parent_of_subset1 = self.find_and_path_compression(edge[0])
        parent_of_subset2 = self.find_and_path_compression(edge[1])
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

def get_mst_using_kruskal():
    """
    keep disjoint set with vertices

    T = {}
    while len(T) < n-1
        take next least cost edge
        if adding next least cost edge wont make cycles then add else ignore
        disjointset.union(edge[0],edge[1])

    if len(T) < n-1
        print("graph is not connected)
    :return:
    """
    global weighted_graph
    edges = get_sorted_edges(graph=weighted_graph)
    disjoint_set = DisjointSet(weighted_graph.keys())

    n = len(weighted_graph)

    T = []

    while len(T) < n-1:
        next_least_cost_edge = edges.pop(0)
        # if not disjoint_set.is_cyclic_using_path_compression(next_least_cost_edge):
        if not disjoint_set.is_cyclic(next_least_cost_edge):
            T.append(next_least_cost_edge)
            disjoint_set.union(next_least_cost_edge[0], next_least_cost_edge[1])
            print("union",disjoint_set.parent)
            # disjoint_set.union_by_rank(next_least_cost_edge[0], next_least_cost_edge[1])

    print("union",disjoint_set.parent)
    print("rank", disjoint_set.rank)

    if len(T) < n-1:
        print("given graph is not connected :(")
    else:
        print("T", T)

if __name__ == '__main__':
    weighted_graph = {
        "1": [('2', 1), ('3', 10), ('4', 40)],
        "2": [('1', 1), ('3', 30), ('4', 1)],
        "3": [('1', 10), ('2', 30), ('4', 20)],
        "4": [('1', 40), ('2', 1), ('3', 20), ('5', 1)],
        "5": [('4', 1)]
    }
    get_mst_using_kruskal()