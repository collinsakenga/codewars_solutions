def midpoint_sum(ints):
    if len(ints)<3:
        return None
    index=1
    left=sum(ints[:index])
    right=sum(ints[index+1:])
    while index<len(ints)-1: 
        if left==right:
            return index
        left+=ints[index]
        right-=ints[index+1]
        index+=1
    return None