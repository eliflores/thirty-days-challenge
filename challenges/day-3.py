#!/bin/python3

number = int(input().strip())
remainder = number % 2

if remainder == 0:
    if 2 <= number <= 5:
        print("Not Weird")
    elif 6 <= number <= 20:
        print("Weird")
    elif number > 20:
        print("Not Weird")
else:
    print ("Weird")
