def schedule(employees, month, n):
    if len(employees)//n<2:
        return None
    day=dates(int(month[:2]), int(month[2:]))
    index=0
    length=len(employees)
    employees*=2
    res=[]
    for i in range(day):
        res.append(employees[index:index+n])
        index=(index+n)%length
    return res
def dates(m, y):
    return [31, 29 if leap_year(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m-1]  
def leap_year(y):
    return True if y%400==0 else False if y%100==0 else True if y%4==0 else False