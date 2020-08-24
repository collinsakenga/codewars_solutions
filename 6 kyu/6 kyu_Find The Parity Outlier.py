def find_outlier(integers):
    temp = [i % 2 for i in integers]
    if temp.count(0) > 1:
        return integers[temp.index(1)]
    elif temp.count(1) > 1:
        return integers[temp.index(0)]
