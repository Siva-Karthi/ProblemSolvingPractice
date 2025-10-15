import math


def maxProfitWithKTransactions(prices, k):
    """
     5 11 3 50 60 90
   0 0  0 0 0  0   0
   1 0  6 6 47 57 87
   2 0  6 6 53 63 93
   3 0  6 6 53 0  83

   output =
    """
    n = len(prices)
    dp = [[0 for _ in range(n)] for _ in range(k + 1)]

    start = 1

    for day in (1, k + 1):
        for sp_idx in range(start, n + 1):

            cur_prof = -math.inf
            prev_prof = dp[day - 1][sp_idx - 1]
            cur_prof = max(cur_prof, prev_prof)  # not trading

            for i in range(0, sp_idx):  # cal each prof while trading
                cur_prof = max(cur_prof, prices[sp_idx] - prices[i] + prev_prof)
            # cur_prof  = max(cur_prof, dp[i][j-1])
            dp[day][sp_idx] = cur_prof
        start += 1
    return dp[-1][-1]
