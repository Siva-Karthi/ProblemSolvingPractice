"""
91. Decode Ways
Attempted
Medium
Topics
premium lock icon
Companies
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.




"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n)]
        # base cases
        if (s[0] == "0"):
            return 0

        dp[0] = 1
        for i in range(1, n):
            res = 0
            if s[i] == "0":
                if s[i - 1] == "1" or s[i - 1] == "2":
                    res = dp[i - 1]  # just take it from prev
                else:  # invalid
                    return 0
            else:
                if int(s[i]) > 6 and int(s[i - 1]) >= 2:
                    res = dp[i - 1]
                else:
                    res = dp[i - 1] + 1
            dp[i] = res
        return dp[n - 1]
