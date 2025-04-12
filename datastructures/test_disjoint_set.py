from . import DisjointSet


def test_init():
    ds = DisjointSet()
    ds.make_set([1, 2, 3])
    assert ds.size == [1] * 4
    assert ds.rank == [0] * 4
    assert ds.find(1) == 1
    assert ds.find(2) == 2
    assert ds.find(3) == 3


def test_union_find():
    ds = DisjointSet()
    ds.make_set([1, 2, 3, 4, 5])
    ds.union(1, 2)
    ds.union(2, 3)
    ds.union(3, 4)
    ds.union(4, 5)

    assert ds.find(5) == 1
    assert ds.find(4) == 1
    assert ds.find(3) == 1
    assert ds.find(2) == 1
    assert ds.find(1) == 1
    assert ds.parent == {5: 1, 4: 1, 3: 1, 2: 1, 1: 1}


def test_pathcompression():
    ds = DisjointSet()
    ds.make_set([1, 2, 3, 4, 5])
    ds.union(1, 2)
    ds.union(2, 3)
    ds.union(3, 4)
    ds.union(4, 5)

    assert ds.find_with_path_compression(5) == 1  # same result but faster
    assert ds.find_with_path_compression(4) == 1
    assert ds.find_with_path_compression(3) == 1
    assert ds.find_with_path_compression(2) == 1
    assert ds.find_with_path_compression(1) == 1
    assert ds.parent == {5: 1, 4: 1, 3: 1, 2: 1, 1: 1}


def test_union_by_rank():
    ds = DisjointSet()
    ds.make_set([1, 2, 3, 4, 5])
    ds.union_by_rank(1, 2)
    assert ds.find_with_path_compression(2) == 1
    assert ds.rank[1] == 1
    assert ds.rank[2] == 0
    ds.union_by_rank(2, 3)
    assert ds.find_with_path_compression(3) == 1
    assert ds.rank[1] == 1
    assert ds.rank[3] == 0

    ds.union_by_rank(4, 5)
    assert ds.rank[4] == 1
    assert ds.rank[5] == 0

    ds.union_by_rank(1, 4)
    assert ds.rank[1] == 2
    assert ds.rank[4] == 1
    assert ds.rank[5] == 0


def test_union_by_size():
    ds = DisjointSet()
    ds.make_set([1, 2, 3, 4, 5])
    ds.union_by_size(1, 2)
    assert ds.find_with_path_compression(2) == 1
    assert ds.size[1] == 2
    assert ds.size[2] == 1
    ds.union_by_size(2, 3)
    assert ds.find_with_path_compression(3) == 1
    assert ds.size[1] == 3
    assert ds.size[3] == 1
    ds.union_by_size(4, 5)
    assert ds.size[4] == 2
    assert ds.size[5] == 1
    ds.union_by_size(1, 4)
    assert ds.size[1] == 5
    assert ds.size[4] == 2
    assert ds.size[5] == 1
