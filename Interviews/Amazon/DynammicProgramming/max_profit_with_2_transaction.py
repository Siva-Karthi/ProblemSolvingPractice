def max_profit(arr, k, ta = 2):
    for t in range(ta):
        maxStill = 0
        for day in range(1,k+1):
            maxYesterday = profits[t][day-1]
            maxToday = arr[day] + max([profits[t-1][i] - arr[day] for i in range(day)])
            profits[t][day] = max(maxStill,maxToday)

if __name__ == '__main__':
    N = 7
    TA = 2
    profits = [[0]*N for i in range(TA)]
    print(profits)
    # buy = -1
    # sell = -1
    print("max_profit", max_profit([ 12,13,15,2,7,8,1], N, 2))
    # print("buy at",buy)
    # print("sell at",sell)
    # print("cache at",cache)


