units = {
        "zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8,
        "nine":9, "ten":10, "eleven":11, "twelve":12, "thirteen":13, "fourteen":14, "fifteen":15,
        "sixteen":16, "seventeen":17, "eighteen":18, "nineteen":19,
        "twenty":20, "thirty":30, "forty":40, "fifty":50, "sixty":60, "seventy":70, "eighty":80, "ninety":90,
        "hundred":100      
        }
times={"thousand":1000  ,"million":1000000,"billion":1000000000,"trillion":1000000000000}
def parse_int(string):
    string=string.lower()
    string+=" zero"
    temp=string.replace("thousand","abcdefgh").replace("and","").replace("-"," ").replace("abcdefgh","thousand")
    res=[]
    flag=[False]*4
    backup=temp
    for i in backup.split():
        if i in times:
            for j in list(times):
                if i==j:
                    flag[list(times).index(i)]=True
            temp=temp.split(" "+i+" ")
            res.append(temp[0])
            temp.pop(0)
            temp="".join(temp)
    res.append(temp)
    num=0
    num2=0
    for i in res:
        num2=getNum(i.split())
        for i in range(len(flag)-1,-1,-1):
            if flag[i]:
                num+=num2*times[list(times)[i]]
                flag[i]=False
                break
        else:
            num+=num2
    return num
def getNum(list):
    if not list:
        return 0
    num=0
    list.reverse()
    for i in range(0,len(list)):
        if units[list[i]]==100:
            num+=units[list[i]]*units[list[i+1]]
            break
        else:
            num+=units[list[i]]
    return num