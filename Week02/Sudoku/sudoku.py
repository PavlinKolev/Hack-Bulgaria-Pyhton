def sub_matrix(start_i, start_j, sudoku):
    result = []
    for indx_1 in range(3):
        for indx_2 in range(3):
            result.append(sudoku[start_i + indx_1][start_j+indx_2])

    return result


def sudoku_solved(sudoku):
    size = 9
    for indx in range(size):
        if not(len(set(sudoku[indx])) == size):
            return False

    for indx in range(size):
        if not(len(set([sudoku[x][indx] for x in range(size)])) == size):
            return False

    for indx_1 in range(3):
        for indx_2 in range(3):
            if not(len(set(sub_matrix(indx_1*3, indx_2*3,sudoku))) == size):
                return False

    return True
