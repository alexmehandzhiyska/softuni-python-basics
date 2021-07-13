initial_points = int(input())
bonus = 0

if initial_points <= 100:
    bonus = 5
elif initial_points <= 1000:
    bonus = 0.2 * initial_points
else:
    bonus = 0.1 * initial_points

if initial_points % 2 == 0:
    bonus += 1
elif initial_points % 5 == 0:
    bonus += 2

print(bonus)
print(initial_points + bonus)