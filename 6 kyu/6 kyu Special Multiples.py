def count_specMult(n, max_val):
    total=1
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37][:n]:
        total*=i
    return max_val//total