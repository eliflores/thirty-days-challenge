n = int(input().strip())
c = '#'
number_of_spaces = n - 1
number_of_c = 1
for i in range(n):
    for j in range(number_of_spaces):
        print(' ', end="")
    for k in range(number_of_c):
        print(c, end="")
    number_of_c += 1
    number_of_spaces -= 1
    print("")
