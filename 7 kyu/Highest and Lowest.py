def high_and_low(numbers):
    res=[int(i) for i in numbers.split()]
    return f"{max(res)} {min(res)}"