def histogram(rolls):
    compare=max(rolls)
    result=[" "*12 for i in range (compare+1)]
    for i in range(0,len(rolls)):
        value=rolls[i]
        if value==0:
            continue        
        result[compare-value]=result[compare-value][:i*2]+str(value)+result[compare-value][i*2+len(str(value)):]
        for j in range(compare-value+1,len(result)):
            result[j]=result[j][:i*2]+"#"+result[j][i*2+1:]
    result=[i.rstrip() for i in result]    
    return "\n".join(result)+'\n-----------\n1 2 3 4 5 6\n'
    