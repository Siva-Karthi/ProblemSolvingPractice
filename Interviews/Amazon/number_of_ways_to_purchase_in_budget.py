import os
shirts = [100, 15, 2000, 3500]
trousers = [550, 7000]
vests = [70 , 6]
budget = 1000


"""
x + y <= 900
y = (900 - x)
z = 900 - y - x

x *  (900 - x) * (900 - (900 - x) - x)

t += x * get_t(900 - x) * get_vests(900 - get_t(900 - x) - x)
"""

vests_cache = {}

def get_vests(budget):
    if budget in vests_cache:
        return vests_cache[budget]
    else:
        c = 0
        for i in vests:
            if i <= budget:
                c += 1
        vests_cache[budget] = c
        return c

t_cache = {}
def get_t(budget):
    if budget in t_cache:
        return t_cache[budget]
    c = 0
    for t in trousers:
        c += get_vests(budget - t)
        t_cache[budget] = c
    os.walk()
    return c

def no_of_ways_to_purchase_in_budget():
    ways = 0
    for x in shirts:
        # print("x = ", x)
        # print("y = ",  get_t(budget - x), budget - x)
        # print("z = ", get_vests(budget - (get_t(budget - x) + x)))
        # print("ans = ", get_t(budget - x) * get_vests(budget - get_t(budget - x) - x))
        # ways += get_t(budget - x) * get_vests(budget - get_t(budget - x) - x)
        ways += get_t(budget - x) # * get_vests(budget - get_t(budget - x) - x)
    return ways

if __name__ == '__main__':
    no_of_ways = no_of_ways_to_purchase_in_budget()
    print("answer is ", no_of_ways)
