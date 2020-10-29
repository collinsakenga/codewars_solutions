from collections import Counter
def solve(arr):
    high=max(arr)
    temp=Counter(arr)
    total=0
    for i in arr:
        for j in range(1, (high-i)//2+1):
            if temp.get(i+j, None) and temp.get(i+j*2, None):
                total+=1
    return total