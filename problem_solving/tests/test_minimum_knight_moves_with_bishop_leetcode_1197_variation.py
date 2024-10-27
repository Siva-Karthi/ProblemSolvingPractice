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
from ..minimum_knight_moves_with_bishop_leetcode_1197_variation import get_kinight_min_steps


# position?

def test_minium_knight_moves_with_attacking_bishop_gets_killed():
    res = get_kinight_min_steps(M=6, N=6, X=1, Y=3, S=5, T=0, BX=4, BY=2)
    assert res == 3
