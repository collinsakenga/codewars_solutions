def target_game(values):
    n2=n1=0
    for i,j in enumerate(values[::-1]):
        if i%2==0:
            cur=max(j+n1, n2)
            n1=cur
        else:
            cur=max(n1, n2+j)
            n2=cur
    return max(n1, n2)