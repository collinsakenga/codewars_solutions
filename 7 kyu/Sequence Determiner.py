def determine_sequence(arr):
    ap=len({arr[i]-arr[i-1] for i in range(1, len(arr))})==1
    gp=len({arr[i]/arr[i-1] for i in range(1, len(arr))})==1
    return 2 if ap and gp else 1 if gp else 0 if ap else -1