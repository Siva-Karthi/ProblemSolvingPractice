from pprint import pprint


def numberOfWaysToMakeChange(n, denoms):
    dp = [0] * (n + 1)
    dp[0] = 1  # One way to make 0

    for coin in denoms:
        import pdb
        pdb.set_trace()
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]
    print("dp")
    pprint(dp)
    return dp[n]


print(numberOfWaysToMakeChange(3, [1, 2]))
