num1 = int(input())
num2 = int(input())
valid_nums = []

for num in range(num1, num2 + 1):
  num_str = str(num)
  sum_odd = int(num_str[1]) + int(num_str[3]) + int(num_str[5])
  sum_even = int(num_str[0]) + int(num_str[2]) + int(num_str[4])
  
  if sum_even == sum_odd:
    valid_nums.append(num_str)

if len(valid_nums) > 0:
  print((' ').join(valid_nums))
