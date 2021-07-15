degrees = int(input())
part_of_day = input()

outfit = ''
shoes = ''

if part_of_day == 'Morning':
  if degrees >= 10 and degrees <= 18:
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'
  elif degrees <= 24:
    outfit = 'Shirt'
    shoes = 'Moccasins'
  else:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif part_of_day == 'Afternoon':
  if degrees >= 10 and degrees <= 18:
    outfit = 'Shirt'
    shoes = 'Moccasins'
  elif degrees <= 24:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
  else:
    outfit = 'Swim Suit'
    shoes = 'Barefoot'
else:
  outfit = 'Shirt'
  shoes = 'Moccasins'

print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')