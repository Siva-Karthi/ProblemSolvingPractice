def max_increasing_sub_sum_no_adj(array):
    n = len(array)
    dp = [[0,0] for i in range(n)]
    dp[0][0] = 0
    dp[0][1] = array[0]
    for i in range(1,n):
        dp[i][1] = dp[i-1][0] + array[i]
        dp[i][0] = max(dp[i-1][0] , dp[i-1][1])
    return max([dp[n-1][0] , dp[n-1][1]])

print(max_increasing_sub_sum_no_adj([ 5, 5, 10, 100, 10, 5 ])) # 110
