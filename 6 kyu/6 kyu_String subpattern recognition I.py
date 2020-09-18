def has_subpattern(string):
    count = 1
    while count < len(string)//2:
        if len(string) % count != 0:
            count += 1
            continue
        temp = string[:count]
        flag = True
        for i in range(count, len(string), count):
            if string[i:i+count] != temp:
                flag = False
                break
        if flag:
            return True
        count += 1
    return False
