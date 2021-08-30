def differences(lst):
    if not lst:
        return 0
    while len(lst)>1:
        lst=[abs(lst[i]-lst[i+1]) for i in range(len(lst)-1)]
    return lst[0]