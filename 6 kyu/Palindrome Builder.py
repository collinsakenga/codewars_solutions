def build_palindrome(s):
    if palindrome(s): return s
    flag=True
    res=""
    for i in range(1,len(s)+1):
        if palindrome(s[0:i]):
            res=s[0:i]
    for i in range(len(s)-1,-1,-1):
        if palindrome(s[i:len(s)]) and len(s[i:len(s)])>len(res):
            res=s[i:len(s)]
            flag=False
    return s+s[0:len(s)-len(res)][::-1] if not flag else s[len(res):][::-1]+s
def palindrome(s):
    index=0
    index2=len(s)-1
    while index<=index2:
        if s[index]!=s[index2]:
            return False
        index+=1
        index2-=1
    return True