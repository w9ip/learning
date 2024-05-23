largest1 = 0
largest2 = 0
for i in range(int(input())):
    n = int(input())
    if n > largest1:
        largest2, largest1 = largest1, n
    elif largest1 > largest2 < n:
        largest2 = n
print(largest1, largest2, sep='\n')
