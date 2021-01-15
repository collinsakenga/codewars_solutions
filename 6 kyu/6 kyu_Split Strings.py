def solution(s):
    s=s+"_"*(len(s)%2)
    return [s[i:i+2] for i in range(0, len(s), 2)]