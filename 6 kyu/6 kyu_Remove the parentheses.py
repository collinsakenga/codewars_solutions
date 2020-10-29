def remove_parentheses(s):
    first=0
    res=""
    for i in s:
        if i=="(":
            first+=1
        if not first:
            res+=i
        if i==")":
            first-=1
    return res