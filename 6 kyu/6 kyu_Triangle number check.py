def is_triangle_number(number):
    if not(isinstance(number, int)):
        return False
    total = 0
    start = 1
    while total < number:
        total += start
        start += 1
    return True if total == number else False
