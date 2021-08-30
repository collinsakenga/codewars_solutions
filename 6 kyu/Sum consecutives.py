def sum_consecutives(s):
    result = [s[0]]
    index=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            result[index]+=s[i]
        else:
            result.append(s[i])
            index+=1
    return result