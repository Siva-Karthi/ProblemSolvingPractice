from collections import OrderedDict


# time O(n) | space = O(1)?
def nth_non_repeating_char(string, pos=1):
    # normal dict also will work in pythoon3.7, for safe side using OrderedDict
    my_dict = OrderedDict()
    for char in string:
        if char in my_dict:
            my_dict.pop(char)
        else:
            my_dict[char] = 1

    # optimize this since O(n) and TypeError: 'odict_keys' object is not subscriptable to do my_dict.keys()[n] (then need to handle index error)
    i = 1
    for k, v in my_dict.items():
        if i == pos:
            return k
        i += 1
