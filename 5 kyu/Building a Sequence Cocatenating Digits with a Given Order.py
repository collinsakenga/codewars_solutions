from itertools import product
def proc_seq(*args):
    arr=[str(i) for i in args]
    res=helper(arr, "", len(args), set())
    if len(res)==1:
        return [len(res), max(res)]
    return [len(res), min(res), max(res), sum(res)]
def helper(arr, cur, count, res):
    if cur and cur[0]=="0":
        return 
    elif count==0:
        res.add(int(cur))
        return 
    for i in arr[0]:
        helper(arr[1:], cur+i, count-1, res)
    return res