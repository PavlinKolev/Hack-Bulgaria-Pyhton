from monomial import Monomial


class Parser:
    def to_polynom(polynom_):
        list_monomials = []
        var = Parser.__get_poly_var(polynom_)
        for elem in polynom_.split('+'):
            pair = Parser.__to_monomial(elem, var)
            mon = Monomial(pair[0], pair[1], var)
            list_monomials.append(mon)

        return list_monomials


    @classmethod
    def __to_monomial(cls, monomial, var):
        pair = []
        pair.append(Parser.__get_coef(monomial, var))
        pair.append(Parser.__get_pow(monomial, var))
        return pair


    @classmethod
    def __get_coef(cls, monomial, var):
        coef = monomial.split(var)[0]
        if coef == '' or coef == ' ':
            return 1
        else:
            return int(coef)

    @classmethod
    def __get_pow(cls, monomial, var):
        if var not in monomial:
            return 0
        if '^' not in monomial:
            return 1

        exp = monomial.split(var)[-1]
        return int(exp.split('^')[-1])

    @classmethod
    def __get_poly_var(cls, polynom_):
        for char in polynom_:
            if char.isalpha():
                return char
        return 'x'
