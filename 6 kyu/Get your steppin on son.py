def word_step(s):
    res=s.split()
    width=sum(len(res[i])-1 for i in range(0, len(res), 2))+1
    height=sum(len(res[i])-1 for i in range(1, len(res), 2))+1
    solution=[[" "]*width for i in range(height)]
    x=y=0
    for i,j in enumerate(res):
        for k,l in enumerate(j):
            if i%2==0:
                solution[y][x+k]=l
            else:
                solution[y+k][x]=l
        if i%2==0:
            x+=len(j)-1
        else:
            y+=len(j)-1
    return solution