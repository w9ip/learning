lst = []
counter = 1
for i in range(ord('a'), ord('z') + 1):
    lst.append(chr(i) * counter)
    counter += 1
print(lst)