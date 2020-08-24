def iq_test(numbers):
    numbers = numbers.split()
    numlist = [0 if int(x) % 2 else 1 for x in numbers]
    countOdd = 0
    countEven = 0
    for y in numlist:
        if y == 0:
            countEven += 1
        elif y == 1:
            countOdd += 1
        if countEven == 2:
            return numlist.index(1)+1
        elif countOdd == 2:
            return numlist.index(0)+1
