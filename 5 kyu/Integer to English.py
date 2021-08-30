arr=["thousand", "million", "billion", "trillion","quadrillion","quintillion","sextillion","septillion"]
arr2= {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', \
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', \
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', \
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
arr3=['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def helper(mod, num, index):
    if not mod and not num:
        return "zero"
    elif not mod:
        return ""
    res=[] 
    if mod>=100:
        res.append(f"{arr2[mod//100]} hundred")
        mod-=mod//100*100
    if mod>=20:
        res.append(arr3[mod//10-2])
        mod-=mod//10*10
    if mod:
        res.append(arr2[mod])
    if index>=0:
        res.append(arr[index])
    return " ".join(res)
def int_to_english(n): 
    if n<0 or not isinstance(n, int):
        return ""
    num, index=n, -1
    res=[] 
    while True:
        res.append(helper(num%1000, num,  index))
        num//=1000
        index+=1 
        if num==0: 
            break
    return " ".join((i for i in res[::-1] if i))