def compute_ranks(number, games):
    dict={}
    for i in range(number):
        dict[i]=[0,0,0]
    for i in games:
        dict[i[0]][0]+=i[2]
        dict[i[0]][1]+=i[3]
        dict[i[1]][0]+=i[3]
        dict[i[1]][1]+=i[2]
        if i[2]==i[3]:
            dict[i[0]][2]+=1
            dict[i[1]][2]+=1
        elif i[2]>i[3]:
            dict[i[0]][2]+=2
        elif i[3]>i[2]:
            dict[i[1]][2]+=2
    dict={k:v for k,v in sorted(dict.items(), key=lambda x: (-x[-1][-1], -(x[-1][0]-x[-1][1]), -(x[-1][0])))}
    check=[]
    rank=cumulative=0
    res=[None]*number
    for i,j in dict.items():
        if not check or check[-1]!=j:
            rank+=cumulative+1
            cumulative=0
        else:
            cumulative+=1
        check.append(j)
        res[i]=rank
    return res