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


def longestPalindromicSubstring(string):
    n = len(string)
    if n == 0:
        return ""

    dp = [[0] * n for _ in range(n)]
    res = 1
    pal = string[0]

    for i in range(n):
        dp[i][i] = 1  # single char is a palindrome

    for l in range(1, n):  # length of substring
        for i in range(n - l):
            j = i + l
            if string[i] == string[j]:
                if l == 1 or dp[i + 1][j - 1]:
                    dp[i][j] = 1
                    curr_len = j - i + 1
                    if curr_len > res:
                        res = curr_len
                        pal = string[i:j + 1]

    return pal


def myLongestPalindromicSubstring(string):
    n = len(string)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    if n == 0:
        return ""

    if n == 1:
        return string
    res = 1

    pal = string[0]

    for i in range(n):
        dp[i][i] = 1

    s = string
    for l in range(1, n - 1):  # length of ss

        for i in range(0, n - l):  # start idx
            j = i + l  # end idx

            if s[i] == s[j]:
                if l == 1:
                    dp[i][j] = 1
                    if l + 1 > res:
                        res = l + 1
                        pal = s[i:j + 1]
                else:
                    if dp[i + 1][j - 1] > 0:
                        dp[i][j] = dp[i + 1][j - 1] + 1
                        if l + 1 > res:
                            res = l + 1
                            pal = s[i:j + 1]
    # print(dp)
    return pal


if __name__ == '__main__':
    print(longestPalindromicSubstring("aca"))
    print(myLongestPalindromicSubstring("aca"))
