def find_the_key(message, code):
    res=[]
    for i in range(len(code)):
        res.append(code[i]-(ord(message[i])-ord("a"))-1)
    solution="".join(str(i) for i in res)
    for i in range(1, len(solution)+1):
        temp=solution[:i]
        flag=True
        for j in range(len(temp)):
            for k in range(j,len(solution), i):
                if solution[k]!=solution[j]:
                    flag=False
                    break
            if not flag:
                break
        if flag:
            return int(temp)