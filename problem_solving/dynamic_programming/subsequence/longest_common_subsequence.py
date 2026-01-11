"""
1) LCS Length (Classic)

Given two strings text1, text2
Return the length of the Longest Common Subsequence.

Example:
text1 = "abcde", text2 = "ace" → output 3 ("ace")
"""

"""
   ""  a b c d e  
""  0  0 0 0 0 0 
a   0  1 1 1 1 1 
b   0  1 2 2 2 2
e   0  1 2 2 2 3
"""


def lcs(s1, s2):
    s1_len = len(s1)
    s2_len = len(s2)
    dp = [[0 for _ in range(s2_len + 1)] for _ in range(s1_len + 1)]

    for i in range(1, s1_len + 1):
        for j in range(1, s2_len + 1):
            res = 0
            if s1[i - 1] == s2[j - 1]:
                res = 1
            dp[i][j] = max(dp[i - 1][j - 1] + res, dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


if __name__ == '__main__':
    s1 = "abcde"
    s2 = "ace"

    insect = set(s1) & set(s2)
    print(insect)
    print(lcs(s1, s2))

# optimization
# I need only last row like any matrix DP
# another level
# Patience Sorting / Binary Search LIS
