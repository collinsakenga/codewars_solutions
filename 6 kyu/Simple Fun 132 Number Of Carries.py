def number_of_carries(a, b):
    temp1, temp2=str(a), str(b)
    temp1=temp1.rjust(len(temp2), "0")
    temp2=temp2.rjust(len(temp1), "0")
    carry=add=0
    for i,j in zip(temp1[::-1], temp2[::-1]):
        if (int(i)+int(j)+add)>=10:
            carry+=1
            add=1
        else:
            add=0
    return carry