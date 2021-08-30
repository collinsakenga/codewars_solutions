from math import log
def compare_powers(n1,n2):
    if n1[0]==1:
        return 1 if n2[0]>1 else 0
    elif n2[0]==1:
        return -1 if n1[0]>1 else 0
    convert_power=log(n2[0], n1[0])
    return 0 if n1[1]==convert_power*n2[1] else -1 if n1[1]>convert_power*n2[1] else 1