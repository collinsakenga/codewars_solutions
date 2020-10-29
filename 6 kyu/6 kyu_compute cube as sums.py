def find_summands(n):
    temp=n**2-n+1
    return [temp+i*2 for i in range(n)]