hours = int(input())
minutes = int(input())

total = hours * 60 + minutes + 15
new_hours = total // 60
new_minutes = total % 60

if new_hours == 24:
    new_hours = 0

if new_minutes < 10:
    new_minutes = f'0{new_minutes}'


print(f'{new_hours}:{new_minutes}')