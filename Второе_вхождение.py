s = input()
counter = 0
for i in range(len(s)):
    if 'f' not in s:
        print(-2)
        break
    else:
        if s[i] == 'f':
            counter += 1
            if counter == 2:
                print(i)
                break
else:
    print(-1)
