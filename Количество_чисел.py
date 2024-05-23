a, b = int(input()), int(input())
counter = 0
for i in range(a, b + 1):
    end_n = i ** 3 % 10
    if end_n == 4 or end_n == 9:
        counter += 1
print(counter)
