def is_anagram(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    len_1 = len(str_1)
    len_2 = len(str_2)

    if(len_1 != len_2):
        return False

    dict_str_2 = {}
    for char in str_2:
        dict_str_2[char] = 0

    for char in str_1:
        dict_str_2[char] = 1

    for char in str_2:
        if (dict_str_2[char] == 0):
            return False
    return True
