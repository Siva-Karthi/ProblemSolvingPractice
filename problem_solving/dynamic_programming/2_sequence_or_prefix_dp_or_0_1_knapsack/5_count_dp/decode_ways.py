# """
# 91. Decode Ways
# Attempted
# Medium
# Topics
# premium lock icon
# Companies
# You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:
#
# "1" -> 'A'
#
# "2" -> 'B'
#
# ...
# "22" -> 'V'
# "23" -> 'W'
# "24" -> 'X'
# "25" -> 'Y'
#
# "26" -> 'Z'
#


"""
Number,Letter,,Number,Letter
1,A,
2,B,
3,C,
4,D,
5,E,
6,F,
7,G,
8,H,
9,I,
10,J,
11,K,
12,L,
13,M,
14,N,
15,O,
16,P,
17,Q,
18,R,
19,S,
20,T,
21,U,
22,V,
23,W,
24,X,
25,Y,
26,Z,
"""


# However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").
#
# For example, "11106" can be decoded into:
#
# "AAJF" with the grouping (1, 1, 10, 6)
# "KJF" with the grouping (11, 10, 6)
# The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
# Note: there may be strings that are impossible to decode.
#
# Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.
#
# The test cases are generated so that the answer fits in a 32-bit integer.
#
#
#
# Example 1:
#
# Input: s = "12"
#
# Output: 2
#
# Explanation:
#
# "12" could be decoded as "AB" (1 2) or "L" (12).
#
# Example 2:
#
# Input: s = "226"
#
# Output: 3
#
# Explanation:
#
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#
# Example 3:
#
# Input: s = "06"
#
# Output: 0
#
# Explanation:
#
# "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.
#
#
#
#
# """
#
#
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         dp = [0 for _ in range(n)]
#         # base cases
#         if (s[0] == "0"):
#             return 0
#
#         dp[0] = 1
#         for i in range(1, n):
#             res = 0
#             if s[i] == "0":
#                 if s[i - 1] == "1" or s[i - 1] == "2":
#                     res = dp[i - 1]  # just take it from prev
#                 else:  # invalid
#                     return 0
#             else:
#                 if int(s[i]) > 6 and int(s[i - 1]) >= 2:
#                     res = dp[i - 1]
#                 else:
#                     res = dp[i - 1] + 1
#             dp[i] = res
#         return dp[n - 1]


# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         if n == 1:
#             return 1
#         dp = [0 for _ in range(n)]
#         # base cases
#         if (s[0]  == "0"):
#             return 0
#         dp[0] = 1
#         if s[1] == "0":
#             dp[1] = 1
#         elif int(s[1]) >=7 and int(s[0]) >=2:
#             dp[1] = 1
#         else:
#             dp[1] = 2
#         # handle index 1 also
#         for i in range(2,n):
#             dp[i] = 0
#             # handle when I can't take i-1 and i-2
#             """
#             106 - JF
#             216 - BAF
#                   UF
#                   BP
#             217 - 2 17 | 21 7 | 2 1 7 = 3
#             227 - 2 2 7 | 22 7
#             237 - 2 3 7 | 23 7 = 2
#             """
#             if s[i] == "0":
#                 # dp[i] = dp[i-1]
#                 dp[i] = dp[i - 2]
#             elif s[i-1] == "0":
#                 dp[i] = dp[i-1]
#             elif int(s[i]) >=7 and int(s[i - 1]) >=2:
#                 dp[i] = dp[i-1]
#             else:
#                 dp[i] = dp[i-1] + dp[i-2]
#         print(dp)
#         return dp[-1]

#
# class Solution:
#     def numDecodings(self, s: str) -> int:
#         n = len(s)
#         if n == 0:
#             return 0
#
#         dp = [0] * (n + 1)
#
#         dp[0] = 1                      # empty string
#         dp[1] = 0 if s[0] == "0" else 1
#
#         for i in range(2, n + 1):
#             one = s[i - 1]             # single char
#             two = s[i - 2:i]           # two chars
#
#             # single digit decode (1..9)
#             if one != "0":
#                 dp[i] += dp[i - 1]
#
#             # two digit decode (10..26)
#             if "10" <= two <= "26":
#                 dp[i] += dp[i - 2]
#
#         return dp[n]

# space optimized
class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0 or s[0] == "0":
            return 0

        prev2 = 1  # dp[i-2]
        prev1 = 1  # dp[i-1]

        for i in range(1, n):
            curr = 0

            if s[i] != "0":
                curr += prev1

            if "10" <= s[i - 1:i + 1] <= "26":
                curr += prev2

            prev2, prev1 = prev1, curr

        return prev1


if __name__ == '__main__':
    s = Solution()
    inp = "12"
    inp = "06"
    inp = "106"  # 10 6
    # inp = "216"
    # inp = "217"
    # inp = "227"
    # inp = "237"
    # # inp = "60" #
    inp = "2101"  # 2 10 1
    inp = "1201234"
    print(s.numDecodings(inp))
