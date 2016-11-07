from parser import Parser
from monomial import Monomial


class Polynom:
    def __init__(self, polynom_):
        if type(polynom_) == list:
            self.list_monomials = polynom_
        elif type(polynom_) == str:
            self.list_monomials = Parser.to_polynom(polynom_)
        else:
            raise TypeError("Argument for Polynom must be str or list.")
        self._sort_and_shrink()

    def __str__(self):
        if self.list_monomials == []:
            return ""
        result = str(self.list_monomials[0])
        for indx in range(1, len(self.list_monomials)):
            if self.list_monomials[indx].coef != 0:
                result += ' + ' + str(self.list_monomials[indx])
        return result

    def __repr__(self):
        return self.__str__()

    def derivative(self):
        list_derivates = []
        for mon in self.list_monomials:
            list_derivates.append(mon.derivative())
        return Polynom(list_derivates)

    def print_derivative(self):
        derivat = self.derivative()
        print(derivat)

    def _sort_and_shrink(self):
        self.list_monomials.sort(reverse=True)
        indx = 0
        while indx < len(self.list_monomials) - 1:
            left_exp = self.list_monomials[indx].exp
            right_exp = self.list_monomials[indx + 1].exp
            if left_exp == right_exp:
                self.list_monomials[indx] += self.list_monomials[indx+1]
                del self.list_monomials[indx + 1]
            else:
                indx += 1
