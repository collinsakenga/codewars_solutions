def bouncy_ratio(percent):
    bounce=0
    num=101
    while True:
        if not helper(num):
            bounce+=1  
        if bounce/num>=percent:
            return num
        num+=1
def helper(num):
    temp=str(num)
    compare="".join(sorted(temp))
    return temp==compare or temp==compare[::-1]