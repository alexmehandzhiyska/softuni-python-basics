n = int(input())
l = int(input())
passwords = []

for i in range(1, n + 1):
  for j in range(1, n + 1):
    for k in range(97, l + 97):
      for m in range(97, l + 97):
        for o in range(1, n + 1):
          if o > i and o > j:
            letter_1 = chr(k)
            letter_2 = chr(m)
            passwords.append(f'{i}{j}{letter_1}{letter_2}{o}')
          
print(' '.join(passwords))