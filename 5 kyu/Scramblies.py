def scramble(s1, s2):    
    hash=[0]*26
    for i in set(s2):
        hash[ord(i)-ord("a")]+=s1.count(i)
        hash[ord(i)-ord("a")]-=s2.count(i)
        if hash[ord(i)-ord("a")]<0:
            return False
    return True