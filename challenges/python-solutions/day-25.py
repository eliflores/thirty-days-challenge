import math


def is_prime_number(number):
    if number < 2:
        return False

    if number == 2 or number == 3:
        return True

    if number % 2 == 0 or number % 3 == 0:
        return False

    number_sqrt = math.sqrt(number)
    int_number_sqrt = int(number_sqrt) + 1

    for d in range(6, int_number_sqrt, 6):
        if number % (d - 1) == 0 or number % (d + 1) == 0:
            return False
    return True


test_cases = int(input())
numbers = []
for test_case in range(test_cases):
    numbers.append(int(input()))

for n in numbers:
    if is_prime_number(n):
        print('Prime')
    else:
        print('Not prime')
