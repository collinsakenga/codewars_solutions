def solution(n, m):
    return next((1 for i in range(1, int(m**0.5)+1) if (m-i**2)**2+i==n), 0)