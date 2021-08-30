def longest_palindrome(s):
    longest=0
    comp=0
    for i in range(0,len(s)):
        for j in range(i,len(s)):
            check=i
            check2=j
            while True:
                if check>check2:
                    break
                if s[check]==s[check2]:
                    if check==check2:
                        longest+=1
                    else:
                        longest+=2
                else:
                    longest=0
                    break
                check+=1
                check2-=1                    
            if longest>comp:
                comp=longest
            longest=0
    return comp