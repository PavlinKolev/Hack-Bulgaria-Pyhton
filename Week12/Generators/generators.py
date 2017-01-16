import os
import string
import random


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


def read_chapter(book_directory):
    file_names = os.listdir(book_directory)
    for name in file_names:
        with open(book_directory + '/' + name, 'r') as f:
            line = f.readline()
            lines = [line]  # for first line of chapter
            while line:
                line = f.readline()
                if line == "" or line.startswith('#'):
                    yield ''.join(lines)
                    lines = [line]
                else:
                    lines.append(line)


def generate_book(chapters_count, chapter_len_range):
    ALL_SYMBOLS = string.ascii_letters + string.digits + string.punctuation
    MIN_WORD_LEN = 3
    MAX_WORD_LEN = 15
    book = "book.txt"
    f = open(book, 'w')
    for i in range(1, chapters_count + 1):
        text = "# Chapter {}\n".format(i)
        for i in range(chapter_len_range):
            word_len = random.randint(MIN_WORD_LEN, MAX_WORD_LEN)
            word = "".join([random.choice(ALL_SYMBOLS) for i in range(word_len)])
            symbol = random.choice(string.whitespace)
            text += word + symbol
        text += '\n'
        f.write(text)
    f.close()
