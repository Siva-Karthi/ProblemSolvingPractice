"""

Given a string s, find the length of the longest subsequence of s that is a palindrome.

A subsequence is a sequence that can be derived from the string by deleting some characters without changing the order of the remaining characters.

✅ Return

Return an integer — the length of the longest palindromic subsequence in s.

Example 1

Input:
s = "bbbab"
Output:
4
Explanation:
One possible longest palindromic subsequence is "bbbb".

Example 2

Input:
s = "cbbd"
Output:
2
Explanation:
One possible longest palindromic subsequence is "bb".

Constraints

1 <= s.length <= 1000

s contains only lowercase English letters.

"""

"""
    "" c b b d
""   0 0 0 0 0
c    0 1 0 1 2
b    0 0 2 2 2
b    0 0 0 1 2 
d    0 0 0 0 1
"""


def lps(s):
    n = len(s)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for l in range(1, n + 1):  # length
        for i in range(0, n - l + 1):  # start
            j = i + l - 1  # end
            print(i, j)
            if i == j:
                dp[i][j] = 1
            elif s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]


def try_loop(s):
    n = len(s)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for l in range(1, n):
        # print(l) # 1 , 2, 3
        # for s in range(l,n+1):
        for s in range(0, n - l):
            e = s + l
            # print(f"l = {l} s={s} e={e}")
            print(f"s={s} e={e}")
            """
            1
            2
            3
            """
            pass

    for gap in range(1, n):  # gap = end - start
        for start in range(0, n - gap):
            end = start + gap
            print(start, end)


if __name__ == '__main__':
    s = "cbbd"
    # s = "bbbab"
    # print(lps(s))
    print(try_loop(s))
