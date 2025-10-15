from .palindrome_partitioning import palindromePartitioningMinCuts


def test_base():
    inp = "a"
    res = palindromePartitioningMinCuts(inp)
    assert res == 0


def test_small1():
    inp = "abc"
    res = palindromePartitioningMinCuts(inp)
    assert res == 2


def test_small2():
    inp = "aba"
    res = palindromePartitioningMinCuts(inp)
    assert res == 0


def test_large():
    inp = "noonabbad"
    res = palindromePartitioningMinCuts(inp)
    assert res == 2
