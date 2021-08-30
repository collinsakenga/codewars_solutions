prime_list=[2,3,5,7,11,13,17,19,23]
def find_max(n):
    res=[n]
    check={n}
    while len(res)==len(check):
        res.append(product_sum(res[-1]))
        check.add(res[-1])
    return max(res)
def product_sum(n):
    total=1
    for i in str(n):
        if i=="0":
            continue
        total*=prime_list[int(i)-1]
    return total