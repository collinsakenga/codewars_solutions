dict={11:"th", 12:"th", 13:"th", 1:"st", 2:"nd", 3:"rd"}
def what_century(year):
    year=str(year)
    century=int(year[:2])+1 if year[-2:]!="00" else int(year[:2])
    if century in dict:
        return f"{century}{dict[century]}"
    elif century%10 in dict:
        return f"{century}{dict[century%10]}"
    return f"{century}th"