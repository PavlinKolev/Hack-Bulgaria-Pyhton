import math


def sum_of_digits(number):
    sum = 0
    if number < 0:
        number *= -1
    while (number > 0):
        sum += number % 10
        number //= 10
    return sum


def to_digits(number):
    return [int(char) for char in str(number)]


def to_number(digits):
    string = ""
    for num in digits:
        string += str(num)
    return int(string)


def count_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


def count_consonants(string):
    consonants = "qQwWrRtTpPsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM"
    count = 0
    for char in string:
        if char in consonants:
            count += 1
    return count


def prime_number(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    max_range = int(math.sqrt(number)) + 1
    for num in range(2, max_range):
        if(number % num == 0):
            return False
    return True


def fact(n):
    if (n <= 1):
        return 1
    return n * fact(n - 1)


def fact_digits(n):
    sum = 0
    while(n > 0):
        sum += fact(n % 10)
        n //= 10
    return sum


def fibonacci(number):
    if(number == 1):
        return [1]
    fibonacci_list = [1, 1]
    for i in range(2, number):
        fib = fibonacci_list[i - 1] + fibonacci_list[i - 2]
        fibonacci_list.append(fib)
    return fibonacci_list


def fib_number(n):
    fib_numbers = fibonacci(n)
    string = ""
    for num in fib_numbers:
        string += str(num)
    return int(string)


def palindrome(string):
    if type(string) != str:
        string = str(string)
    for i in range(len(string) // 2):
        if(string[i] != string[-(i + 1)]):
            return False
    return True


def char_histogram(string):
    dictionary = {}
    for i in range(len(string)):
        temp_count = 1
        for j in range(i+1, len(string)):
            if(string[i] == string[j]):
                temp_count += 1
        if string[i] not in dictionary.keys():
            dictionary[string[i]] = temp_count
    return dictionary
