def solve(s):
    total=0
    for i in range(len(s)):
        for j in range(len(s)-i):
            if int(s[j:j+i+1])%2:
                total+=1
    return total