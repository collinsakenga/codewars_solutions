def loneliest(strng):
    s=strng.strip()
    letter=[]
    comp=0
    for i,j in enumerate(s):
        if j==" ":
            continue
        index1=index2=i
        space_left=space_right=0
        while (index1-1)>=0 and s[index1-1]==" ":
            space_left+=1
            index1-=1
        while (index2+1)<len(s) and s[index2+1]==" ":
            space_right+=1
            index2+=1
        if (space_left+space_right)==comp:
            letter.append(j)
        elif (space_left+space_right)>comp:
            comp=space_left+space_right
            letter=[j]
    return letter