def custom_int_str(num: int) -> str:
    """
    get each digits and concatenate the respective str representation
    :param num:
    :return:
    100
    100 % 10 =
    """
    str_repr = ""
    mapping = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if num < 10:
        return mapping[num]
    while num > 9:
        d = num % 10
        str_repr = mapping[d] + str_repr
        num = num // 10
    str_repr = mapping[num] + str_repr
    return str_repr


if __name__ == '__main__':
    str_num = custom_int_str(54321)
    print(str_num, type(str_num))
    # todo try str to int
    # ASCII manipulation,
    # modulus / division logic,
    # handling
    # negatives and zeros
    # try ascii based char(ord('0') + digit) # to optmise space
    # https://leetcode.com/problems/string-to-integer-atoi/description/
