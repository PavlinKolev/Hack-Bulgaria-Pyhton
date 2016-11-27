def count_substrings(haystack, needle):
    count_substrings = haystack.count(needle)
    return count_substrings


def sum_matrix(m):
    sum_m = 0
    for line in m:
        sum_m += sum(line)
    return sum_m


def nan_expand(times):
    if times <= 0:
        return ""
    result = ""
    for indx in range(times):
        result += "Not a "
    result += "NaN"
    return result


def prime_factorization(n):
    nat_number = 2
    temp_pow = 0
    prime_numbers = []
    while n > 1:
        if (n % nat_number) != 0:
            if(temp_pow > 0):
                prime_numbers.append((nat_number, temp_pow))
            temp_pow = 0
            nat_number += 1
        else:
            n //= nat_number
            temp_pow += 1
    prime_numbers.append((nat_number, temp_pow))
    return prime_numbers


def group(list_1):
    result_list = []
    temp_list = [list_1[0]]
    for indx in range(1, len(list_1)):
        if list_1[indx] != list_1[indx-1]:
            result_list.append(temp_list)
            temp_list = [list_1[indx]]
        else:
            temp_list.append(list_1[indx])
    result_list.append(temp_list)
    return result_list


def max_consecutive(items):
    group_items = group(items)
    max_len = 0
    for sublist in group_items:
        if max_len < len(sublist):
            max_len = len(sublist)
    return max_len


def count_sublist(main_list, sub_list):
    if len(sub_list) > len(main_list):
        return 0
    main_str = "".join(main_list)
    sub_str = "".join(sub_list)
    return count_substrings(main_str, sub_str)


def word_count(word, table_lines, row_count, col_count):
    table_cols = [[table_lines[indx_2][indx] for indx_2 in range(row_count)] for indx in range(col_count)]

    reverse_word = word[::-1]
    count = 0
    for i in range(row_count):
        count += count_sublist(table_lines[i], word)
        count += count_sublist(table_lines[i], reverse_word)

    for i in range(col_count):
        count += count_sublist(table_cols[i], word)
        count += count_sublist(table_cols[i], reverse_word)

    diagonal = []
    i = 0
    j = 0
    while (i < row_count and j < col_count):
        diagonal.append(table_lines[i][j])
        i += 1
        j += 1

    count += count_sublist(diagonal, word)
    count += count_sublist(diagonal, reverse_word)
    return count
