def reverse_fizzbuzz(string):
    if string == "Fizz Buzz":
        return [9, 10]
    elif string == "Fizz":
        return [3]
    elif string == "Buzz":
        return [5]
    elif string == "FizzBuzz":
        return [15]
    elif string == "Buzz Fizz":
        return [5, 6]
    res = []
    temp = string.split()
    for i, j in enumerate(temp):
        if not (j == "Fizz" or j == "Buzz" or j == "FizzBuzz"):
            index = i
            break
    for i, j in enumerate(temp):
        res.append(int(temp[index])+i-index)
    return res
