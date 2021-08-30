def check_vin(number):
    if len(number)!=17 or any(i in number for i in "IOQ"):
        return False
    number=number.upper()
    s1="A B C D E F G H J K L M N P R S T U V W X Y Z"
    s2="1 2 3 4 5 6 7 8   1 2 3 4 5   7   9 2 3 4 5 6 7 8 9"
    table={i:int(j) for i,j in zip(s1.split(), s2.split())}
    total=sum(j*(int(i) if i not in table else table[i]) for i,j in zip(number, [8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]))
    check=int(number[8]) if number[8] not in table else table[number[8]]
    if ((total%11)==10 and check==7):
        return number[8]=="X"
    elif ((total%11)==7 and check==7):
        return number[8]=="7"
    return (total%11)!=10 and total%11==check