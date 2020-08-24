def solution(n):
    res = int(n)
    if n-res >= 0.75:
        return res+1
    elif n-res >= 0.25:
        return res+0.5
    return res
