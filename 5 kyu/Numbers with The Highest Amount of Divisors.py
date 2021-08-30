def proc_arrInt(listNum):
    dict={}
    prime_count=0
    for i in listNum:
        prime_count+=1 if is_prime(i) else 0
        dict[i]=max_factor(i)
    temp=sorted(dict.items(), key=lambda x: -x[1])
    res=[]
    for i in temp:
        if i[1]!=temp[0][1]:
            break
        res.append(i[0])
    return [len(listNum), prime_count, [temp[0][1], sorted(res)]]
def is_prime(n):
    for i in range(2, int(n**0.5)+1):        
        if n%i==0:
            return False
    return True
def max_factor(n):
    res=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            res.add(i)
            res.add(n//i)
    return len(res)