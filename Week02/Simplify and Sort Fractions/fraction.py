def gcd(a, b):
    if(a == b):
        return a
    if(a > b):
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)


def simplify_fraction(fraction):
    gcd_fraction = gcd(fraction[0], fraction[1])

    return (fraction[0]//gcd_fraction, fraction[1]//gcd_fraction)


def sort_fractions(fractions):
    for indx_1 in range(len(fractions)):
        frac_1 = float(fractions[indx_1][0])/fractions[indx_1][1]
        for indx_2 in range(len(fractions)):
            frac_2 = float(fractions[indx_2][0]/fractions[indx_2][1])
            if (frac_2 > frac_1):
                temp = fractions[indx_1]
                fractions[indx_1] = fractions[indx_2]
                fractions[indx_2] = temp

    return fractions
