def bob(y):
    total=0
    divide=1
    for i in range(y):
        total+=1/divide
        divide*=(i+2)
    return total