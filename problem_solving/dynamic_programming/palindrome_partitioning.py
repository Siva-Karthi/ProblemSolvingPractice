import math


def palindromePartitioningMinCuts(string):
    n = len(string)
    dp = [[None for _ in range(n)] for _ in range(n)]

    # len 0 - fill diagonal
    for i in range(n):
        dp[i][i] = 0
    # len 1
    for i in range(n - 1):
        if string[i] == string[i + 1]:
            dp[i][i + 1] = 0
        else:
            dp[i][i + 1] = 1

    for l in range(2, n):
        for start_idx in range(n - l):
            end_idx = start_idx + l
            cuts = math.inf
            if dp[start_idx + 1][end_idx - 1] == 0:  # if mid palindrome
                if string[start_idx] == string[end_idx]:
                    cuts = 0
                    dp[start_idx][end_idx] = 0
                    continue
            else:
                cuts = 2 + dp[start_idx + 1][end_idx - 1]

            # mid is not palindrome hence the current string wont be a palindrom any way, check the other possibilities as we inclue the current index
            for sub_str_l in range(l):
                cur_cut = dp[start_idx][start_idx + sub_str_l] + 1 + dp[start_idx + sub_str_l + 1][end_idx]
                cuts = min([cuts, cur_cut])

            dp[start_idx][end_idx] = cuts
    return dp[0][n - 1]


print(palindromePartitioningMinCuts("noonabbad"))
