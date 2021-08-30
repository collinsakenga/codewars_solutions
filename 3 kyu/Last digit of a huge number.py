def last_digit(lst):   
    if not lst: return 1
    elif len(lst)==1: return lst[0]%10
    delete=len(lst)-1
    while len(lst)>2:
        if lst[delete]==0:
            lst[delete-1]=1
        elif lst[delete-1]==0:
            lst[delete-1]=0
        else:
            x=lst[delete-1]%4
            if x==0:
                x=4
            elif x==1:
                x=lst[delete-1]
            elif x==2:
                x=4 if lst[delete] >1 else 2
            elif x==3:
                x=3 if lst[delete]%2!=0 else 1
            lst[delete-1]=x
        lst.pop(-1)
        delete-=1
    return (((lst[0]%10)**(lst[1]))%10)