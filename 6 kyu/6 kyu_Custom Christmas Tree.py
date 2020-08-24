def custom_christmas_tree(chars, n):
    s = ""
    temp = []
    index = 0
    rec = len(chars)
    for i in range(n):
        for space in range(n-i-1):
            s += " "
        for j in range(i+1):
            temp.append(chars[index % rec])
            index += 1
        s += " ".join(temp)
        s += "\n"
        temp = []
    for i in range(n//3):
        for space in range(n-1):
            s += " "
        s += "|"
        s += "\n"
    print(s[:-1])
    return s[:-1]
