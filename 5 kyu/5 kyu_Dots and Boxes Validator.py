def dots_and_boxes(ar):
    start=3
    check=12
    temp=12
    while True:
        if temp==len(ar):
            break
        temp+=check
        check+=4
        start+=1
    scoreboard=[[-1]*(start-1) for i in range(start-1)]
    flag=[[False]*(start-1) for i in range(start-1)]
    res=[[0]*(start*2-1) for i in range(start*2-1)]
    player=True
    for i in ar:
        check=False
        y=min(i[0], i[1])
        if abs(i[0]-i[1])==1:
            res[y//start*2][(y%start)*2]=1
            res[y//start*2][(y%start)*2+1]=1
            res[y//start*2][(y%start)*2+2]=1
        elif abs(i[0]-i[1])==start:
            res[y//start*2][(y%start)*2]=1
            res[y//start*2+1][(y%start)*2]=1
            res[y//start*2+2][(y%start)*2]=1
        for j in range(len(flag)):
            for k in range(len(flag)):
                if flag[j][k]:
                    continue   
                if res[j*2][k*2]==res[j*2][k*2+1]==res[j*2][k*2+2]==res[j*2+1][k*2]==res[j*2+1][k*2+2]==res[j*2+2][k*2]==res[j*2+2][k*2+1]==res[j*2+2][k*2+2]==1:
                    flag[j][k]=True
                    scoreboard[j][k]=1 if player else 2
                    check=True
        if check: continue
        player=not player
    final=[0,0]
    for i in scoreboard:
        for j in i:
            if j==1:
                final[0]+=1
            elif j==2:
                final[1]+=1
    return tuple(final)