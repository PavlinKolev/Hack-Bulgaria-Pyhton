def binary_search(array, start, end, element):
    if start > end:
        return False
    middle = (end + start)//2
    if array[middle] is element:
        return middle
    if array[middle] < element:
        return binary_search(array, middle + 1, end, element)
    else:
        return binary_search(array, start, middle - 1, element)


def find_turning_point(array, start, end):
    if end <= start:
        return False
    middle = (start + end)//2
    if (end - start) % 2 == 1:
        middle += 1
    if array[middle - 1] < array[middle]:
        res = find_turning_point(array, start, middle - 1)
        if res is False:
            return find_turning_point(array, middle, end)
        else:
            return res
    else:
        return "Turning point is {} on index {}.".format(array[middle], middle)
