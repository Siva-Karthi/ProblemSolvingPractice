from problem_solving.algo_expert.dfs import Node


def test_dfs_simple_positive():
    """
    input =
               A
          /    |     \
        B      C      D
     /   \          /
     E    F        G
        /   \        \
       H    I         J
    output =
    """
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")
    G = Node("G")
    H = Node("H")
    I = Node("I")
    J = Node("J")

    A.addChild("B")
    A.addChild("C")
    A.addChild("D")

    # B
    A.children[0].addChild("E")
    A.children[0].addChild("F")

    # D
    A.children[2].addChild("G")

    # F
    A.children[0].children[1].addChild("H")
    A.children[0].children[1].addChild("I")

    # G
    A.children[2].children[0].addChild("J")

    dfs_path = []
    A.depthFirstSearch(dfs_path)
    print("dfs_path", dfs_path)
    assert dfs_path == ["A", "B", "E", "F", "H", "I", "C", "D", "G", "J"]
