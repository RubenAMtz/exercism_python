from __future__ import division
from math import gcd
# import math

class Rational(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.normalize()

    def normalize(self):
        gcd_ = gcd(self.numer, self.denom)
        self.numer = self.numer // gcd_
        self.denom = self.denom // gcd_
        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1
        return self

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        num = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(num, denom)

    def __sub__(self, other):
        num = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(num, denom)

    def __mul__(self, other):
        num = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(num, denom)

    def __truediv__(self, other):
        num = self.numer * other.denom
        denom = self.denom * other.numer
        if denom == 0:
            raise Exception("Division by zero, noob.")
        return Rational(num, denom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        #positive power
        if power > 0:
            num = self.numer ** power
            denom = self.denom ** power
        #negative power
        else:
            denom = self.numer ** abs(power)
            num = self.denom ** abs(power)
        return Rational(num,denom)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)