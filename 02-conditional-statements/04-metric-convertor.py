num = float(input())
initial_unit = input()
target_unit = input()

units = { 'mm': 1, 'cm': 10, 'm': 1000}

result = num * units[initial_unit] / units[target_unit]
print('{0:.3f}'.format(result))