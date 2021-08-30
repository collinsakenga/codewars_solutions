from collections import Counter
def solve(arr): 
    return [i for i in Counter(arr[::-1]).keys()][::-1]