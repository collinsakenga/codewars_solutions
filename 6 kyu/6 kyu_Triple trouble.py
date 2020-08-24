def triple_double(num1, num2):
    total = ""
    num1 = str(num1)
    num2 = str(num2)
    for i in range(0, len(num1)-2):
        if num1[i] == num1[i+1] == num1[i+2]:
            total += num1[i:i+3]
    for i in range(0, len(num2)-1):
        if num2[i:i+2] in total:
            return 1
    return 0
