def solve(a,b):
    total=0
    for i in range(max(2, a), b):
        if not is_prime(i):
            continue
        temp=[i]
        temp2=set()
        temp2.add(temp[-1])
        while True:
            temp.append(square_sum(temp[-1]))
            temp2.add(temp[-1])
            if temp[-1]==1:
                total+=1
                break
            elif len(temp)!=len(temp2):
                break
    return total
def is_prime(n):
    if n>2 and n%2==0:
        return False
    elif n>3 and n%3==0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def square_sum(n):
    total=0
    for i in str(n):
        total+=int(i)**2
    return total