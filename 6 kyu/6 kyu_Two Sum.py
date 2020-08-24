def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[j]+numbers[i] == target:
                return (i, j)
