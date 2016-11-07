class Monomial:

    def __init__(self, coef, exp, var):
        self.coef = coef
        self.exp = exp
        self.var = var

    def __str__(self):
        if self.coef == 0:
            return '0'
        if self.exp == 0:
            return str(self.coef)
        if self.coef == 1 and self.exp == 1:
            return self.var
        result = str(self.coef) + '*' + self.var
        if self.exp == 1:
            return result
        return result + '^' + str(self.exp)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if self.exp != other.exp:
            return
        return Monomial(self.coef + other.coef, self.exp, self.var)

    # operator ==
    def __eq__(self, other):
        return (self.coef == other.coef and self.exp == other.exp)

    # operator !=
    def __ne__(self, other):
        return not(self == other)

    def __hash__(self):
        value = (self.coef**self.exp)*ord(self.var)
        return hash(value)

    # operator <
    def __lt__(self, other):
        return (self.exp < other.exp or self.exp == other.exp and self.coef < other.coef)

    # operator <=
    def __le__(self, other):
        return (self < other or self == other)

    # operator >
    def __gt__(self, other):
        return not(self <= other)

    # operator >=
    def __ge__(self, other):
        return (self > other or self == other)

    def derivative(self):
        dev_coef = self.coef * self.exp
        dev_exp = self.exp - 1 if self.exp >= 1 else 0
        return Monomial(dev_coef, dev_exp, self.var)
