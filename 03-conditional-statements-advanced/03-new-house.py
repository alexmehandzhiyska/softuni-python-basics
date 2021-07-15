flowers_type = input()
flowers_count = int(input())
budget = int(input())

flowers_prices = { 'Roses': 5, 'Dahlias': 3.8, 'Tulips': 2.8, 'Narcissus': 3, 'Gladiolus': 2.5}

price = flowers_count * flowers_prices[flowers_type]

if flowers_type == 'Roses' and flowers_count > 80:
  price *= 0.9
elif flowers_type == 'Dahlias' and flowers_count > 90:
  price *= 0.85
elif flowers_type == 'Tulips' and flowers_count > 80:
  price *= 0.85
elif flowers_type == 'Narcissus' and flowers_count < 120:
  price *= 1.15
elif flowers_type == 'Gladiolus' and flowers_count < 80:
  price *= 1.2

difference = abs(budget - price)

if budget >= price:
  print(f'Hey, you have a great garden with {flowers_count} {flowers_type} and {"{:.2f}".format(difference)} leva left.')
else:
  print(f'Not enough money, you need {"{:.2f}".format(difference)} leva more.')