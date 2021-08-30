def mean(town, strng):
    total=0
    for i in strng.split("\n"):
        res=i.split(":")
        if res[0]==town:
            for data in res[1].split(","):
                total+=float(data.split()[1])
    return total/12 if total else -1
def variance(town, strng):
    total=0
    average=mean(town, strng)
    for i in strng.split("\n"):
        res=i.split(":")
        if res[0]==town:
            for data in res[1].split(","):
                total+=(float(data.split()[1])-average)**2
    return total/12 if total else -1
    