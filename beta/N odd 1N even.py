# return the resulting product of n and 1/n until n reaches 1
def nole(n):
    if n==1:
        return 1
    return (n if n%2==1 else 1/n)*nole(n-1)