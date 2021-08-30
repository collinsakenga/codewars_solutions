def peak_height(mountain):
    res=[1 if mountain[i][j]=="^" else 0 for i in range(len(mountain)) for j in range(len(mountain[i]))]
    if 1 not in res:
        return 0
    new=[res[i:i+len(mountain[0])] for i in range(0, len(res), len(mountain[0]))]
    start=1
    while True:
        flag=False
        for i in range(len(new)):
            for j in range(len(new[i])):
                if new[i][j]==0 and start==1 or i==0 or i==len(new)-1 or j==0 or j==len(new[i])-1:
                    continue
                if new[i-1][j]>=start and new[i+1][j]>=start and new[i][j-1]>=start and new[i][j+1]>=start:
                    flag=True
                    new[i][j]+=1
        if not flag:
            break
        start+=1
    return start