def withdraw(n):
    one=two=three=0
    if n%100==60 or n%100==20 or n%100==80 or n%100==40:
        three+=(n%100)//20
        n-=n%100//20*20
    if n%100==10:
        n-=110
        two+=1
        three+=3
    elif n%100==30:
        n-=130
        two+=1
        three+=4
    elif n%100==50:
        n-=50
        two+=1
    elif n%100==70:
        n-=70
        two+=1
        three+=1
    elif n%100==90:
        n-=90
        two+=1
        three+=2
    return [n//100, two, three]