n = int(input().strip())

phone_book = {}
for i in range(n):
    name = input().strip()
    phone_number = input().strip()
    phone_book[name] = phone_number

queried_name = input().strip()
while queried_name != '':
    found_phone_number = phone_book.get(queried_name)
    if found_phone_number is None:
        print("Not found")
    else:
        print(queried_name + "=" + found_phone_number)
    queried_name = input().strip()
