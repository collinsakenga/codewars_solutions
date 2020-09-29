def solution(number):
    return total((number-1)//3, 3)+total((number-1)//5, 5)-total((number-1)//15, 15)


def total(n, divide):
    return divide*(n+1)//2*n if n % 2 == 1 else (n*divide+divide)*(n//2)
