money_needed = float(input())
current_money = float(input())
days = 0
days_spent = 0

while current_money < money_needed:
  days += 1

  action = input()
  money = float(input())

  if action == 'save':
    current_money += money
    days_spent = 0
  else:
    days_spent += 1

    if days_spent == 5:
      print(f'You can\'t save the money. \n{days}')
      exit()
    
    current_money -= money

    if current_money < 0:
      current_money = 0
  
print(f'You saved the money for {days} days.')