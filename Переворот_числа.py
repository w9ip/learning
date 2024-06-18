s = input()
print(int(s[::-1]) if len(s) == 5 else int(s[0] + s[::-1][:-1]))