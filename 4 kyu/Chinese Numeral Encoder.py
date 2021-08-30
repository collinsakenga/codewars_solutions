numerals = {
    "-":"负",
    ".":"点",
    0:"零",
    1:"一",
    2:"二",
    3:"三",
    4:"四",
    5:"五",
    6:"六",
    7:"七",
    8:"八",
    9:"九",
    10:"十",
    100:"百",
    1000:"千",
    10000:"万"
}
def to_chinese_numeral(n):
    if n==0: return '零'
    res=str(n)
    result=""
    if res[0]=="-":
        result+=numerals[res[0]]
        res=res[1:]
    res2=""
    if "." in res:
        res2=res[res.index(".")+1:]
        res=res[:res.index(".")]
    check=res
    result2=""
    if res2:
        if int(check)==0:
            result2+=numerals[0]
        result2+=numerals["."]
        while len(res2)>0:
            result2+=numerals[int(res2[0])]
            res2=res2[1:]
    while len(res)>0:
        if int(res[0])!=0:
            if not (int(check)>=10 and int(check)<=19 and len(res)==2):
                result+=numerals[int(res[0])]
            if (len(res)-1)>0:
                result+=numerals[(10**(len(res)-1))]
            res=res[1:]
        elif int(res[0])==0:
            index=1
            while True:
                if index==len(res):
                    return result+result2
                if int(res[index])!=0:
                    result+=numerals[0]
                    res=res[index:]
                    break
                index+=1
    return result+result2
        