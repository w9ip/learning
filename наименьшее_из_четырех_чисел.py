a = int(input())
b = int(input())
c = int(input())
d = int(input())

l1 = 0
l2 = 0

if a < b:
    l1 = a
else:
    l1 = b
    
if c < d:
    l2 = c
else:
    l2 = d

if l1 < l2:
    print(l1)
else:
    print(l2)
