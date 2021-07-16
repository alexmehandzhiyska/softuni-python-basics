n = int(input())
p1 = p2 = p3 = p4 = p5 = 0

for i in range(n):
  num = int(input())

  if num < 200:
    p1 += 1
  elif num < 400:
    p2 += 1
  elif num < 600:
    p3 += 1
  elif num < 800:
    p4 += 1
  else:
    p5 += 1

print(f'{"{:.2f}".format(p1 / n * 100)}%')
print(f'{"{:.2f}".format(p2 / n * 100)}%')
print(f'{"{:.2f}".format(p3 / n * 100)}%')
print(f'{"{:.2f}".format(p4 / n * 100)}%')
print(f'{"{:.2f}".format(p5 / n * 100)}%')