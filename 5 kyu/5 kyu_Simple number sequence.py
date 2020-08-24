def missing(s):
    index = 1
    numbers = []
    flag = True
    miss = len(s)
    comp = 0
    while index < len(s)//2+1:
        index2 = index
        rec = int(s[0:index])
        numbers.append(rec)
        while index2 < len(s):
            if comp >= 2:
                break
            if len(str(rec+2)) > len(str(rec)) and flag:
                if (str(rec+1)) == s[index2:index2+index]:
                    flag = True
                else:
                    index += 1
                    flag = False
            if (int(s[index2:index2+index])-rec) >= 2 or (int(s[index2:index2+index])-rec) <= 0:
                comp += 1
            rec = int(s[index2:index2+index])
            numbers.append(rec)
            index2 += index
        if not flag:
            index -= 1
        index += 1
        flag = True
        miss = min(comp, miss)
        if miss <= 1:
            break
        numbers = []
        comp = 0
    if not numbers:
        return -1
    for i in range(0, len(numbers)-1):
        if numbers[i+1]-numbers[i] == 2:
            return numbers[i]+1
    return -1
