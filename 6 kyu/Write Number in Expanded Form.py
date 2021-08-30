def expanded_form(num):
    empty_string=""
    divide=10**(len(str(num))-1)
    while num!=0:
        count=int(num/divide)
        num=num%divide
        if count!=0:
            empty_string+=str(count*int(divide))+" + "
        divide/=10
    return(empty_string[:-3])