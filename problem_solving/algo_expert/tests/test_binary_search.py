from problem_solving.algo_expert.binary_search import binarySearch


def test_simple():
    """
    simple search
    :return:
    """
    sorted_array = [1, 2, 3, 4]
    target = 5
    index = binarySearch(array=sorted_array, target=target)
    assert index == -1
