from math import gcd


class Fraction(object):
    def __init__(self, n, d=1):
        self.up = n
        self.down = d
        self.flag = False
        self.quotient = 0

    def __str__(self):
        self.reduce()
        if not self.up:
            return f"{self.quotient}" if self.flag else f"-{self.quotient}"
        if self.quotient:
            return f"{self.quotient} {self.up}/{self.down}" if self.flag else f"-{self.quotient} {self.up}/{self.down}"
        return f"{self.up}/{self.down}" if self.flag else f"-{self.up}/{self.down}"

    def to_decimal(self):
        return self.up/self.down

    def __add__(self, n, d=None):
        temp2 = n.down
        down = (temp2*self.down)//gcd(temp2, self.down)
        up = self.up*down//self.down+n.up*down//n.down
        return Fraction(up, down)

    def __sub__(self, n, d=None):
        temp2 = n.down
        down = (temp2*self.down)//gcd(temp2, self.down)
        up = self.up*down//self.down-n.up*down//n.down
        return Fraction(up, down)

    def __mul__(self, n, d=None):
        return Fraction(self.up*n.up, self.down*n.down)

    def __truediv__(self, n, d=None):
        return Fraction(self.up*n.down, self.down*n.up)

    def reduce(self):
        self.flag = False if abs(self.up)//self.up * \
            abs(self.down)//self.down == -1 else True
        self.up = abs(self.up)
        self.down = abs(self.down)
        factor = 2
        while factor <= self.down:
            if self.up % factor == 0 and self.down % factor == 0:
                self.up //= factor
                self.down //= factor
                factor = 1
            factor += 1
        self.quotient = self.up//self.down
        if self.quotient:
            self.up -= self.quotient*self.down
