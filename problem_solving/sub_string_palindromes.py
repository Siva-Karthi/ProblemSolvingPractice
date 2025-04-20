# https://leetcode.com/problems/palindromic-substrings/?source=submission-ac
class Solution:
    dp_table = None

    def check_palindrome(self, s, l, r, ):
        ptr1 = l
        ptr2 = r
        while l < r:
            if s[l] != s[r]:
                return 0
            l += 1
            r -= 1
        return 1

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        count = 0
        for i in range(n):
            dp[i][i] = 1
            count += 1

        for l in range(1, n):  # length 1 to n
            for i in range(0, n - l):  # start index
                j = i + l
                if l == 1:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                        count += 1
                else:
                    if s[i] == s[j] and (dp[i + 1][j - 1] > 0):
                        dp[i][j] = dp[i + 1][j - 1] + 1
                        count += 1
        return count
