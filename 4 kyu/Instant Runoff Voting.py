def runoff(voters):
    flag=[[False]*len(voters[i]) for i in range(len(voters))]
    dict={}
    for i in voters[0]: dict[i]=0
    eliminate_list=[]
    count=0
    while count<len(voters[0]):
        for i in range(len(voters)):
            for j in range(len(voters[i])):
                if not flag[i][j]:
                    dict[voters[i][j]]+=1
                    break
        rec=sorted(dict.items(), key=lambda x: x[1])
        min=rec[count][1]
        max=rec[-1][1]
        if min==max: return None
        elif max>len(voters)//2: return rec[-1][0]
        for i in dict.keys():
            if dict[i]==min:
                eliminate_list.append(i)
            dict[i]=0
        for i in range(len(voters)):
            for j in range(len(voters[i])):
                if voters[i][j] in eliminate_list:
                    flag[i][j]=True
        eliminate_list=[]
        count+=1