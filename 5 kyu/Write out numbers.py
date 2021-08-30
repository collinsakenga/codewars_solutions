words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
tens = ['', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def number2words(n):
    if n==0:
        return "zero"
    res=[]
    thousand=["thousand"]
    for i in range(1 if n>=1000 else 0):
        res.extend([hundred(n//(10**3)), "thousand"])
        n=int(str(n)[-3:])
    return " ".join(res) if not n else " ".join(res+[hundred(n)])
def hundred(n):
    res=[]
    flag=False
    if n//100:
        res.append(words[n//100])
        n-=n//100*100
        res.append("hundred")
    if n>=20:
        res.append(tens[n//10-1])
        n-=n//10*10
        flag=True
    if n:
        res.append(words[n]) if not flag else res.append("-"+words[n])
    return " ".join(res).replace(" -","-")  