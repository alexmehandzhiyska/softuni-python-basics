import sys

open_tabs = int(input())
salary = int(input())

website_fines = { 'Facebook': 150, 'Instagram': 100, 'Reddit': 50 }

for i in range(open_tabs):
  current_website = input()

  if current_website in website_fines:
    current_fine = website_fines[current_website]

    salary -= current_fine

    if salary <= 0:
      print('You have lost your salary.')
      exit()

print(salary)