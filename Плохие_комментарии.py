n = int(input())
for i in range(n):
    s = input()
    if not s or s.isspace():
        print(str(i + 1) + ':', 'COMMENT SHOULD BE DELETED')
    else:
        print(str(i + 1) + ':', s)
