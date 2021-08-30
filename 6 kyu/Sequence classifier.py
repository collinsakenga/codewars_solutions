def sequence_classifier(arr):
    check=sorted(arr[i]-arr[i-1] for i in range(1, len(arr)))
    low=min(check)
    high=max(check)
    if low==high==0:
        return 5
    elif low>=0:
        return 2 if low==0 else 1
    elif high<=0:
        return 4 if high==0 else 3
    return 0