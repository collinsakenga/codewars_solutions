def sum_pow_dig_seq(start, n, k):
    res=[start]
    memo={start}
    while len(res)<k:
        num=power_sum(res[-1], n)
        if num in memo:
            index=res.index(num)
            return [index, res[index:], len(res[index:]), res[index:][(k-index)%len(res[index:])]]
        memo.add(num)
        res.append(num)
def power_sum(n, pow):
    return sum(int(i)**pow for i in str(n))