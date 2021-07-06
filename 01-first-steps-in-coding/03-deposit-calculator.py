deposited_sum = float(input())
deposit_deadline = int(input())
annual_interest = float(input())

total_interest = deposited_sum * (annual_interest / 100)

sum = deposited_sum + deposit_deadline * (total_interest / 12)
print(sum)