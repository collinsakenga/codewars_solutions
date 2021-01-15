from collections import Counter
def memo():
    res=[0,1,2,3,4,5,6,7,8,9,10]
    dict={i:-1 for i in res}
    for i in range(500):
        num=11
        temp=Counter(str(res[-1]))
        while True:     
            flag=all(temp.get(i, None)==None for i in str(num))
            if flag and dict.get(num, None)==None:
                res.append(num)
                dict[num]=-1
                break
            num+=1
    return res
numbers=memo()
def find_num(n):
    return numbers[n]