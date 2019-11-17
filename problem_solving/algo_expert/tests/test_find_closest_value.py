from Trees import binary_insert, Node
from problem_solving.algo_expert.find_closest_value import findClosestValueInBst


def test_simple():
    """
    simple find
    :return:
    """
    r = Node(10)
    binary_insert(r, Node(7))
    binary_insert(r, Node(1))
    binary_insert(r, Node(5))
    closer = findClosestValueInBst(tree=r,target=2)
    assert closer == 1


# def test_mid():
#     """
#     assumption is only one closer
#     :return:
#     """
#     r = Node(10)
#     binary_insert(r, Node(7))
#     binary_insert(r, Node(1))
#     binary_insert(r, Node(5))
#     closer = findClosestValueInBst(tree=r,target=2)
#     assert closer == 3