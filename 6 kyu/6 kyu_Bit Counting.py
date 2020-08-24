def countBits(n):
    s = str("{0:b}".format(n))
    count = 0
    for i in range(len(s)):
        if s[i] == '1':
            count += 1
    return count
