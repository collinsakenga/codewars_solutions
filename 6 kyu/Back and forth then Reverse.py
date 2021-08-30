def arrange(s):
    res=[]
    left, right=0, len(s)-1
    while left<=right:
        if left<=right:
            res.append(s[left])
            left+=1
        if left<=right:
            res.append(s[right])
            right-=1
        if left<=right:
            res.append(s[right])
            right-=1
        if left<=right:
            res.append(s[left])
            left+=1
    return res