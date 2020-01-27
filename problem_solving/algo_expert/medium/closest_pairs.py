from math import inf


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    l1 = len(arrayOne)
    l2 = len(arrayTwo)

    left = 0
    right = 0
    pairs = []
    _min = inf

    while left < l1 and right < l2:
        curr_abs_diff = abs((arrayOne[left]) - (arrayTwo[right]))
        if curr_abs_diff == 0:
            pairs[0] = arrayOne[left]
            pairs[1] = arrayTwo[right]
            break

        if curr_abs_diff <= _min:
            _min = curr_abs_diff
            pairs = [arrayOne[left], arrayTwo[right]]

        if arrayOne[left] < arrayTwo[right]:
            left += 1
        else:
            right += 1
    return pairs
