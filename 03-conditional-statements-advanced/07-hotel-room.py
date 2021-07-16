month = input()
nights = int(input())
 
studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
  studio_price = nights * 50
  apartment_price = nights * 65

  if nights > 14:
    studio_price *= 0.7
  elif nights > 7:
    studio_price *= 0.95

elif month == 'June' or month == 'September':
  studio_price = nights * 75.2
  apartment_price = nights * 68.7

  if nights > 14:
    studio_price *= 0.8

else:
  studio_price = nights * 76
  apartment_price = nights * 77

if nights > 14:
  apartment_price *= 0.9

print(f'Apartment: {"{:.2f}".format(apartment_price)} lv.\nStudio: {"{:.2f}".format(studio_price)} lv.')