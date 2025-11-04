foods = []
prices = []
total = 0

while True:
    food = input("Please enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break

    else:
        price = float(input(f"Enter the price of a {food} Ksh "))
        foods.append(food)
        prices.append(price)

print("-----YOUR CAT-----")
for food in foods:
     print(food, end= " ")
for price in prices:
    total += price

print()
print(f"Your Total Is: Ksh{total}")