def fraction_simplifier(numerator, denominator):
    product=numerator//denominator
    numerator-=product*denominator
    common=gcd(numerator, denominator)
    numerator, denominator=numerator//common, denominator//common
    if product:
        return [product, numerator, denominator]
    return [numerator, denominator]
def gcd(a, b):
    if not b:
        return a
    return gcd(b, a%b)