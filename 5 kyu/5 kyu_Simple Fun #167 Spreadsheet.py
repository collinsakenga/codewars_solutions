alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def spreadsheet(s):
    diff=[i for i,j in enumerate(s) if j.isdigit()]
    return first(s) if flag(diff) else second(s)

def flag(arr):
    if len(arr)<2:
        return False
    check=max(arr[i]-arr[i-1] for i in range(1, len(arr)))
    return False if check==1 else True

def first(s):
    x, y=s[1:s.index("C")], int(s[s.index("C")+1:])-1
    res=""
    count=0
    while y>=0:
        count+=1
        res+=alphabet[y%(26**count)//(26**(count-1))]
        y-=26**count
    return res[::-1]+x

def second(s):
    index=next(i for i,j in enumerate(s) if j.isdigit())
    x, y=s[:index], s[index:]
    return f"R{y}C{sum((alphabet.index(j)+1)*(26**(len(x)-1-i)) for i,j in enumerate(x))}"