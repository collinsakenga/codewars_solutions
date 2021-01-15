from gmpy2 import is_prime, next_prime
prime_list={i:1 for i in range(2, 10000) if is_prime(i)}
prime_list2=[i for i in prime_list.keys()]
def prime_maxlength_chain(n):
    res=[]
    for i,j in enumerate(prime_list.keys()):
        if res and n//i<=res[0][0]:
            break
        temp=[0, 0]
        count=count2=1
        total=total2=j
        index=i+1
        while True:
            total+=prime_list2[index]
            if total>=n:
                break
            index+=1
            count+=1
            if is_prime(total):
                count2=count
                total2=total
        temp=[count2, total2]
        if not res or temp[0]==res[0][0]:
            res.append(temp)
        elif temp[0]>res[0][0]:
            res=[temp]
    return [i[1] for i in res]