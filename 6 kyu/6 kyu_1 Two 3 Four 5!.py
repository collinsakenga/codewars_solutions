dict={str(i):j for i,j in enumerate("zero one two three four five six seven eight nine".split())}
def conv(num):
    temp=str(num)
    res=""
    flag=len(temp)%2==0
    for i,j in enumerate(temp):
        if flag and int(j)%2==0:
            name=dict[j]
            res+="".join((name[k%len(name)], name[k%len(name)].upper())[k//len(name)%2==1] for k in range(i+1))
        elif not flag and int(j)%2==1:
            name=dict[j]
            res+="".join((name[k%len(name)], name[k%len(name)].upper())[k//len(name)%2==0] for k in range(i+1))
        else:
            res+=j
    return res