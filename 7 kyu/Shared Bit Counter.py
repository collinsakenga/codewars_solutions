def shared_bits(a, b):
    temp1=bin(a)[2:]
    temp2=bin(b)[2:]
    temp1=temp1.rjust(len(temp2),"0")
    temp2=temp2.rjust(len(temp1),"0")
    return sum(i==j=="1" for i,j in zip(temp1, temp2))>=2