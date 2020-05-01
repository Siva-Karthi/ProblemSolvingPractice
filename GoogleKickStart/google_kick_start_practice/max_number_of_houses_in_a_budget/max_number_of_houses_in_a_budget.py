def get_max_number_of_houses(costs, budget):
    n = 0
    costs.sort()
    remaining_budget = budget

    for i in costs:
        if i <= remaining_budget:
            remaining_budget -= i
            n += 1
            if remaining_budget == 0:
                break
    return n

if __name__ == '__main__':
    T = int(input())
    for t in range(1,T+1):
        N,B = input().split(" ")
        N,B = int(N), int(B)
        costs = input().split(" ")
        costs = [int(i) for i in costs]
        print("Case #{}: {}".format(t, get_max_number_of_houses(costs,B)))