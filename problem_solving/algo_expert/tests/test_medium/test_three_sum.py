# Add, edit, or remove tests in this file.
# Treat it as your playground!
from problem_solving.algo_expert.medium.three_number_sum import threeNumberSum


def test_case_1():
    assert threeNumberSum([1, 2, 3], 6) == [[1, 2, 3]]


def test_case_2():
    assert threeNumberSum([1, 2, 3], 7) == []


def test_case_3():
    assert threeNumberSum([8, 10, -2, 49, 14], 57) == [[-2, 10, 49]]


def test_case_4():
    assert threeNumberSum([12, 3, 1, 2, -6, 5, -8, 6], 0) == [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]


def test_case_5():
    assert threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1], 0) == [[-8, 3, 5], [-6, 1, 5], [-1, 0, 1]]


def test_case_6():
    assert threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6], 0) == [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5],
                                                                     [-1, 0, 1]]


def test_case_7():
    assert threeNumberSum([12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0) == [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5],
                                                                         [-5, -1, 6], [-5, 0, 5], [-5, 2, 3],
                                                                         [-1, 0, 1]]


def test_case_8():
    assert threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18) == [[1, 2, 15], [1, 8, 9], [2, 7, 9], [3, 6, 9],
                                                                   [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]]


def test_case_9():
    assert threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 32) == [[8, 9, 15]]


def test_case_10():
    assert threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 33) == []


def test_case_11():
    assert threeNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 5) == []
