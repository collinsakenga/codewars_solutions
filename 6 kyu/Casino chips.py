def solve(arr):
    return (sum(arr))//2 if max(arr)<(sum(arr)-max(arr)) else sum(arr)-max(arr)