meal_price = float(input())
tip = float(input())
tax = float(input())

total_price = meal_price + ((meal_price * tip) / 100) + ((meal_price * tax) / 100)
total_price_rounded = round(total_price)

print("The final price of the meal is $" + str(total_price_rounded) + ".")