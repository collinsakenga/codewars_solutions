sort_alnum="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
def unusual_sort(array):
    return sorted(array, key=lambda x: (sort_alnum.index(str(x)), check_type(x)))
def check_type(n):
    return 0 if isinstance(n, int) else 1