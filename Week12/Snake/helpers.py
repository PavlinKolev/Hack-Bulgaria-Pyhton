from random import randint


def gen_random_pair(start, end):
    # import ipdb; ipdb.set_trace()
    pair_set = set()
    x = randint(start, end)
    y = randint(start, end)

    while True:
        pair_set.add((x, y))
        yield (x, y)
        x = randint(start, end)
        y = randint(start, end)
        while (x, y) in pair_set:
            x = randint(start, end)
            y = randint(start, end)


def gen_next_coords(temp, direction):
    return temp - direction
