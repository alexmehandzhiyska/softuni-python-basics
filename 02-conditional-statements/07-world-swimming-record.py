old_record_sec = float(input())
distance_m = float(input())
time_per_m = float(input())

additional_time = distance_m // 15 * 12.5
total_time = time_per_m * distance_m + additional_time

if (old_record_sec <= total_time):
    print(f"No, he failed! He was {'{:.2f}'.format(total_time - old_record_sec)} seconds slower.")
else:
    print(f"Yes, he succeeded! The new world record is {'{:.2f}'.format(total_time)} seconds.")