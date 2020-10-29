from itertools import combinations
def solve(arr,n):
    for i in range(len(arr)):
        for j in combinations(arr, i+1):
            root=sum(j)
            if root%n==0:
                return True
    return False