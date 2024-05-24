n = int(input())
second_digit = n % 10
while n // 10 != 0:
  last_digit = n % 10
  n = n // 10
  if n // 10 == 0:
    second_digit = last_digit
print(second_digit)