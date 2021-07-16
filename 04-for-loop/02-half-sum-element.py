n = int(input())

max_num = 0
sum = 0

for i in range(n):
  num = int(input())

  if num > max_num:
    max_num = num

  sum += num

if max_num == sum - max_num:
  print(f'Yes\nSum = {max_num}')
else:
  print(f'No\nDiff = {abs(max_num - (sum - max_num))}')