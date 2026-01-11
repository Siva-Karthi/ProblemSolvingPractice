class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # Base case: empty string or single character requires 0 cuts
        if n <= 1:
            return 0

        # 1. Palindrome DP Matrix (n x n)
        # dp[i][j] will be True if s[i...j] is a palindrome
        dp = [[False for _ in range(n)] for _ in range(n)]

        # Every single character is a palindrome (diagonal)
        for i in range(n):
            dp[i][i] = True

        # Fill the palindrome table using the 'distance' (l) logic
        for l in range(1, n):  # l is the distance between start (si) and end (ei)
            for si in range(0, n - l):
                ei = si + l
                if s[si] == s[ei]:
                    # CHANGED: Added logic to handle length 2 (l=1) or check inner range
                    # If l=1 (length 2), s[si]==s[ei] is enough (e.g., "aa")
                    # If l > 1, the inner substring s[si+1...ei-1] must be a palindrome
                    if l == 1 or dp[si + 1][ei - 1]:
                        dp[si][ei] = True

        # 2. 1D DP for minimum cuts
        # dp2[i] = minimum cuts needed for the prefix s[0...i]
        dp2 = [0 for _ in range(n)]

        for i in range(n):
            # If s[0...i] is already a palindrome, no cuts are needed
            if dp[0][i]:
                dp2[i] = 0
            else:
                # Initialize with maximum possible cuts (each character is a partition)
                dp2[i] = i

                # Try all possible split points 'k'
                # We check if s[0...k] followed by a cut, then a palindrome s[k+1...i]
                for k in range(i):
                    # If the suffix s[k+1...i] is a palindrome,
                    # we can use the result of dp2[k] and add 1 cut
                    if dp[k + 1][i]:
                        dp2[i] = min(dp2[i], dp2[k] + 1)

        return dp2[n - 1]


# Testing with "aab"
sol = Solution()
result = sol.minCut("aab")
print(f"Min cuts for 'aab': {result}")  # Expected: 1 (aa | b)
