def palindrome(num, s):
    if not isinstance(num, int) or not isinstance(s, int) or num < 0 or s < 0:
        return "Not valid"
    res = []
    temp = 11 if num < 11 else num
    while len(res) < s:
        if int(str(temp)[::-1]) == temp:
            res.append(temp)
        temp += 1
    return res
