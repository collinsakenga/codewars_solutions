def solve(arr):
    res=[arr[i]-arr[i-1] for i in range(1, len(arr))]
    pos=sum(1 for j in res if j>0)
    neg=sum(1 for j in res if j<0)
    if pos==0:
        return "D"
    elif neg==0:
        return "A"
    elif pos==1 and neg==1:
        return "RA" if res[0]<res[1] else "RD"
    return "RA" if neg==1 else "RD"