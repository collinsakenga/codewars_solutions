from random import randint
lower1="abcdefghijklmnopqrstuvwxyz"
upper1="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digit1="0123456789"
def password_gen(): 
    temp="".join(((lower1[randint(0, 25)]+upper1[randint(0, 25)],digit1[randint(0, 9)])[randint(0, 1)] for i in range(randint(6, 10))))
    return temp[:-3]+lower1[randint(0, 25)]+digit1[randint(0, 9)]+upper1[randint(0, 25)]
    