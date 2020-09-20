def sort_number(a):
    a[a.index(max(a))] = 1 if max(a) > 1 else 2
    return sorted(a)
