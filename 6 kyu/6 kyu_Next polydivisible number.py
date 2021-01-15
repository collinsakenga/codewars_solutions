def all_numbers():
    all=[]
    first=[]
    for i in range(1,10):
        first.append(i)
    all.extend(first)
    digit=2
    while True:
        numbers=[]
        for i in first:
            temp=i*10
            for j in range(10):
                if (temp+j)%digit==0:
                    numbers.append(temp+j)
        if not numbers:
            break
        all.extend(numbers)
        first=numbers
        digit+=1   
    return all
res=all_numbers()
def next_num(n):
    return next((i for i in res if i>n), None)