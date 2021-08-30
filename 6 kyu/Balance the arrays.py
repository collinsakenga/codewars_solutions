from collections import Counter
def balance(arr1, arr2):
    return sorted(j for j in Counter(arr1).values())==sorted(j for j in Counter(arr2).values())