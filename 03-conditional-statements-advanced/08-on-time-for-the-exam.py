exam_start_hour = int(input())
exam_start_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

exam_start_time = exam_start_hour * 60 + exam_start_min
arrival_time = arrival_hour * 60 + arrival_min
difference = abs(exam_start_time - arrival_time)


if exam_start_time == arrival_time:
  print('On time')
elif exam_start_time > arrival_time:
  if difference >= 60:
    difference_hours = difference // 60
    difference_min = difference % 60 if difference % 60 >= 10 else '0' + str(difference % 60)
    print(f'Early\n{difference_hours}:{difference_min} hours before the start')
  elif difference > 30:
    print(f'Early\n{difference} minutes before the start')
  else:
    print(f'On time\n{difference} minutes before the start')
else:
  if difference < 60:
    print(f'Late\n{difference} minutes after the start')
  else:
    difference_hours = difference // 60
    difference_min = difference % 60 if difference % 60 >= 10 else '0' + str(difference % 60)
    print(f'Late\n{difference_hours}:{difference_min} hours after the start')