from itertools import combinations_with_replacement
def find_all(sum_dig, digs):
    res=["".join(i) for i in combinations_with_replacement("123456789", digs) if sum(int(j) for j in i)==sum_dig]
    return [] if not res else [len(res), int(res[0]), int(res[-1])]
    """
    maximum=str(sum_dig//digs)*(digs-sum_dig%digs)+str(sum_dig//digs+1)*(sum_dig%digs)    
    nine=sum_dig//9
    if (digs-nine)>(sum_dig-nine*9):
        nine-=1
    minimum=int("1"*(digs-nine-1)+str(sum_dig-nine*9+1-(digs-nine))+"9"*nine)
    print(minimum, maximum)
    """