#
# TC:
# normal
# to
# reach
# to
# reach = bishop
# to
# reach is in bishop
# border
# bishop and knnight
# same
from ..recursion_and_backtracking.n_queens import nonAttackingQueens


def test_nonAttackingQueens_negative():
    res = nonAttackingQueens(n=2)
    assert res == 0


def test_nonAttackingQueens_positive():
    res = nonAttackingQueens(n=4)
    assert res == 2


def test_nonAttackingQueens_positive_2():
    res = nonAttackingQueens(n=10)
    assert res == 724
