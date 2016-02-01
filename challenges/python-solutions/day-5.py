test_cases = int(input().strip())

user_input_lines = []
for i in range(test_cases):
    line_input = input()
    user_input_lines.append(line_input)

for line_input in user_input_lines:
    line_input_parsed = line_input.split(" ")
    a = int(line_input_parsed[0])
    b = int(line_input_parsed[1])
    N = int(line_input_parsed[2])

    sum = a
    for e in range(N):
        sum += pow(2, e) * b
        print(sum, end=" ")
    print("")

