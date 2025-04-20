def reverseWordsInString(string):
    if not string:
        return string
    stack = []
    res = ""
    word = ""
    for i in string:
        print("i = ", i)
        if i != " ":
            word += i
        else:  # white space push word
            stack.append(word)
            stack.append(" ")
            word = ""
    if word:
        stack.append(word)

    print(stack)
    while stack:
        res += stack.pop()
    return res


if __name__ == '__main__':
    print(reverseWordsInString("siva     is working!"))
