def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return "Not valid"
    elif num <= 16:
        return 11
    elif is_palin(str(num)):
        return num
    index = 1
    while index < num:
        if is_palin(str(num+index)):
            return num+index
        elif is_palin(str(num-index)):
            return num-index
        index += 1


def is_palin(s):
    return s[::-1] == s
