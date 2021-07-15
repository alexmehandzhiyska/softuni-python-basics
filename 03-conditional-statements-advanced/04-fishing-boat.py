budget = int(input())
season = input()
fishers_count = int(input())

rent_prices = { 'Spring': 3000, 'Summer': 4200, 'Autumn': 4200, 'Winter': 2600 }
rent = rent_prices[season]

if fishers_count <= 6:
  rent *= 0.9
elif fishers_count <= 11:
  rent *= 0.85
else:
  rent *= 0.75

if fishers_count % 2 == 0 and season != 'Autumn':
  rent *= 0.95

difference = abs(budget - rent)

if budget >= rent:
  print(f'Yes! You have {"{:.2f}".format(difference)} leva left.')
else:
  print(f'Not enough money! You need {"{:.2f}".format(difference)} leva.')