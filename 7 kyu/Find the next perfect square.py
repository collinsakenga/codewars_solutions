def find_next_square(n):
    for i in range(1,int(n**0.5)+1):
        if i**2==n:
            return (i+1)**2
    return -1
        