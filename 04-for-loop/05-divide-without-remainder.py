n = int(input())
p1 = p2 = p3 = 0

for i in range(n):
  num = int(input())

  if num % 2 == 0:
    p1 += 1
  if num % 3 == 0:
    p2 += 1
  if num % 4 == 0:
    p3 += 1

print(f'{"{:.2f}".format(p1 / n * 100)}%')
print(f'{"{:.2f}".format(p2 / n * 100)}%')
print(f'{"{:.2f}".format(p3 / n * 100)}%')