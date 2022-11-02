import math
def compute_crossing(arr, l, r, mid):
    l_tot = -math.inf
    tot = 0
    max_left = None
    for i in range(mid, l , -1):
        tot = tot + arr[i]
        if tot > l_tot:
            l_tot = tot
            max_left = i
    r_tot = -math.inf
    tot = 0
    max_right = None
    for i in range(mid + 1, r):
        tot += arr[i]
        if tot > r_tot:
            r_tot = tot 
            max_right = i
    return max_left, max_right, l_tot + r_tot

def dc_recur_helper(arr, l, r):
    if (l == r):
        return l,r,arr[l]
    tot = 0
    # 3 cases l to mid, mid + 1 to r, crossing mid 
    mid = (l + r) // 2
    print("mid", mid, l, r) 
    l_start, l_end, l_tot = dc_recur_helper(arr, l, mid)
    r_start, r_end, r_tot = dc_recur_helper(arr, mid + 1, r)
    cross_start, cross_end, cross_tot = compute_crossing(arr, l, r, mid)
    if l_tot >= r_tot >= cross_tot:
        return l_start, l_end, l_tot
    elif r_tot >= l_tot >= cross_tot:
        return r_start, r_end, r_tot
    else:
        return cross_start, cross_end, cross_tot
arr = [3,-5,4,8,9,-5]
print("len", len(arr))
print("res = ", dc_recur_helper(arr, 0, len(arr) - 1))
