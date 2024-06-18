n, k = int(input()), int(input())
winner = 0
for i in range(1, n + 1):
    winner = (winner + k) % i
print(winner + 1)
