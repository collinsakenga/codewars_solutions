def solve(s):
    s=list(s)
    s.sort()
    s=''.join(s)
    if len(s)==1:
        return True
    for i in range(1,len(s),1):
        if ord(s[i])-ord(s[i-1])!=1:
            return False
    return True