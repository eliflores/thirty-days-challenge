# Euclid's Algorithm for Computing the GCD of two integers
def find_gcd(a, b):
    if a == b or b == 0:
        return a
    return find_gcd(b, a % b)


numbers_from_input = input().strip().split(' ')
gcd = find_gcd(int(numbers_from_input[0]), int(numbers_from_input[1]))
print(gcd)