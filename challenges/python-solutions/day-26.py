import datetime


def get_fine(actual_date_str, expected_date_str):
    actual_date = datetime.date(actual_date_str[2], actual_date_str[1], actual_date_str[0])
    expected_date = datetime.date(expected_date_str[2], expected_date_str[1], expected_date_str[0])
    if actual_date < expected_date:
        return 0
    elif actual_date.year == expected_date.year:
        if actual_date.month == expected_date.month:
            difference_of_days = actual_date.day - expected_date.day
            return 15 * difference_of_days
        else:
            difference_of_months = actual_date.month - expected_date.month
            return 500 * difference_of_months
    else:
        return 10000


actual_return_date = [int(e) for e in input().split(' ')]
expected_return_date = [int(e) for e in input().split(' ')]
print(str(get_fine(actual_return_date, expected_return_date)))
