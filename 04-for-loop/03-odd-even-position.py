n = int(input())

odd_nums = []
even_nums = []

for i in range(1, n + 1):
  num = float(input())
  
  if i % 2 == 0:
    even_nums.append(num)
  else:
    odd_nums.append(num)

print(f'OddSum={"{:.2f}".format(sum(odd_nums))},')
print(f'OddMin={"{:.2f}".format(min(odd_nums)) if len(odd_nums) != 0 else "No"},')
print(f'OddMax={"{:.2f}".format(max(odd_nums)) if len(odd_nums) != 0 else "No"},')

print(f'EvenSum={"{:.2f}".format(sum(even_nums))},')
print(f'EvenMin={"{:.2f}".format(min(even_nums)) if len(even_nums) != 0 else "No"},')
print(f'EvenMax={"{:.2f}".format(max(even_nums)) if len(even_nums) != 0 else "No"}')