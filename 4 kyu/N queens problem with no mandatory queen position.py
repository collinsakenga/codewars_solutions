def nQueen(n):
    if 2<=n<=3:
        return []
    mod=n%6
    odd, even=[], []
    for i in range(1, n+1):
        if i%2:
            odd.append(i-1)
        else:
            even.append(i-1)
    if mod==2:
        odd[0], odd[1]=odd[1], odd[0]
        odd.append(odd.pop(2))
    elif mod==3:
        even.append(even.pop(0))
        odd.extend([odd.pop(0), odd.pop(0)])
    return even+odd