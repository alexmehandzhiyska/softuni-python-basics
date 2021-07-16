import math

year_type = input()
holidays_count = int(input())
weekends_in_town = int(input())

free_weekends_in_sofia = 3/4 * (48 - weekends_in_town)
weekends_to_play = free_weekends_in_sofia + weekends_in_town
holidays_to_play = 2/3 * holidays_count

days_to_play = weekends_to_play + holidays_to_play

if year_type == 'leap':
  days_to_play *= 1.15

print(math.floor(days_to_play))