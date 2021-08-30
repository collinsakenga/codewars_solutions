def find_solution(puzzle):
    res=[]
    for i,j in enumerate(puzzle):
        if j.count(0)>j.count(1):
            res.append(i)
            for k,l in enumerate(j):
                puzzle[i][k]=0 if l==1 else 1
    length=len(puzzle)       
    for i in range(len(puzzle)):
        temp=[puzzle[j][i] for j in range(len(puzzle[i]))]
        if temp.count(0)>temp.count(1):
            res.append(length+i)
    return res