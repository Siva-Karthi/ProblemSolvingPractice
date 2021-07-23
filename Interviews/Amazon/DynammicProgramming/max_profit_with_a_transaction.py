cache = {}

def max_profit(arr, k):
    global buy
    global sell
    # base cases
    if k in cache:
        return cache[k]
    elif k == 2:
        if arr[0] < arr[1]:
            buy = 0
            sell = 1
            mp = arr[1] - arr[0]
            cache[k] = mp
            return mp
        else:
            mp = 0
            cache[k] = mp
            return 0
    else:
        # cases
        # i) already bought and sold
        profit = max_profit(arr, k - 1)
        # ii) already bought and selling today what is the price should I bought so that I can get max profit
        profit_way1 = arr[k - 1] - arr[k - 2]
        profit_way2 = arr[k - 1] - arr[k - 3]
        if (profit_way1 > profit_way2) and (profit_way1 > profit):
            buy = k - 2
            sell = k - 1
        elif (profit_way2 > profit_way1) and (profit_way2 > profit):
            buy = k - 3
            sell = k - 1

        # iii) do nothing to avoid loss
        noops = 0
        # print("profit, profit_way1, profit_way2, noops", profit, profit_way1, profit_way2, noops, k)
        mp = max(profit, profit_way1, profit_way2)
        cache[k] = mp
        return mp

if __name__ == '__main__':
    buy = -1
    sell = -1
    print("max_profit", max_profit([7,1,5,3,6,4], 6))
    print("buy at",buy)
    print("sell at",sell)
    print("cache at",cache)


