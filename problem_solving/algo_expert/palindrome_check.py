# O(n) time | O(1) space ??? it should be O(n/2) right
def isPalindrome(string):
    is_palidrome = True
    start = 0
    end = len(string) - 1
    while start < end:  # ignoring mid
        if string[start] != string[end]:
            is_palidrome = False
            break
        start += 1
        end -= 1
    return is_palidrome
