def solve_pirates(p,b):
    if p==3:
        return [b-1]+[1, 0]
    elif p==4:
        return [b-3]+[0, 2, 1]
    elif p==5:
        return [b-3]+[0, 1, 0, 2]
    most=b-(p//2+1) 
    arr=[most]+([0, 1, 2] if p%2==0 else [0, 1, 2, 0])
    return arr+([0, 1] if p%2==0 else [1, 0])*(p//2-3)+([1, 0] if p%2==0 else [0, 1])