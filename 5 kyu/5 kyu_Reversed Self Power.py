def memo(n):
    res=[]
    for i in range(n):
        total=0
        for j in range(i):
            total+=(j+1)**(i-j)
        res.append(len(str(total)))
    return res
check_length=memo(1001)
def min_length_num(num_dig, ord_max): 
    res=next((i+1 for i,j in enumerate(check_length[:ord_max]) if j==num_dig), -1)
    return [res!=-1, res]