def luck_check(string):
    try:
        temp=int(string)
    except:
        raise 
    Leftsum=0
    Rightsum=0
    index1=0
    index2=len(string)-1
    if len(string)%2==0:
        for i in range(0,len(string)//2):
            Leftsum += int(string[i])
        for i in range(len(string)//2,len(string)):
            Rightsum += int(string[i])
        return Leftsum==Rightsum
    else:
        for i in range(0,len(string)//2):
            Leftsum += int(string[i])
        for i in range(len(string)//2+1,len(string)):
            Rightsum += int(string[i])
        return Leftsum==Rightsum    