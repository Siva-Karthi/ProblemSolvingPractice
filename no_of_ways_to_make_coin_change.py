# def numberOfWaysToMakeChange(n, denoms):
#     dp = [0] * (n + 1)
#     dp[0] = 1  # One way to make 0
#
#     for coin in denoms:
#         print("coin", coin, list(range(coin, n + 1)))
#         for amount in range(coin, n + 1):
#             dp[amount] += dp[amount - coin]
#             print("\tcheck dp[{}] from dp[{}]".format(amount, amount - coin) )
#     print("dp")
#     pprint(dp)
#     return dp[n]


def numberOfWaysToMakeChange(n, denoms):
    dp = [[0 for _ in range(n + 1)] for _ in range(len(denoms) + 1)]

    for i in range(len(denoms) + 1):
        dp[i][0] = 1  # 1 way to make change for 0 (use no coins)

    for i in range(1, len(denoms) + 1):
        for j in range(n + 1):
            denom = denoms[i - 1]
            if j >= denom:
                dp[i][j] = dp[i - 1][j] + dp[i][j - denom]  # Include + exclude
            else:
                dp[i][j] = dp[i - 1][j]  # Can't include the coin

    return dp[len(denoms)][n]


print(numberOfWaysToMakeChange(12, [2, 3, 7]))
