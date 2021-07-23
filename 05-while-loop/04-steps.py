command = input()
total_steps = 0

while command != 'Going home':
  current_steps = int(command)
  total_steps += current_steps

  if total_steps >= 10000:
    print(f'Goal reached! Good job!\n{total_steps - 10000} steps over the goal!')
    exit()
  
  command = input()

steps_to_home = int(input())
total_steps += steps_to_home

if total_steps >= 10000:
    print(f'Goal reached! Good job!\n{total_steps - 10000} steps over the goal!')
else:
  print(f'{10000 - total_steps} more steps to reach goal.')