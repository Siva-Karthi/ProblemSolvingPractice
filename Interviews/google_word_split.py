def word_split(w, d):
	if not w or not d:
		return -1
	n = len(w)
	dp = [[False for _ in range(n)] for _ in range(n)]
	selections = [[None for _ in range(n)] for _ in range(n)]
	for i in range(n):
		if w[i] in d:
		    dp[i][i] = True
		    selections[i][i] = i
	if len(w) == 1:
		return dp[0][n-1]
	for l in range(1, n):
		for i in range(0, n-l):
			j = i + l
			if w[i:j+1] in d:
			    dp[i][j] = True
			    selections[i][i] = None
			for k in range(i,j):
				# if w[i:k] in d and w[k+1:j] in d:
				if dp[i][k] and dp[k+1][j]:
				    dp[i][j] = True or dp[i][j]
				    selections[i][i] = k
	print(dp)
	return dp[0][n-1]

print("res = ",word_split("pythoncompiler", ["python", "compiler"]))
