def expected_party_rank(lst):
    a=(round(lst[0]+lst[2], 2), "A")
    b=(round(lst[1]+lst[3], 2), "B")
    c=(round(1-a[0]-b[0], 2), "C")
    return [j for i,j in sorted((a, b, c), key=lambda x:(-x[0], x[1]))]