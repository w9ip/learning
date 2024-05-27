s = input()
largest = 0
frequent_char = ''
for c in s:
    if s.count(c) > largest:
        largest = s.count(c)
for c in s:
    if s.count(c) == largest:
        frequent_char = c
print(frequent_char)
