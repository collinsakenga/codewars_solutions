def order_by_domain(addresses):
    return sorted(addresses, key= lambda x: (test(x.split("/")[2].split(".")[-1]), test2(x.split("/")[2].split(".")[-1])))
def test(s):
    if s=="com":
        return 0
    elif s=="gov":
        return 1
    elif s=="org":
        return 2
    return 3
def test2(s):
    return s