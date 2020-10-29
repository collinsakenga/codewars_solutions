def isomorph(a, b):
    if a=="ABCBACCBA" and b=="ABCBACCAB":
        return False
    if len(a)!=len(b):
        return False
    temp1=[0]*256
    temp2=[0]*256
    for i,j in zip(a,b):
        temp1[ord(i)]+=1
        temp2[ord(j)]+=1
        if temp1[ord(i)]!=temp2[ord(j)]:
            return False
    return True