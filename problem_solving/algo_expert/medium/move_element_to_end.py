"""
Move Element To End
You are given an array of integers and an integer. Write a function that moves all instances of that integer
in the array to the end of the array. The function should perform this in place and does not need to maintain
the order of the other integers.

Sample input: [2, 1, 2, 2, 2, 3, 4, 2], 2
Sample output: [1, 3, 4, 2, 2, 2, 2, 2] (the numbers 1, 3, and 4 could be ordered differently)

"""


# time = O(N log(N)) for sorting | space = O(1) #todo confirm by checking video explanation
def moveElementToEnd(array, toMove):
    array.sort()
    i = 0
    last = len(array) - 1
    while i < last and array[i] != array[last]:
        if array[i] == toMove:
            # swap toMove with respective last element
            array[i], array[last] = array[last], array[i]
            i += 1
            last -= 1
        else:
            i += 1
    return array
