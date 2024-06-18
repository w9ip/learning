s = input().split()
result = [[]]
for i in range(len(s)):
    for j in range(len(s)-i):
        result.append(s[j:j + i + 1])
print(result)
