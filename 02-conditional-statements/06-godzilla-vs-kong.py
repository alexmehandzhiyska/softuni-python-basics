budget = float(input())
people = int(input())
price_per_person = float(input())

clothes_price = price_per_person * people
decor = 0.1 * budget

if people > 150:
    clothes_price *= 0.9

total = decor + clothes_price

if budget >= total:
    print(f"Action!\nWingard starts filming with {'{:.2f}'.format(budget - total)} leva left.")
else:
    print(f"Not enough money!\nWingard needs {'{:.2f}'.format(total - budget)} leva more.")
