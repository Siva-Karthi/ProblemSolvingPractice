from ..recursion_and_backtracking.permutation import permutation_recursion_backtracking_framework


def test_permutation():
    res = permutation_recursion_backtracking_framework([1, 2, 3])
    assert len(res) == 6
    assert res == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
