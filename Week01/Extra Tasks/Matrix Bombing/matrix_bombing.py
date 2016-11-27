def value_after_attack(i, j, indx_1, indx_2, m):
    if(indx_1 == i and indx_2 == j):
        return m[i][j]

    if(indx_1 in range(i-1, i+2) and (indx_2 in range(j-1, j+2))):
        after_attack = m[indx_1][indx_2] - m[i][j]
        if(after_attack < 0):
            after_attack = 0
        return after_attack

    return m[indx_1][indx_2]


def attack_at_pos(i, j, m):
    sum_matrix = 0
    for indx_1 in range(len(m)):
        for indx_2 in range(len(m[i])):
            sum_matrix += value_after_attack(i, j, indx_1, indx_2, m)
    return sum_matrix


def matrix_bombing_plan(m):
    bombing_plan_dict = {}
    for i in range(len(m)):
        for j in range(len(m[i])):
            bombing_plan_dict[(i, j)] = attack_at_pos(i, j, m)
    return bombing_plan_dict
