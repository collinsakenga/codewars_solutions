def partitions(n):
    return helper(n, n)
def helper(n, n2, dict={}):
    if n2==0:
        return 0
    elif n<=0:
        return 1 if n==0 else 0
    if dict.get((n, n2)):
        return dict[(n, n2)]
    dict[(n, n2)]=(helper(n, n2-1)+helper(n-n2, n2))
    return dict[(n, n2)]