def mult_triangle(n):
    first=(n*(n+1)//2)**2
    third=((n+1)//2)**4
    return [first, first-third, third]