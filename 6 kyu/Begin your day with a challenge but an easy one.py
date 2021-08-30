def one_two_three(n):
    if n==0:
        return [0,0]
    res=divmod(n, 9)
    return [int(("0" if not res[0] else "9"*res[0]) + ("" if not res[1] else str(res[1]))), int("1"*n)]
    