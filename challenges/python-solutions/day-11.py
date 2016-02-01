import sys

arr = []
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

hourglass_max_sum = -sys.maxsize - 1
for row_index in range(4):
    for col_index in range(4):
        current_sum = arr[row_index][col_index] \
                      + arr[row_index][col_index + 1] \
                      + arr[row_index][col_index + 2] \
                      + arr[row_index + 1][col_index + 1] \
                      + arr[row_index + 2][col_index] \
                      + arr[row_index + 2][col_index + 1] \
                      + arr[row_index + 2][col_index + 2]
        if current_sum > hourglass_max_sum:
            hourglass_max_sum = current_sum

print(hourglass_max_sum)
