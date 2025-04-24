"""
levenshteinDistance
str1 = "abc"
str2 = "yabd"
output = 2
explanation
1) insert y
2) replace c with d
"""
"""
def levenshteinDistance(str1, str2):
    # Write your code here.
    # res = fn(str1, str2, len(str1), len(str2))
	print("str1", str1, "str2", str2)
	if str1 == str2:
		res = 0
	else:
		res = fn(str1, str2, len(str1), len(str2))
	print("res", res)
    return res

def fn(str1, str2, m, n):
	if m==0:
		return n
	if n == 0:
		return m
	
	if str1[m-1]== str2[n-1]:
        return fn(str1, str2, m-1, n-1)

	return 1 + min(
		fn(str1, str2, m  , n - 1) , # insert
		fn(str1, str2, m - 1, n) , # remove
		fn(str1, str2, m - 1, n - 1)  # replace
	)
	 
def editDistance(str1, str2, m, n, d = {}):
    # print("here", str1, str2, m, n, d)
    key = m, n

    # If first string is empty, the only option
    # is to insert all characters of second
    # string into first
    if m == 0:
        return n

    # If second string is empty, the only
    # option is to remove all characters
    # of first string
    if n == 0:
        return m
    # print("here2", str1, str2, m, n)
    if key in d:
		print("here3", d)
        return d[key]
    # print("here3", str1, str2, m, n)
    # If last characters of two strings are same,
    # nothing much to do. Ignore last characters
    # and get count for remaining strings.
	# print(" str1[m - 1] == str2[n - 1]",  str1[m - 1] , str2[n - 1])
    if str1[m - 1] == str2[n - 1]:
		# print(" str1[m - 1] == str2[n - 1]",  str1[m - 1] , str2[n - 1])
        return editDistance(str1, str2, m - 1, n - 1)

    # If last characters are not same, consider
    # all three operations on last character of
    # first string, recursively compute minimum
    # cost for all three operations and take
    # minimum of three values.

    # Store the returned value at dp[m-1][n-1]
    # considering 1-based indexing
    d[key] = 1 + min(editDistance(str1, str2, m, n - 1), # Insert
                     editDistance(str1, str2, m - 1, n), # Remove
                     editDistance(str1, str2, m - 1, n - 1)) # Replace
    # print("d", d)
    return d[key]
"""


def levenshteinDistance(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    """
        ""  y   a   b   d
    ""  0   1   2   3   4
    a   1   
    b   2   
    c   3
    a to y = a - 0,
    if same 
        dp[i][j] = dp[i-1][j-1]
    not same
        dp[a][y] = 1 + min(
        dp[i-1][j-1] + 1, # replace [0][0]
        dp[i][j - 1] +1 # insert [1][0]
        dp[i - 1][j] + 1 # delete [0][1]
        )
    """
    # fill default base cases

    counter = 1
    for i in range(1, m + 1):
        dp[i][0] = counter
        counter += 1
    counter = 1
    for j in range(1, n + 1):
        print("j", j, n, str2, list(range(1, n + 1)))
        dp[0][j] = counter
        counter += 1
    for i in range(1, m + 1):  # str1 row
        for j in range(1, n + 1):  # str2 col
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min([
                    dp[i - 1][j - 1],
                    dp[i][j - 1],
                    dp[i - 1][j]])
    return dp[m][n]


print(levenshteinDistance("abc", "yabd"))
