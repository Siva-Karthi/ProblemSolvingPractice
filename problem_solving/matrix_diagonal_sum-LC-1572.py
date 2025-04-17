matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
];

"""
d1 = 10
d2 = 20
"""


def add_diagonals(matrix, n):
    """
    start from 0,0 end in n,n
    at each step increment x, y
    :param matrix:
    :param n:
    :return:
    """
    x = 0
    y1 = 0
    y2 = n - 1
    pds = 0
    cds = 0
    while x < n:
        pds += matrix[x][y1]
        cds += matrix[x][y2]
        x += 1
        y1 += 1
        y2 -= 1
    return pds, cds


"""
input  = 5
output  = "5"
builtin str()
"""

if __name__ == '__main__':
    n = len(matrix)
    print("primary diagonal sum", add_diagonals(matrix, n))
    # todo : total diagonal sum, handle odd num (centre caluculated twice) and
