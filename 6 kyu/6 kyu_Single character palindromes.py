def solve(s):
    if palindrome(s):
        return "OK"
    index = 0
    check = ""
    while index < len(s):
        check = s[0:index]+s[index+1:]
        if palindrome(check):
            return "remove one"
        index += 1
    return "not possible"


def palindrome(string):
    start = 0
    end = len(string)-1
    while start <= end:
        if string[start] != string[end]:
            return False
        end -= 1
        start += 1
    return True
