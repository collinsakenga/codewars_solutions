from math import gcd


class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    # Equality test

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    def __add__(self, other):
        bottom = self.bottom*other.bottom//gcd(self.bottom, other.bottom)
        top = bottom//self.bottom*self.top+bottom//other.bottom*other.top
        for i in range(int(min(bottom, top)**0.5), 1, -1):
            if top % i == 0 and bottom % i == 0:
                top //= i
                bottom //= i
        return Fraction(top, bottom)

    def __str__(self):
        return f"{self.top}/{self.bottom}"
