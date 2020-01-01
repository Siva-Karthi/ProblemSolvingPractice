"""
Problem

Write a function that takes in a "special" array and returns its product sum. A "special" array is a non-empty array
that contains either integers or other "special" arrays. The product sum of a "special" array is the sum of its
elements, where "special" arrays inside it should be summed themselves and then multiplied by their level of depth.

For example, the product sum of [x, y] is x + y; the product sum of [x, [y, z]] is x + 2y + 2z.

Sample input: [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
Sample output: 12 (calculated as: (5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)))

"""


def productSum(array):
    def get_prod_sum(spl_array, level=1):
        prod_sum = 0
        for elem in spl_array:
            if type(elem) == list:
                inner_sum = get_prod_sum(elem, level + 1)
                prod_sum += inner_sum * level
            else:
                prod_sum += elem * level
        return prod_sum

    return get_prod_sum(array)

# nuances inner results also multipled by level => :-)
