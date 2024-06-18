n = int(input())
print(
    *[
        [e for e in range(1, n + 1)]
        for _ in range(n)
    ],
    sep='\n'
)
