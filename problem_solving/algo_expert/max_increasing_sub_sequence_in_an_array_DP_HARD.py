
def max_increasing_sub_seq(array):
    max_sum_id = 0
    sums = array[:]
    seq = [None for i in array]
    for i in range(len(array)):
        for j in range(0, i):
            if array[i] > array[j]:
                if sums[j] + array[i] > sums[i]:
                    sums[i] = sums[j] + array[i]
                    seq[i] = j
        if sums[i] > sums[max_sum_id]:
            max_sum_id = i
    return sums[max_sum_id], build_seq(seq, max_sum_id, array)


def build_seq(seq, curr, array):
    res = []
    while curr is not None:
        res.append(array[curr])
        curr = seq[curr]
    return list(reversed(res))


# print("get_jira_dict", get_jira_dict())
print("max subseq_sum", max_increasing_sub_seq([8,12,2,3,15,5,7]))
