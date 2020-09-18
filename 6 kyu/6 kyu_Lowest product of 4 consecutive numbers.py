def lowest_product(input):
    if len(input) < 4:
        return "Number is too small"
    if "0" in input:
        return 0
    total = 9**4
    for i in range(len(input)-3):
        total = min(
            total, (int(input[i])*int(input[i+1])*int(input[i+2])*int(input[i+3])))
    return total
