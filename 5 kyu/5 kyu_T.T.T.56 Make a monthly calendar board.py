import datetime
dict1={j:i for i,j in enumerate("SUN MON TUE WED THU FRI SAT".split())}
dict2={j:i for i,j in dict1.items()}
dict3={i+1:j.capitalize() for i,j in enumerate("january february march april may june july august september october november december".split())}
def calendar(year,month):
    temp=datetime.datetime(year, month, 1).strftime("%A")[:3].upper()
    start=dict1[temp]
    calendar=[(str(year)+" "+dict3[month]).center([27, 26][len(dict3[month])%2]).rstrip(" "), "SUN MON TUE WED THU FRI SAT"]
    line=[]
    for i in range(1, date(month, year)+1):
        line.append(str(i).center(3, " "))
        if start==6:
            calendar.append(" ".join(line).rjust(27, " ").rstrip(" "))
            line=[]
        start=(start+1)%7
    return ("\n".join(calendar)+"\n"+" ".join(line)).rstrip("\n")
def date(m, y):
    return [31, 29 if leap_year(y) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][m-1]  
def leap_year(y):
    return True if y%400==0 else False if y%100==0 else True if y%4==0 else False