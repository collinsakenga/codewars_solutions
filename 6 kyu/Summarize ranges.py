def summary_ranges(nums):
    res=sorted(set(nums))
    index=0
    check=[]
    solutions=[]
    while index<len(res):
        if index>0 and res[index]-check[-1]!=1:
            solutions.append(str(check[0])) if len(check)==1 else solutions.append(f"{check[0]}->{check[-1]}")
            check=[res[index]]
        else:
            check.append(res[index])
        index+=1
    return [] if not nums else solutions+([str(check[0])] if len(check)==1 else [f"{check[0]}->{check[-1]}"])