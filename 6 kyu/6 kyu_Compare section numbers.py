def compare(s1, s2):
    temp1=s1.split(".")
    temp2=s2.split(".")
    temp1.extend(["0"]*(len(temp2)-len(temp1)))
    temp2.extend(["0"]*(len(temp1)-len(temp2)))
    for i,j in zip(temp1, temp2):
        if int(i)>int(j):
            return 1
        elif int(j)>int(i):
            return -1 
    return 0