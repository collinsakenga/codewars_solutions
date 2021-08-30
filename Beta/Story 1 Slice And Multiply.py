def solve(string, times):
    res=""
    for j in string.lower():
        if not j.isalpha():
            res+=j
            continue
        res+=str((ord(j)-ord("a"))*times)
    return res[:times]