def quadratic_builder(expression):
    first, second=expression[1:-1].split(")(")
    first, second=helper(first), helper(second)
    two=int(first[0][:-1])*int(second[0][:-1])
    one=int(first[1])*int(second[0][:-1])+int(second[1])*int(first[0][:-1])
    zero=int(first[1])*int(second[1])
    res=""
    if two!=0:
        res+=(f"+{first[0][-1]}" if two==1 else f"-{first[0][-1]}" if two==-1 else ("+" if two>0 else "-")+f"{abs(two)}{first[0][-1]}")+"^2"
    if one!=0:
        res+=(f"+{first[0][-1]}" if one==1 else f"-{first[0][-1]}" if one==-1 else ("+" if one>0 else "-")+f"{abs(one)}{first[0][-1]}")
    if zero!=0:
        res+="+1" if zero==1 else "-1" if zero==-1 else ("+" if zero>0 else "-")+f"{abs(zero)}"
    return res.lstrip("+")
def helper(s):
    if "+" in s:
        first, second=s[:s.index("+")], s[s.index("+")+1:]
    elif "-" in s:
        index=len(s)-s[::-1].index("-")
        first, second=s[:index-1], "-"+s[index:]
    if first[0].isalpha() and len(first)==1:
        first="1"+first
    elif second[0].isalpha() and len(second)==1:
        second="1"+second
    elif first[0]=="-" and len(first)==2 and first[-1].isalpha():
        first="-1"+first[-1]
    elif second[0]=="-" and len(second)==2 and second[-1].isalpha():
        second="-1"+second[-1]
    return (first, second) if any(i.isalpha() for i in first) else (second, first)