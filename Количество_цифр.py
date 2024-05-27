s = input()
total = 0
for i in range(len(s)):
    if '0' <= s[i] <= '9':
        total += 1
print(total)