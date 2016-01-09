n = int(input().strip())

phone_book = {}
for i in range(0, n):
    name = input().strip()
    phone_number = input().strip()
    phone_book[name] = phone_number

queried_name = input().strip()
while queried_name != '':
    foundPhoneNumber = phone_book.get(queried_name)
    if foundPhoneNumber is None:
        print("Not found")
    else:
        print(queried_name + "=" + foundPhoneNumber)
    queried_name = input().strip()
