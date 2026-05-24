"""
maximum weight of plates for the barbell within maxCapacity
"""


def get_max_weights(weights, maxCapacity):
    """
    base cases
    0 weight  - 0
    3 cases
    cur_weight > cur_max_weight
        dp[i][j] = dp[i-1][j]
    cur_weight = cur_max_weight
        dp[i][j] = weights[i]
    cur_weight < cur_max_weight
        rem = cur_max_weight - cur_weight
        if dp[i-1][rem] != 0:
            dp[i][j] = weights[i]+dp[i-1][rem]
        else:
            dp[i][j] = dp[i][j-1]

      0 1 2 3 4 5 6 7
      # 0 0 0 0 0 0 0 0
    1 0 1 0 0 0 0 0 0
    2 0 1 2 3 3 3 3 3
    5 0
    6 0
    7 0
    :param weights:
    :param maxCapacity:
    :return:
    """
    n = len(weights)
    weights.sort()
    max_weight = 0
    dp = [[0 for _ in range(maxCapacity + 1)] for _ in range(n)]
    for i in range(n):  # row
        for j in range(1, maxCapacity + 1):  # column
            cur_weight = weights[i]
            cur_max_weight = j
            if cur_weight > cur_max_weight:
                dp[i][j] = dp[i - 1][j]
            elif cur_weight == cur_max_weight:
                dp[i][j] = weights[i]
            elif cur_weight < cur_max_weight:
                rem = cur_max_weight - cur_weight
                if dp[i - 1][rem] != 0:
                    dp[i][j] = weights[i] + dp[i - 1][rem]
                else:
                    dp[i][j] = dp[i][j - 1]
            if dp[i][j] > max_weight:
                max_weight = dp[i][j]
    return max_weight


def get_max_weights_practise(weights, maxCapacity):
    """

      0 1 2 3 4 5 6 7
      # 0 0 0 0 0 0 0 0
    1 0 1 0 0 0 0 0 0
    2 0 1 2 3 3 3 3 3
    5 0
    6 0
    7 0
    :param weights:
    :param maxCapacity:
    :return:
    """
    n = len(weights)
    weights.sort()
    max_weight = 0
    # base case
    dp = [[0 for _ in range(maxCapacity + 1)] for _ in range(n)]
    # first row
    # base case: first item
    for j in range(maxCapacity + 1):
        if weights[0] <= j:
            dp[0][j] = weights[0]

    for i in range(1, n):
        w = weights[i]
        for j in range(1, maxCapacity + 1):
            cmc = j
            # not take
            not_take = dp[i - 1][j]
            # take
            take = 0
            if w <= cmc:
                take = w + dp[i - 1][cmc - w]
            dp[i][j] = max(not_take, take)
            # if dp[i][j] > max_weight:
            #     max_weight = dp[i][j]

    return dp[n - 1][maxCapacity]

weights = [7, 1, 5, 6, 2]
maxCapacity = 7
print(get_max_weights(weights, maxCapacity))
