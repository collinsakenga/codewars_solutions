from math import sqrt


def sum_for_list(lst):
    flag = [False]*len(lst)
    for i in range(0, len(lst)):
        if lst[i] < 0:
            flag[i] = True
    compare = [abs(i) for i in lst]
    result = {}
    res = set()
    factor = 2
    index = 0
    for i in compare:
        rec = i
        while True:
            if rec == 1:
                break
            if factor > rec:
                break
            if rec % factor == 0:
                if factor not in res:
                    res.add(factor)
                rec = rec//factor
                factor = 1
            factor += 1
        key = list(res)
        for keys in key:
            if flag[index]:
                result[keys] = result.get(keys, 0) - i
            else:
                result[keys] = result.get(keys, 0) + i
        res.clear()
        index += 1
    final = []
    for test in sorted(result):
        final.append([test, result[test]])
    return final
