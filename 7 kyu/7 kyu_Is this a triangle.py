def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if (a+b) <= c or (c+b) <= a or (a+c) <= b:
        return False
    else:
        return True
