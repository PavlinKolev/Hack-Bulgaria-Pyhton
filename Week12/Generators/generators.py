def chain(iterable_1, iterable_2):
    for x in iterable_1:
        yield x
    for x in iterable_2:
        yield x


def compress(iterable, mask):
    for i in range(len(iterable)):
        if mask[i]:
            yield iterable[i]


def cycle(iterable):
    while True:
        for x in iterable:
            yield x
