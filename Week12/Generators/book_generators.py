import os
import string
import random


ALL_SYMBOLS = string.ascii_letters + string.digits + string.punctuation
MIN_WORD_LEN = 3
MAX_WORD_LEN = 15
DEFAULT_BOOK = "book.txt"


def book_reader(book_directory):
    pages = filter(lambda f: f.endswith('.txt'), os.listdir(book_directory))
    for page in pages:
        with open(book_directory + '/' + page, 'r') as f:
            line = f.readline()
            lines = [line]  # for first line of chapter
            while line:
                line = f.readline()
                if line == "" or line.startswith('#'):
                    yield ''.join(lines)
                    lines = [line]
                else:
                    lines.append(line)


def book_generator(chapters_count, chapter_len_range, book_name=DEFAULT_BOOK):
    with open(book_name, 'w') as f:
        for chapter_index in range(1, chapters_count + 1):
            chapter_len = random.randint(1, chapter_len_range)
            f.write(chapter_text(chapter_index, chapter_len))


def chapter_text(chapter_index, chapter_len):
    text = "# Chapter {}\n".format(chapter_index)
    for i in range(chapter_len):
        word_len = random.randint(MIN_WORD_LEN, MAX_WORD_LEN)
        word = "".join([random.choice(ALL_SYMBOLS) for j in range(word_len)])
        white_space = random.choice(string.whitespace)
        text += word + white_space
    text += '\n\n'
    return text


def main():
    for chapter in book_reader("Book"):
        print(chapter)
        input()


if __name__ == '__main__':
    main()
