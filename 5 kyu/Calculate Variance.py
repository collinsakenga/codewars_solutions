def variance(numbers): 
    mean=sum(numbers)/len(numbers)
    return sum((i-mean)**2 for i in numbers)/len(numbers)