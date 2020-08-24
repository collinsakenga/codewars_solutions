def get_middle(s):
    n = len(s)
    if n % 2 == 1:
        return s[(n-1)//2]
    else:
        return s[(n-1)//2:(n+1)//2+1]
