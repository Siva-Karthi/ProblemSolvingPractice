class DisjointSet(object):
    """
    data = [1,2,3]
    parents = []
    by rank -  done
    by size -  done
    path compression - done
    """
    data = []
    parent = {}

    def make_set(self, subsets: list):
        self.data = subsets
        self.parent = {i: i for i in subsets}  # initially parent are self only
        self.size = [1] * (len(self.data) + 1)
        self.rank = [0] * (len(self.data) + 1)

    def union(self, subset1, subset2):
        self.parent[subset2] = self.find(subset1)

    def union_by_size(self, subset1, subset2):
        subset1_par = self.find(subset1)
        subset2_par = self.find(subset2)
        if subset1_par == subset2_par:
            return
        if self.size[subset1_par] < self.size[subset2_par]:
            self.parent[subset1_par] = subset2_par
            self.size[subset2_par] += self.size[subset1_par]
        else:
            self.parent[subset2_par] = subset1_par
            self.size[subset1_par] += self.size[subset2_par]

    def union_by_rank(self, subset1, subset2):
        subset1_par = self.find(subset1)
        subset2_par = self.find(subset2)

        if subset1_par == subset2_par:
            return

        if self.rank[subset1_par] < self.rank[subset2_par]:
            self.parent[subset1_par] = subset2_par
        elif self.rank[subset2_par] < self.rank[subset1_par]:
            self.parent[subset2_par] = subset1_par
        else:
            self.parent[subset2_par] = subset1_par
            self.rank[subset1_par] += 1

    def find(self, element):
        if self.parent[element] == element:
            return element
        return self.find(self.parent[element])

    def find_with_path_compression(self, element):
        if self.parent[element] == element:
            return element
        self.parent[element] = self.find(self.parent[element])
        return self.parent[element]
