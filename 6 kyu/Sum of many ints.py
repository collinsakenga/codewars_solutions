def f(n, m):
    if n<m:
        return n*(n+1)/2
    return (n//m)*(m*(m-1)/2)+(n%m)*((n%m)+1)/2