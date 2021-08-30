def count_cows(n):
    if not isinstance(n, int):
        return None
    list=[1,1,1,2]
    if n<=3:
        return list[n]
    for i in range(n-3):
        list.append(list[-2]+list[-3]+list[-4])
    return list[n]