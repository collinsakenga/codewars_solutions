def last_digit(n):
    return 1 if n<=1 else 6*[1, 1, 2, 6, 4, 4, 4, 8, 4, 6][n%10]*3**(n//5%4)*last_digit(n//5)%10
    