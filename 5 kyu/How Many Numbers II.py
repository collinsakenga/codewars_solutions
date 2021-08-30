def max_sumDig(nMax, maxSum):
    res=[]
    for i in range(1000, nMax+1):
        flag=True
        num=str(i)
        for j in range(0, len(num)-3):
            if sum(int(k) for k in num[j:j+4])>maxSum:
                flag=False
                break
        if flag:
            res.append(i)
    mean=sum(res)/len(res)
    val=min(abs(i-mean) for i in res)
    return [len(res),(mean-val if mean-val in res else mean+val),sum(res)]