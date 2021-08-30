def strings_in_max_depth(s):
    maxi=cur=0
    res=[]
    temp=[]
    for i in s:
        if i in "()":
            if cur>maxi:
                res=["".join(temp)]
                maxi=cur
            elif cur==maxi:
                res.append("".join(temp))
            cur+=1 if i=="(" else -1
            temp=[]
        else:
            temp.append(i)
    return res if res else ["".join(temp)]
