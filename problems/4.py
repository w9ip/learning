N, M = map(int, input().split())
for i in range(N):
    for j in range(M):
        print(str(i+j*N+1).ljust(3, ' '), end='')
    print()
