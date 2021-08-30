def generate_all_possible_matches(k=1):
    return helper(0, 0, k, [], [])
def helper(n, m, k, arr, res):
    if n==k or m==k:
        res.append(arr+[f"{n}:{m}"])
        return
    helper(n+1, m, k, arr+[f"{n}:{m}"], res)
    helper(n, m+1, k, arr+[f"{n}:{m}"], res)
    return res