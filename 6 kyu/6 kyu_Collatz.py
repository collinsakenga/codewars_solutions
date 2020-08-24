strng = ""
res = 0


def collatz(n):
    global strng, res
    if not res:
        res = n
    if n == 1:
        rec = strng
        strng = ""
        rec2 = str(res)
        res = 0
        return rec2+rec
    else:
        if n % 2 == 0:
            strng += "->"+str(n//2)
            return collatz(n//2)
        else:
            strng += "->"+str(3*n+1)
            return collatz(3*n+1)
