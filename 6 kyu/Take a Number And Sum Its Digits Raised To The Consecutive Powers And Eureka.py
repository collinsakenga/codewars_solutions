def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    temp=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 89, 135, 175, 518, 598, 1306, 1676, 2427, 2646798, 12157692622039623539]
    res=[]
    for i in range(a,b+1):
        for j in temp:
            if i==j:
                res.append(j)
    return res
            
        