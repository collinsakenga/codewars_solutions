def sort_array(a):
    if not a:
        return []
    odd = sorted(i for i in a if i % 2 == 1)
    even = sorted((i for i in a if i % 2 == 0), key=lambda x: -x)
    res = []
    odd_len = 0
    even_len = 0
    temp = a[0] % 2
    index = 0
    rec = 0
    while index < len(a):
        if a[index] % 2 != temp:
            if temp == 1:
                res.extend(odd[odd_len:odd_len+index-rec])
                odd_len += index-rec
            else:
                res.extend(even[even_len:even_len+index-rec])
                even_len += index-rec
            rec = index
            temp = a[index] % 2
        index += 1
    res.extend(odd[odd_len:]) if odd_len != len(
        odd) else res.extend(even[even_len:])
    return res
