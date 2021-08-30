import re
from math import factorial
def factorial_sum(string):
    return sum(factorial(int(i)) for i in re.split(r'\D+',string) if i)