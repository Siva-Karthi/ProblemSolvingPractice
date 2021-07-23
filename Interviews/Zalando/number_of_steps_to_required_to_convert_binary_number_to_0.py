"""
Given a binary string str, the task is to print the numbers of steps required to convert it to one by the following operations:

If ‘S’ is odd add 1 to it.
If ‘S’ is even divide it by 2.

Input: str = “1001001”
Output: 12

Input: str = “101110”
Output: 8

Number ‘101110’ is even, after dividing it by 2 we get an odd number ‘10111’ so we will add 1 to it. Then we’ll get ‘11000’ which is even and can be divide three times continuously in a row and get ’11’ which is odd, adding 1 to it will give us ‘100’ which is even and can be divided 2 times in a row. As, a result we get 1.
So 8 times the above two operations were required in this number.

Example 7
111 - 7
    7 - 1  = 6
    6 / 2 = 3
    3 - 1 = 2
    2 / 2 = 0


1000 - 8
    8 / 2 = 4
    4 / 2 =  2
    2 / 2 = 1
    1 - 1 = 0

1001 = 9

    9 - 1 = 8
    8 / 2 = 4
    4 / 2 = 2
    2 / 2 = 1
    1- 1 = 0

1010
    10 / 2 = 5
    5 - 1 = 4
    4 / 2 = 2
    2 / 2 = 1
    1 - 1 = 0
"""

"""
2 = 1
3 = 2
4 = 2 
5 = 3
6 = 3
7 = 4
8 = 3
9 = 4
10 = 4
"""
def calc(S):
    return 0


if __name__ == '__main__':
    s = "10000100000"
    res = calc(s)
    print(res)