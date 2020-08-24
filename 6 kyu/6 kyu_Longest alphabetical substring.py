def longest(s):
    count = 1
    comp = 1
    index = 1
    index2 = 0
    while index < len(s):
        if s[index] >= s[index-1]:
            count += 1
            if count > comp:
                comp = count
                index2 = index-comp+1
        else:
            count = 1
        index += 1
    return s[index2:index2+comp]
