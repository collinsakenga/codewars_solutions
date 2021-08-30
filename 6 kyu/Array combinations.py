def solve(arr):
    total=1
    for i in arr:
        total*=len(set(i))
    return total