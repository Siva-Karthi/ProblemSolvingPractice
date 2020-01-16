from problem_solving.algo_expert.find_three_largest_integers import findThreeLargestNumbers


def test_simple():
    res = findThreeLargestNumbers([55, 43, 11, 3, -3, 10])
    assert res == [11, 43, 55]
