def presses(s):
    s=s.upper()
    one_count="ADGJMPTW 1*#"
    two_count="BEHKNQUX0"
    three_count="CFILORVY"
    four_count="SZ234568"
    five_count="79"
    total=0
    for i in range(len(s)):
        if s[i] in one_count:
            total+=1
        elif s[i] in two_count:
            total+=2
        elif s[i] in three_count:
            total+=3
        elif s[i] in four_count:
            total+=4
        elif s[i] in five_count:
            total+=5
    return total