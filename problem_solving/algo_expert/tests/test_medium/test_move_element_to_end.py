from problem_solving.algo_expert.medium.move_element_to_end import moveElementToEnd


def test_case_1():
    array = []
    toMove = 3
    expected = []
    output = moveElementToEnd(array, toMove)
    assert output == []


def test_case_2():
    array = [1, 2, 4, 5, 6]
    toMove = 3
    expected = [1, 2, 4, 5, 6]
    output = sorted(moveElementToEnd(array, toMove))
    assert output == expected


def test_case_3():
    array = [3, 3, 3, 3, 3]
    toMove = 3
    expected = [3, 3, 3, 3, 3]
    output = moveElementToEnd(array, toMove)
    assert output == expected


def test_case_4():
    array = [3, 1, 2, 4, 5]
    toMove = 3
    expectedStart = [1, 2, 4, 5]
    expectedEnd = [3]
    output = moveElementToEnd(array, toMove)
    outputStart = sorted(output[0:4])
    outputEnd = output[4:]
    assert outputStart == expectedStart
    assert outputEnd == expectedEnd


def test_case_5():
    array = [1, 2, 4, 5, 3]
    toMove = 3
    expectedStart = [1, 2, 4, 5]
    expectedEnd = [3]
    output = moveElementToEnd(array, toMove)
    outputStart = sorted(output[0:4])
    outputEnd = output[4:]
    assert outputStart == expectedStart
    assert outputEnd == expectedEnd


def test_case_6():
    array = [1, 2, 3, 4, 5]
    toMove = 3
    expectedStart = [1, 2, 4, 5]
    expectedEnd = [3]
    output = moveElementToEnd(array, toMove)
    outputStart = sorted(output[0:4])
    outputEnd = output[4:]
    assert outputStart == expectedStart
    assert outputEnd == expectedEnd


def test_case_7():
    array = [5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
    toMove = 5
    expectedStart = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
    expectedEnd = [5, 5, 5, 5, 5, 5]
    output = moveElementToEnd(array, toMove)
    outputStart = sorted(output[0:11])
    outputEnd = output[11:]
    assert outputStart == expectedStart
    assert outputEnd == expectedEnd


def test_case_8():
    array = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]
    toMove = 5
    expectedStart = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
    expectedEnd = [5, 5, 5, 5, 5, 5]
    output = moveElementToEnd(array, toMove)
    outputStart = sorted(output[0:11])
    outputEnd = output[11:]
    assert outputStart == expectedStart
    assert outputEnd == expectedEnd


def test_case_9():
    array = [5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12]
    toMove = 5
    expectedStart = [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12]
    expectedEnd = [5, 5, 5, 5, 5, 5]
    output = moveElementToEnd(array, toMove)
    outputStart = sorted(output[0:11])
    outputEnd = output[11:]
    assert outputStart == expectedStart
    assert outputEnd == expectedEnd


def test_case_10():
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2
    expectedStart = [1, 3, 4]
    expectedEnd = [2, 2, 2, 2, 2]
    output = moveElementToEnd(array, toMove)
    outputStart = sorted(output[0:3])
    outputEnd = output[3:]
    assert outputStart == expectedStart
    assert outputEnd == expectedEnd
