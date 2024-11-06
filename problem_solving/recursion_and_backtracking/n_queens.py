def nonAttackingQueens(n):
    res = []
    # selected_cols={i:False for i in range(n)}
    selected_cols = [[False for i in range(n)] for i in range(n)]
    helper(n, 0, selected_cols, res)
    return len(res)


def validate_position(row, col, selected_cols, n):
    # validate col
    # if col in selected_cols and selected_cols[col] == True:
    #     print(row * "\t","validate col failed", col in selected_cols, selected_cols[col],selected_cols)
    # return False
    i = row
    j = col
    while i >= 0:
        if selected_cols[i][j] == True:
            return False
        i -= 1
    # ignore selected left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if selected_cols[i][j] == True:
            print(row * "\t", "validate left diagonal failed", i, j, selected_cols)
            return False
        i -= 1
        j -= 1
    # ignore selected right diagonal
    i = row
    j = col
    while i >= 0 and j < n:
        if selected_cols[i][j] == True:
            print(row * "\t", "validate right diagonal failed", i, j, selected_cols)
            return False
        i -= 1
        j += 1
    return True


def helper(n, row, selected_cols, res):
    # base condition
    print(row * "\t", " ", "checking queen", row)
    if (row == n):
        res.append(1)
        print("res", res)
        # validate and update res - should be valid as each
        # is a valid placement
        return
        # explore choices
    for i in range(n):  # cols
        # ignore selected col
        print(row * "\t", " ", "checking pos", row, i)
        is_valid = validate_position(row, i, selected_cols, n)
        # if there is no placement ignore the cell
        print(row * "\t", " ", "isvalid", is_valid)
        if is_valid == False:
            continue  # power of backtracking
        selected_cols[row][i] = True
        helper(n, row + 1, selected_cols, res)
        selected_cols[row][i] = False


if __name__ == '__main__':
    print(nonAttackingQueens(10))
