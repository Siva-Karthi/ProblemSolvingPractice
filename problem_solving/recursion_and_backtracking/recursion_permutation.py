def compute_powerset(array):
	res = []
	# if not array:
	# 	return [[]]
	n = len(array)
	helper(array, res, 0,[], n)
	return res

def helper(array, res, idx, current, n):	
	if idx == n:
		res.append(current)
		return

	helper(array, res, idx+1, current, n) # exclude
	helper(array, res, idx+1, current+[array[idx]], n) # include


if __name__ == '__main__':
	array = [1,2]
	print(array)
	print(compute_powerset(array))

	array = [1,2,3]
	print(array)
	print(compute_powerset(array))

	array = [1,2,3,4]
	print(array)
	print(compute_powerset(array))