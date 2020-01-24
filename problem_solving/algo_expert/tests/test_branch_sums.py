from problem_solving.algo_expert.branch_sums import branchSums


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


def test_case_1():
    tree = BinaryTree(1)
    assert branchSums(tree) == [1]


def test_case_2():
    tree = BinaryTree(1).insert([2])
    assert branchSums(tree) == [3]


def test_case_3():
    tree = BinaryTree(1).insert([2, 3])
    assert branchSums(tree) == [3, 4]


def test_case_4():
    tree = BinaryTree(1).insert([2, 3, 4, 5])
    assert branchSums(tree) == [7, 8, 4]


def test_case_5():
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
    assert branchSums(tree) == [15, 16, 18, 10, 11]


def test_case_6():
    tree = BinaryTree(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1])
    assert branchSums(tree) == [15, 16, 18, 9, 11, 11, 11]


def test_case_7():
    tree = BinaryTree(0)
    tree.left = BinaryTree(1)
    tree.left.left = BinaryTree(10)
    tree.left.left.left = BinaryTree(100)
    assert branchSums(tree) == [111]


def test_case_8():
    tree = BinaryTree(0)
    tree.right = BinaryTree(1)
    tree.right.right = BinaryTree(10)
    tree.right.right.right = BinaryTree(100)
    assert branchSums(tree) == [111]


def test_case_9():
    tree = BinaryTree(0)
    tree.left = BinaryTree(9)
    tree.right = BinaryTree(1)
    tree.right.left = BinaryTree(15)
    tree.right.right = BinaryTree(10)
    tree.right.right.left = BinaryTree(100)
    tree.right.right.right = BinaryTree(200)
    assert branchSums(tree) == [9, 16, 111, 211]
