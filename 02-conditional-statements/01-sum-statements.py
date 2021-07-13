seconds_1 = int(input())
seconds_2 = int(input())
seconds_3 = int(input())

sum = seconds_1 + seconds_2 + seconds_3

minutes = sum // 60
seconds = sum % 60 if sum % 60 > 9 else '0' + str(sum % 60) 

print(f'{minutes}:{seconds}')
