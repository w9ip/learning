n = int(input())
l_digit = n % 10
counter_3 = 0
counter_l_digit = 0
counter_even = 0
total_gt_5 = 0
multiple_gt_7 = 1
counter_0_5 = 0
while n != 0:
    last_digit = n % 10
    if last_digit == 3:
        counter_3 += 1
    if last_digit == l_digit:
        counter_l_digit += 1
    if not last_digit & 1:
        counter_even += 1
    if last_digit > 5:
        total_gt_5 += last_digit
    if last_digit > 7:
        multiple_gt_7 *= last_digit
    if last_digit == 0:
        counter_0_5 += 1
    if last_digit == 5:
        counter_0_5 += 1
    n //= 10

print(
    counter_3,
    counter_l_digit,
    counter_even,
    total_gt_5,
    multiple_gt_7,
    counter_0_5,
    sep='\n'
)
