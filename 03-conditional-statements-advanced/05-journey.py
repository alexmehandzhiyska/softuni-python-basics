budget = float(input())
season = input()

destination = ''
place = ''
price = 0

if season == 'summer':
  place = 'Camp'
else:
  place = 'Hotel'

if budget <= 100:
  destination = 'Bulgaria'

  if season == 'summer':
    price = budget * 0.3
  else:
    price = budget * 0.7

elif budget <= 1000:
  destination = 'Balkans'

  if season == 'summer':
    price = budget * 0.4
  else:
    price = budget * 0.8

else:
  destination = 'Europe'
  place = 'Hotel'
  price = budget * 0.9

print(f'Somewhere in {destination}\n{place} - {"{:.2f}".format(price)}')