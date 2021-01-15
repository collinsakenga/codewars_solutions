from gmpy2 import is_prime
dict={i:i for i in range(2, 1000000) if is_prime(i)}
def check_goldbach(number):
    if number>2 and number%2:
        return []
    for i,j in dict.items():
        if i>=number:
            break
        if dict.get(number-i, None):
            return [i, number-i]
    return []