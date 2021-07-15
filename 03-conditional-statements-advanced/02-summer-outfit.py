degrees = int(input())
part_of_day = input()

outfit = 'Shirt'
shoes = 'Moccasins'

if part_of_day == 'Morning':
  if degrees >= 10 and degrees <= 18:
    outfit = 'Sweatshirt'
    shoes = 'Sneakers'
  elif degrees >= 25:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
elif part_of_day == 'Afternoon':
  if degrees > 18 and degrees <= 24:
    outfit = 'T-Shirt'
    shoes = 'Sandals'
  elif degrees >= 25:
    outfit = 'Swim Suit'
    shoes = 'Barefoot'

print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')