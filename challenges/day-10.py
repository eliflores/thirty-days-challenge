# Convert a given number, n, from decimal (base 10) to binary (base 2).
test_cases = int(input().strip())
BASE = 2
binary_numbers = []
for test_case in range(0, test_cases):
    n = int(input().strip())
    result = 0
    binary_number = []
    while n != 0:
        remainder = n % BASE
        n //= BASE
        binary_number.insert(0, str(remainder))
    binary_numbers.append(''.join(binary_number))

for binary_number in binary_numbers:
    print(binary_number)
