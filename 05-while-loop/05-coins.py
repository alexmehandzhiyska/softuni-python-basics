import math

coins = 0
sum = float(input()) * 100

while sum > 0:
  if sum >= 200:
    sum -= 200
  elif sum >= 100:
    sum -= 100
  elif sum >= 50:
    sum -= 50
  elif sum >= 20:
    sum -= 20
  elif sum >= 10:
    sum -= 10
  elif sum >= 5:
    sum -= 5
  elif sum >= 2:
    sum -= 2
  else:
    sum -= 1

  coins += 1
  sum = math.floor(sum)

print(coins)