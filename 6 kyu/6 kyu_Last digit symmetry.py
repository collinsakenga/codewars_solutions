def memo():
    prime_list={11: '', 13: '', 17: '', 19: '', 23: '', 29: '', 31: '', 37: '', 41: '', 43: '', 47: '', 53: '', 59: '', 61: '', 67: '', 71: '', 73: '', 79: '', 83: '', 89: '', 97: ''}
    numbers=[]
    for i in range(1176, 1000000):
        num=str(i)
        if int(num[:2]) not in prime_list:
            continue
        square=str(i**2)
        if int(square[:2]) in prime_list and num[-2:]==square[-2:]:
            numbers.append(i)
    return numbers
res=memo()
def solve(a,b):
    return sum(1 for i in res if i>=a and i<b)