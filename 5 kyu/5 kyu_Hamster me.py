def hamster_me(code, message):
    temp = sorted(set(code))
    dict = {}
    total = 0
    for i in range(len(temp)-1):
        count = 1
        dict[temp[i]] = temp[i]+str(count)
        while chr(ord(temp[i])+count) < chr(ord(temp[i+1])):
            dict[chr(ord(temp[i])+count)] = temp[i]+str(count+1)
            count += 1
        total += count
    for i in range(26-total):
        dict[chr(ord("a")+(ord(temp[-1])-ord("a")+i) % 26)] = temp[-1]+str(i+1)
    return "".join(dict[i] for i in message)
