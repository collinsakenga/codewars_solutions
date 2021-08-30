def calc_fuel(n):
    one=two=three=four=five=0
    temp=n*11
    one+=temp//800
    temp-=temp//800*800
    two+=temp//120
    temp-=temp//120*120
    three+=temp//80
    temp-=temp//80*80
    four+=temp//15
    temp-=temp//15*15
    five+=temp
    return {"lava": one, "blaze rod": two, "coal": three, "wood": four, "stick": five }
    