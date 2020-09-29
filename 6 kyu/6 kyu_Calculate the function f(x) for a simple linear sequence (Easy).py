def get_function(sequence):
    res = []
    check = []
    for i in sequence:
        res.append(i)
        if len(res) == 1:
            continue
        check.append(i-res[-2])
    if len(set(check)) != 1:
        return 'Non-linear sequence'
    if check[0] == 0:
        return f"f(x) = {res[0]}"
    elif check[0] == -1:
        return f"f(x) = -x + {abs(res[0])}" if res[0] > 0 else f"f(x) = -x - {abs(res[0])}" if res[0] < 0 else f"f(x) = -x"
    elif check[0] == 1:
        return f"f(x) = x + {abs(res[0])}" if res[0] > 0 else f"f(x) = x - {abs(res[0])}" if res[0] < 0 else f"f(x) = x"
    return f"f(x) = {check[0]}x + {abs(res[0])}" if res[0] > 0 else f"f(x) = {check[0]}x - {abs(res[0])}" if res[0] < 0 else f"f(x) = {check[0]}x"
