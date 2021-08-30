def largest_sum(arr):
    n=0
    comp=0
    for i in arr:
        n+=i
        if n>0:
            comp=max(n, comp)
        else:
            n=0
    return comp