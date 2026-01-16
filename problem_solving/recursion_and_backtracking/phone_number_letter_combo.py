"""

The Problem
Given a string containing digits from 2-9 inclusive (like on an old telephone keypad),
return all possible letter combinations that the number could represent.

"""


def letterCombinations(digits):
    if not digits:
        return []

    # Mapping of digits to letters
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    results = []

    def backtrack(index, path):
        # goal
        # print("path = ", path, len(path) == len(digits), len(path) , len(digits))
        if len(path) == len(digits):
            results.append("".join(path))
            return

        cur_dig = digits[index]
        dig_choices = phone_map[cur_dig]
        for choice in dig_choices:
            # select option
            path.append(choice)
            backtrack(index=index + 1, path=path)
            # unselect option
            path.pop()

    backtrack(index=0, path=[])
    return results


if __name__ == '__main__':
    digits = "23"
    print(letterCombinations(digits))
