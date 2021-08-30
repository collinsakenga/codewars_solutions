def pos_average(s):
    check=s.split(", ")
    total=0
    for i in range(len(check)-1):
        string=check[i]
        for j in range(i+1, len(check)):
            for k in range(len(check[j])):
                if check[j][k]==string[k]:
                    total+=1    
    return total/(len(check[0]))/(len(check)*(len(check)-1)/2)*100