def greatest_product(n):
    compare = 0
    for i in range(0, len(n)-4):
        temp = int(n[i])*int(n[i+1])*int(n[i+2])*int(n[i+3])*int(n[i+4])
        compare = max(compare, temp)
    return compare
