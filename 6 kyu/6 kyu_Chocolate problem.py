def chocolate(n, first_bar, second_bar):
    temp={j:i for i,j in enumerate(second_bar)}
    index=check=total=0
    while index<n:
        if index>0 and temp[first_bar[index]]-check!=1:
            total+=1
        check=temp[first_bar[index]]
        index+=1 
    return total