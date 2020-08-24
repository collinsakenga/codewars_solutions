def solution(n):
    result = ""
    while n > 0:
        if n//1000 >= 1:
            result += "M"
            n -= 1000
            continue
        elif n//900 >= 1:
            result += "CM"
            n -= 900
            continue
        elif n//500 >= 1:
            result += "D"
            n -= 500
            continue
        elif n//400 >= 1:
            result += "CD"
            n -= 400
            continue
        elif n//100 >= 1:
            result += "C"
            n -= 100
            continue
        elif n//90 >= 1:
            result += "XC"
            n -= 90
            continue
        elif n//50 >= 1:
            result += "L"
            n -= 50
            continue
        elif n//40 >= 1:
            result += "XL"
            n -= 40
            continue
        elif n//10 >= 1:
            result += "X"
            n -= 10
            continue
        elif n//9 >= 1:
            result += "IX"
            n -= 9
            continue
        elif n//5 >= 1:
            result += "V"
            n -= 5
            continue
        elif n//4 >= 1:
            result += "IV"
            n -= 4
            continue
        elif n//1 >= 1:
            result += "I"
            n -= 1
    return result
