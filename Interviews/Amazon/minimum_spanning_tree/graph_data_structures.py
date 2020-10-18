"""
#           1
#   (1) /   |   \ (10)
#      2 -  |  - 3                           -> (2,3) =30 and (1,4) = 40
#  (1)  \   |   / (20)
#           4
#   (1)     |
#           5

output

#           1
#   (1) /      \ (10)
#      2         3
#  (1)  \
#          4
#   (1)    |
#          5

"""

weighted_graph = {
    "1": [('2', 1), ('3', 10), ('4', 40)],
    "2": [('1', 1), ('3', 30), ('4', 1)],
    "3": [('1', 10), ('2', 30), ('4', 20)],
    "4": [('1', 40), ('2', 1), ('3', 20), ('5', 1)],
    "5": [('4', 1)]
}


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


if __name__ == '__main__':
    ds = DisjointSet()
    ds.make_set([1, 2, 3])
    print(ds.find(3))
    ds.union(2, 3)  # is this correct?
    print(ds.find(3))
    print("---------")
    print(ds.find(1))
    print(ds.is_cyclic((2, 1)))
    ds.union(2, 1)  # is this correct?
    print(ds.find(1))
    print("---------")
    print(ds.is_cyclic((1, 3)))
