def fib():
    res=[1, 1]
    index=2
    for i in range(100000):
        res.append(res[index-res[-1]]+res[index-res[-2]])
        index+=1
    return res
memo=fib()
def length_sup_u_k(n, k):
    return sum(i>=k for i in memo[:n])
    
def comp(n):
    return sum(memo[i+1]<memo[i] for i in range(n-1))