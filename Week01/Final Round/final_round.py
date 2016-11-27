def is_number_balanced(n):
    if n < 0:
        n *= -1
    if n >= 0 and n <= 9:
        return True
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10

    left_sum = 0
    right_sum = 0
    middle = len(digits) // 2
    for i in range(middle):
        left_sum += digits[i]
        right_sum += digits[-(i + 1)]
    return left_sum == right_sum


def increasing_or_decreasing(seq):
    is_decr = False
    is_incr = False
    for indx in range(1, len(seq)):
        if seq[indx - 1] < seq[indx]:
            is_incr = True
            if is_decr:
                return False
        if seq[indx - 1] > seq[indx]:
            is_decr = True
            if is_incr:
                return False

    if not(is_incr) and not(is_decr):
        return False
    if is_incr:
        return "Up!"
    return "Down!"


def is_palindrome(n):
    if n >= 0 and n <= 9:
        return True
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    middle = len(digits)//2
    for indx in range(middle):
        if digits[indx] != digits[-(indx + 1)]:
            return False
    return True


def get_largest_palindrome(n):
    num = n - 1
    while num:
        if is_palindrome(num):
            return num
        num -= 1
    return 0


def sum_of_numbers(random_str):
    sum_num = 0
    indx = 0
    while indx < len(random_str):
        if random_str[indx] >= '0' and random_str[indx] <= '9':
            num_str = random_str[indx]
            i = indx + 1
            while i < len(random_str):
                if(random_str[i] < '0' or random_str[i] > '9'):
                    break
                num_str += random_str[i]
                i += 1
            indx = i
            sum_num += int(num_str)
        indx += 1
    return sum_num


def birthday_ranges(birthdays, ranges):
    birthdays.sort()
    birthdays_count = []
    for rang in ranges:
        start = rang[0]
        end = rang[1]
        temp_count = 0
        for i in range(len(birthdays)):
            if birthdays[i] >= start and birthdays[i] <= end:
                print(i)
                temp_count += 1
        birthdays_count.append(temp_count)
    return birthdays_count


def group(list_1):
    result_list = []
    temp_list = [list_1[0]]
    for indx in range(1, len(list_1)):
        if list_1[indx] != list_1[indx - 1]:
            result_list.append(temp_list)
            temp_list = [list_1[indx]]
        else:
            temp_list.append(list_1[indx])

    result_list.append(temp_list)
    return result_list


def numbers_to_message(numbers):
    keypad = {
              2:['a', 'b', 'c'],
              3:['d', 'e', 'f'],
              4:['g', 'h', 'i'],
              5:['j', 'k', 'l'],
              6:['m', 'n', 'o'],
              7:['p', 'q', 'r', 's'],
              8:['t', 'u', 'v'],
              9:['w', 'x', 'y', 'z']}

    message = ""
    group_of_numbers = group(numbers)
    capital = False
    for gr in group_of_numbers:
        if gr[0] == 1:
            capital = True
        elif gr[0] == 0:
            message += ' '
        elif gr[0] == -1:
            pass
        else:
            len_gr = len(gr)
            len_keypad = len(keypad[gr[0]])
            indx = (len_gr % len_keypad) - 1
            if indx < 0:
                indx = len_keypad - 1
            symbol = keypad[gr[0]][indx]
            if capital:
                message += symbol.upper()
                capital = False
            else:
                message += symbol
    return message


def keystrokes_for_letter(symbol, last_key=-1):
    keypad = {
              ('a', 'b', 'c'): 2,
              ('d', 'e', 'f'): 3,
              ('g', 'h', 'i'): 4,
              ('j', 'k', 'l'): 5,
              ('m', 'n', 'o'): 6,
              ('p', 'q', 'r', 's'): 7,
              ('t', 'u', 'v'): 8,
              ('w', 'x', 'y', 'z'): 9}
    symbol_key = None
    symbol_taps = -1
    for key in keypad.keys():
        if symbol in key:
            symbol_taps = key.index(symbol)
            symbol_key = keypad[key]
            break
    symbol_taps += 1
    strokes = []
    if last_key == symbol_key:
        strokes.append(-1)
    for i in range(symbol_taps):
        strokes.append(symbol_key)

    return strokes


def message_to_numbers(message):
    keystrokes = []
    if message[0].isupper():
        keystrokes.append(1)
        keystrokes.extend(keystrokes_for_letter(message[0].lower()))
    else:
        keystrokes.extend(keystrokes_for_letter(message[0]))
    for i in range(1, len(message)):
        if message[i] == ' ':
            keystrokes.append(0)
        else:
            if message[i].isupper():
                keystrokes.append(1)
                keystrokes.extend(keystrokes_for_letter(message[i].lower(), keystrokes[-1]))
            else:
                keystrokes.extend(keystrokes_for_letter(message[i], keystrokes[-1]))

    return keystrokes
