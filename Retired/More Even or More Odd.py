def more_even_or_odd(integers):
    ans = ""
    even = 0
    odd = 0
    for i in integers:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    if even > odd:
        ans += "Even"
    elif even < odd:
        ans += "Odd"
    else:
        ans += "Equal"
    return ans