def sierpinski(n):
    if n==0: return "L"
    elif n==1: return "L\nL L"
    elif n==2: return 'L\nL L\nL   L\nL L L L'
    triangle=[["L"]*(i+1) for i in range(2**2)]
    triangle[2][1]=" "
    for i in range(3,n+1):
        res=[[" "]*(j+1) for j in range(2**i)]
        for j in range(0,(2**i)//2):
            for k in range(len(res[j])):
                res[j][k]=triangle[j][k]
        for j in range((2**i)//2,2**i):
            for k in range(len(res[j-(2**i)//2])):
                res[j][k]=triangle[j-(2**i)//2][k]
        for j in range((2**i)//2,2**i):
            for k in range((2**i)//2,j+1):
                res[j][k]=triangle[j-(2**i)//2][k-(2**i)//2]
        triangle=res.copy()
    return "\n".join([" ".join(i) for i in res])