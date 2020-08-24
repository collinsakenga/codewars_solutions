def binary_array_to_number(s):
    total = 0
    for i in range(0, len(s), 1):
        if s[i] == 1:
            total += 2**(len(s)-i-1)
    return total
