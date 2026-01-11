"""

Problem Statement

You are given a string s.
You need to partition the string into one or more substrings such that:

each substring is a palindrome

Return the minimum number of cuts needed to partition the string into palindrome substrings.

A cut is a split between two characters.

✅ Example 1

Input:
s = "aab"

Output:
1

Explanation:
"aa" | "b" → 1 cut

✅ Example 2

Input:
s = "a"

Output:
0

Explanation:
Already a palindrome.

✅ Example 3

Input:
s = "ab"

Output:
1

Explanation:
"a" | "b"

Constraints

1 <= len(s) <= 2000

s contains only lowercase English letters

"""
