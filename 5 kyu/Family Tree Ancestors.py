from math import log, ceil
def chart(person):
    res=helper(tuple(sorted(person.parents(), key=lambda x: x.sex, reverse=True)), 2, [], 16, 16) 
    res.append((person.name, 16))
    dict={j:i for i,j in res}
    dict2=helper2(16)
    chart=[]
    for i in range(1, 32):
        temp=((4-depth(i))*11-1)*" "+("|" if 4-depth(i)!=0 else "")
        name=dict.get(i, "_______")
        number=str(dict2[i]).rjust(2, "0")
        temp+=f"{number} {name}"
        chart.append(list(temp))
    for index,i in enumerate(chart):
        digits=int("".join(j for j in "".join(i) if j.isdigit()))
        num=5-ceil(log(digits+1, 2))
        if digits==1 or num==0:
            continue
        for k in range(1, 2**num):
            chart[index+(-k if digits%2 else k)][44-num*11-1]="|"
    chart[16][32]=" "
    chart[14][32]=" "
    return "\n".join("".join(i) for i in chart)+"\n"
def helper(person, index, arr, row, rate):       
    if person==None or index>31:
        return
    rate//=2
    for i,j in enumerate(person):
        if (index+i)<=31:
            arr.append((j.name, row-rate if j.sex=="M" else row+rate))
        helper(tuple(sorted(j.parents(), key=lambda x: x.sex, reverse=True)), (index+i)*2, arr, row-rate if j.sex=="M" else row+rate, rate)
    return arr
def depth(num):
    total=0
    while num%2==0:
        num//=2
        total+=1
    return total
def helper2(num):
    start=0
    dict={}
    while num>0:
        increment=2**(start+1)
        for i in range(num):
            dict[2**start+i*increment]=num+i
        start+=1 
        num//=2
    return dict