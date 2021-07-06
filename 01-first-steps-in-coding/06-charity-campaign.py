days = int(input())
confectioners_count = int(input())
cakes_count = int(input())
waffles_count = int(input())
pancakes_count = int(input())

sum_per_confectioner = cakes_count * 45 + waffles_count * 5.8 + pancakes_count * 3.2
sum_per_day = sum_per_confectioner * confectioners_count

total_sum = days * sum_per_day
final_sum = 7/8 * total_sum

print(final_sum)