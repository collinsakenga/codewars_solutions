def add(num1, num2):
    num1, num2=str(num1), str(num2)
    return int("".join(str(int(i)+int(j)) for i,j in zip(num1.rjust(len(num2), "0"), num2.rjust(len(num1), "0"))))