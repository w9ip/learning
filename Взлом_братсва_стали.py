string_count = int(input()[1:])
for i in range(string_count):
    s = input().split('#')
    res = s[0].rstrip()
    print(res)


