def split_and_add(numbers, n):
    temp=[]
    count=0
    while count<n:
        for i in range(0,len(numbers)//2):
            temp.append(numbers[0])
            numbers.pop(0)
        if not temp:
            return numbers
        if len(temp)<len(numbers):
            for i in range(0,len(temp)):
                numbers[i+1]+=temp[i]            
        elif len(temp)==len(numbers):
            for i in range(0,len(temp)):
                numbers[i]+=temp[i]
        temp=[]
        count+=1
    return numbers