width = int(input())
length = int(input())

pieces = width * length

while pieces > 0:
  command = input()

  if command == 'STOP':
    print(f'{pieces} pieces are left.')
    exit()

  pieces_eaten = int(command)
  pieces -= pieces_eaten

print(f'No more cake left! You need {abs(pieces)} pieces more.')