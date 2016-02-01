import sys


def min_difference(arr):
    diff_dict = {}
    min_diff = sys.maxsize
    for i in range(len(arr) - 1):
        difference = abs(arr[i] - arr[i + 1])
        differences_list = diff_dict.get(difference)
        pair = (arr[i], arr[i + 1])
        if differences_list:
            if pair not in differences_list:
                differences_list.append(pair)
        else:
            diff_dict[difference] = [pair]

        if difference < min_diff:
            min_diff = difference

    min_diff_list = diff_dict[min_diff]
    print(min_diff_list, file=sys.stderr)
    for (v1, v2) in sorted(min_diff_list):
        print(v1, v2, end=' ')


n = int(input())
arr = [int(e) for e in input().split(' ')]
min_difference(sorted(arr))
