def get_count(n):
    count = 0
    count2 = 0
    s = str(n)
    total = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if int(s[count:count+1+count2]) != 0:
                if n % int(s[count:count+1+count2]) == 0:
                    total += 1
            count += 1
        count = 0
        count2 += 1
    total -= 1
    return total
