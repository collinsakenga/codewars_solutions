from itertools import permutations
def sc_perm_comb(num):
    total=0
    number=str(num)
    for i in range(len(number)):
        for j in set(permutations(number, i+1)):
            temp="".join(j)
            if temp.startswith("0"):
                continue
            total+=int(temp)
    return total