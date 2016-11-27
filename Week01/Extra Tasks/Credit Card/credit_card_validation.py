def is_credit_card_valid(number):
    number_len = len(str(number))
    if not(number_len & 1):
        return False

    index = 0
    sum_of_digits = 0
    while number:
        digit = number % 10
        if index & 1:
            digit *= 2

        sum_of_digits += digit % 10
        if digit > 9:
            sum_of_digits += 1

        number //= 10
        index += 1

    return (sum_of_digits % 10) == 0
