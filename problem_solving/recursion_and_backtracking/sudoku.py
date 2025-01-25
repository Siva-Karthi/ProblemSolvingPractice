from pprint import pprint


def solveSudoku(board):
    n = len(board)
    res = []
    helper(board, n, 0, 0, res)
    if res:
        res = res[0]
    return res


def validate_choice(board, choice, i, j):
    # check in row
    row = board[i]
    if choice in row:
        return False

    # check col
    for row in board:
        if row[j] == choice:
            return False

    # check the inner matrix
    if i < 3:  # 0-2
        if j < 3:  # 0-2
            for inner_i in range(0, 3):
                for inner_j in range(0, 3):
                    if board[inner_i][inner_j] == choice:
                        return False
        elif j >= 3 and j < 6:  # 3-5
            for inner_i in range(0, 3):
                for inner_j in range(3, 6):
                    if board[inner_i][inner_j] == choice:
                        return False
        else:  # 6 - 8
            for inner_i in range(0, 3):
                for inner_j in range(6, 9):
                    if board[inner_i][inner_j] == choice:
                        return False
    elif i >= 3 and i < 6:  # 3-5
        if j < 3:  # 0-2
            for inner_i in range(3, 6):
                for inner_j in range(0, 3):
                    if board[inner_i][inner_j] == choice:
                        return False
        elif j >= 3 and j < 6:  # 3-5
            for inner_i in range(3, 6):
                for inner_j in range(3, 6):
                    if board[inner_i][inner_j] == choice:
                        return False
        else:  # 7 - 9
            for inner_i in range(3, 6):
                for inner_j in range(6, 9):
                    if board[inner_i][inner_j] == choice:
                        return False
    else:  # 7-9
        if j < 3:  # 0-2
            for inner_i in range(6, 9):
                for inner_j in range(0, 3):
                    if board[inner_i][inner_j] == choice:
                        return False
        elif j >= 3 and j < 6:  # 3-5
            for inner_i in range(6, 9):
                for inner_j in range(3, 6):
                    if board[inner_i][inner_j] == choice:
                        return False
        else:  # 7 - 9
            for inner_i in range(6, 9):
                for inner_j in range(6, 9):
                    if board[inner_i][inner_j] == choice:
                        return False
    return True


def helper(board, n, i, j, res):
    # base
    current_row = i
    current_col = j

    if current_col == n:
        current_row += 1
        current_col = 0
    if current_row == n:
        res.append([row[:] for row in board])
        return
    # print("position", current_row, current_col, board[current_row][current_col])

    # explore choices
    # for i_next in range(i,n):
    #     for j_next in range(j,n):
    if board[current_row][current_col] == 0:
        # print("position needs work", current_row, current_col, board[current_row][current_col])
        for choice in range(1, 10):
            is_valid = validate_choice(board, choice, current_row, current_col)
            # print("is_valid", is_valid, "for position", current_row, current_col, "choice", choice)
            if is_valid == True:
                # choose an option
                board[current_row][current_col] = choice
                helper(board, n, current_row, current_col + 1, res)
                # undo the choice
                board[current_row][current_col] = 0
    else:
        helper(board, n, current_row, current_col + 1, res)


if __name__ == '__main__':
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    res = solveSudoku(board)
    print("res")
    pprint(res)
