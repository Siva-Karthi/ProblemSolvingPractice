def longest_increasing_sub_sequence(arr):
    n = len(arr)
    l = [1] * n
    seq = [None] * n
    max_seq_ending_idx = 0
    max_seq_len = 0
    for i in range(1,n):
        for j in range(0,i):
            if arr[i] > arr[j]:
                res = l[j] + 1
                if res > l[i]:
                    l[i] = res
                    seq[i] = j
        if l[i] > max_seq_len:
            max_seq_ending_idx = i
            max_seq_len = l[i]
    return max_seq_len, build_seq(seq,max_seq_ending_idx, arr)

def build_seq(seq,idx, arr):
    res = []
    while seq[idx] is not None:
      res.append(arr[idx])
      idx = seq[idx]
    res.append(arr[idx])
    return list(reversed(res))
arr = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
print(longest_increasing_sub_sequence(arr))
