from problem_solving.algo_expert.medium.closest_pairs import smallestDifference


def test_case_1():
    assert smallestDifference([-1, 5, 10, 20, 3], [26, 134, 135, 15, 17]) == [20, 17]


def test_case_2():
    assert smallestDifference([-1, 5, 10, 20, 28, 3], [26, 134, 135, 15, 17]) == [28, 26]


def test_case_3():
    assert smallestDifference([10, 0, 20, 25], [1005, 1006, 1014, 1032, 1031]) == [25, 1005]


def test_case_4():
    assert smallestDifference([10, 0, 20, 25, 2200], [1005, 1006, 1014, 1032, 1031]) == [25, 1005]


def test_case_5():
    assert smallestDifference([10, 0, 20, 25, 2000], [1005, 1006, 1014, 1032, 1031]) == [2000, 1032]


def test_case_6():
    assert smallestDifference([240, 124, 86, 111, 2, 84, 954, 27, 89], [1, 3, 954, 19, 8]) == [954, 954]


def test_case_7():
    assert smallestDifference([0, 20], [21, -2]) == [20, 21]


def test_case_8():
    assert smallestDifference([10, 1000], [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]) == [1000, 1014]


def test_case_9():
    assert smallestDifference([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123],
                              [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]) == [-123, -124]


def test_case_10():
    assert smallestDifference([10, 1000, 9124, 2142, 59, 24, 596, 591, 124, -123, 530],
                              [-1441, -124, -25, 1014, 1500, 660, 410, 245, 530]) == [530, 530]
