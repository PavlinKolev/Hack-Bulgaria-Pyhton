class Fraction:
    def __init__(self, numerator, denominator):
        if type(numerator) is not int:
            raise TypeError("Type of nominator must be int.")
        Fraction._check_denom(denominator)
        gcd = Fraction.gcd(numerator, denominator)
        self.numerator = numerator//gcd
        self.denominator = denominator//gcd

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __hash__(self):
        return hash(self.numerator*self.denominator)

    def __add__(self, other):
        num = self.numerator*other.denominator + self.denominator*other.numerator
        denom = self.denominator*other.denominator
        gcd = Fraction.gcd(num, denom)
        return Fraction(num//gcd, denom//gcd)

    def __sub__(self, other):
        num = self.numerator*other.denominator - self.denominator*other.numerator
        denom = self.denominator*other.denominator
        gcd = Fraction.gcd(num, denom)
        return Fraction(num//gcd, denom//gcd)

    def __mul__(self, other):
        num = self.numerator*other.numerator
        denom = self.denominator*other.denominator
        gcd = Fraction.gcd(num, denom)
        return Fraction(num//gcd, denom//gcd)

    @classmethod
    def _check_denom(cls, denominator):
        if type(denominator) is not int:
            raise TypeError("Type of denominator must be int.")
        if denominator == 0:
            raise ValueError("Denominator cannot be 0.")

    @classmethod
    def gcd(cls, a, b):
        if a == b:
            return a
        if -a == b:
            return -a
        if a < b and -a < b:  # |a| < |b|
            if a > 0:
                return Fraction.gcd(a, b - a)
            else:
                return Fraction.gcd(a, b + a)
        else:
            if a > 0:
                return Fraction.gcd(a - b, b)
            else:
                return Fraction.gcd(a + b, b)
