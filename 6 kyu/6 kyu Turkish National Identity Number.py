def check_valid_tr_number(number):
    num=str(number)
    check="".join(i for i in num if not i.isdigit())
    if check or num[0]=="0" or len(num)!=11:
        return False
    total=sum(int(i) for i in num[:-1])
    first=sum(int(num[i]) for i in range(0, len(num)-2, 2))*7
    second=sum(int(num[i]) for i in range(1, len(num)-2, 2))
    if (first-second)%10==int(num[-2]) and total%10==int(num[-1]):
        return True
    return False