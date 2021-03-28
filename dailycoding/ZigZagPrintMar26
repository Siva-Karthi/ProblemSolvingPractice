"""
Good morning! Here's your coding interview problem for today.

This problem was asked by PayPal.

Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

For example, given the sentence "thisisazigzag" and k = 4, you should print:

4 - 2= 2
2 + 2 = 4

4 - 3 = 1
1 + 1 = 2

2 * (k  - ( i + 1))
2 * (4 - i + 1)
2 * (4 - (1 + 1))
2 * (4 - 2) =
2 * 2 = 4

2 * (4  - ( 2 + 1))
2 * (4 - 3)
2 * 1 = 2

--

k = 4
j = 1 | j = 2

k - j = 4 - j +

0 1 3 5 7 9
0 1 2 3 4 5 6

t     a     g
 h   s z   a
  i i   i z
   s     g
"""


def print_zigzag(s, k):

    # first row
    i = 0
    next_index_range = k*2 - 2 # 6
    while True:
        try:
            print(s[i], end=(next_index_range + 1) * " ")
            i += next_index_range
        except IndexError as e:
            break
    print("")
    # mid rows
    for j in range(1,k-1):
        i = j
        print(j*" " + s[j], end="")
        going_down = True
        while True:
            try:
                if going_down:
                    next_index_range = 2 * (k  - ( j + 1))
                    going_down = False
                else:
                    if j <= 1:
                        next_index_range =  2
                    elif j == 2:
                        next_index_range = 4
                    else:
                        next_index_range = j + 3
                    going_down = True
                    # print("next_index_range", next_index_range, j)
                i += next_index_range
                print(next_index_range * " " + s[i], end="")
            except IndexError as e:
                break
        print("")
    # last row
    i = k-1
    print(i * " ", end="")
    next_index_range =  k*2 - 2
    while True:
        try:
            print(s[i], end=(next_index_range + 1) * " ")
            i += next_index_range
        except IndexError as e:
            break
    print("")

if __name__ == '__main__':
    print_zigzag(s = "thisisazigzag", k = 4)
