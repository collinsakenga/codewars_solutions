def dig_pow(n, p):
    s = str(n)
    num = 0
    index = -1
    for j in range(len(s)):
        num += int(s[j])**(j+p)
    if num % n == 0:
        index = num/n
    return index
