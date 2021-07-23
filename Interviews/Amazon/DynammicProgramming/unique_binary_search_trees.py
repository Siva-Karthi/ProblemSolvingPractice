class Solution:
    def numTrees(self, n: int) -> int:
        res = [0 for i in range(n+1)]
        res[0] = 1
        res[1] = 1
        for i in range(2,n+1):
            for j in range(0, i):
                res[i] += res[j] * res[i-j-1]
        print(res)
        return res[n]