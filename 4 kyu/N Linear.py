from collections import deque
def n_linear(m,n):
    dict={i:0 for i in sorted(m)}
    res=[1]
    while len(res)<=n:
        comp, num=float("inf"), []
        for i,j in dict.items(): 
            temp=res[j]*i+1
            if comp>temp:
                comp=temp
                num=[i]
            elif comp==temp:
                num.append(i)
        for i in num:
            dict[i]+=1
        res.append(comp)
    return res[n]