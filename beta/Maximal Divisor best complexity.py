def maximal_divisor(num: int) -> int:
    return next((num//i for i in range(2, int(num**0.5)+1) if num%i==0), 1)