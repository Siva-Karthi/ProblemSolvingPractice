import math
def min_jumps(array):
    jumps = [math.inf for i in array]
    n = len(array)
    jumps[0] = 0
    seqs = [None for i in array]
    for i in range(1,n):
        for j in range(0, i):
            if j + array[j] >= i:
                if jumps[j] + 1 < jumps[i]:
                    jumps[i] = jumps[j] + 1
                    seqs[i] = j
    print("seqs ", seqs)
    return jumps[n-1], build_seqs(array, seqs, n-1)

def build_seqs(array, seqs, idx):
    res = []
    while idx != None:
        # res.append(array[idx])
        res.append(idx)
        idx = seqs[idx]
    # return list(reversed(res))
    return list(reversed(res))
