def uncensor(infected, discovered):
    res=list(infected)
    index=0
    for i,j in enumerate(res):
        if j=="*":
            res[i]=discovered[index]
            index+=1
    return "".join(res)