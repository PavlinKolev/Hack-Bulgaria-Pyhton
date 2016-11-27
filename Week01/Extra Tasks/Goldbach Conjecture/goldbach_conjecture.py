import math


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def goldbach(n):
    goldbach_list = []
    visited = []
    for i in range(2, n):
        if is_prime(i):
            diff = n - i
            if(is_prime(diff)):
                if i not in visited:
                    goldbach_list.append((i, diff))
                    visited.extend([i, diff])
    return goldbach_list
