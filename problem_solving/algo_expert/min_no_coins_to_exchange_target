import math

def min_no_coins_to_exchange_target(coins, target):
    dp = [math.inf for i in range(target + 1)]

    dp[0] = 0

    for i in range(1, target + 1):
        for coin in coins:
            if coin <= i:
                sub_res = dp[i - coin]
                if sub_res != math.inf:
                    if 1 + sub_res < dp[i]:
                        dp[i] = 1 + sub_res
    return dp[target]
print("min_no_coins_to_exchange_target",min_no_coins_to_exchange_target([1,2,5,10] , 7) )
