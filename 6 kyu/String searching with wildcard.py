def find(needle, haystack):
    for i in range(len(haystack)-len(needle)+1):
        flag=True
        for j,char in enumerate(needle):
            if char=="_":
                continue
            elif char!=haystack[i+j]:
                flag=False
                break
        if flag:
            return i
    return -1