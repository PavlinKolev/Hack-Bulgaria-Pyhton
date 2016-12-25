def strawberries(rows, columns, days, dead_strawberries):
    if rows > 1000 or columns > 1000:
        raise ValueError
    ll = make_normal(dead_strawberries, rows, columns)
    return rows*columns - recursion(rows, columns, days, ll, len(ll))


def recursion(rows, columns, days, dead_strawberries, death):
    if days == 0:
        return death
    neighs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    len_ = len(dead_strawberries)
    for i in range(len_):
        for n in neighs:
            point = (dead_strawberries[i][0] + n[0], dead_strawberries[i][1] + n[1])
            if passable(rows, columns, point[0], point[1]):
                if point not in dead_strawberries:
                    death += 1
                    dead_strawberries.append(point)
    return recursion(rows, columns, days - 1, dead_strawberries, death)


def make_normal(ll, rows, cols):
    result = []
    for elem in ll:
        result.append((rows - elem[0], elem[1] - 1))
    return result


def passable(rows, columns, x, y):
    return x >= 0 and x < rows and y >= 0 and y < columns
