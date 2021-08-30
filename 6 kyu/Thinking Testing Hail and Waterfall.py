def test_it(arr): 
    res=[collatz(i) for i in arr]
    solutions=[]
    length=max(len(i) for i in res)
    for i in range(length):
        temp=[]
        for j in res:
            temp.append(".") if i>=len(j) or (j[0]!=1 and j[i]==1) else temp.append(str(j[i]%10))
        solutions.append("|".join(temp))
    return "\n".join(solutions)
def collatz(n):
    if n==1:
        return [1]
    return [n]+collatz(n*3+1) if n%2 else [n]+collatz(n//2)
    