string = input()
prime_sum = 0
non_prime_sum = 0

while string != 'stop':
  num = int(string)

  if num < 0:
    print('Number is negative.')
  else:
    is_prime = True

    if num > 1:
      for i in range(2, num):
        if num % i == 0:
          is_prime = False
          break
      
    if is_prime:
      prime_sum += num
    else:
      non_prime_sum += num
    
  string = input()

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')