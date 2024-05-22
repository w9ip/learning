c1, c2, c3 = input(), input(), input()

if len(c1) == min(len(c1), len(c2), len(c3)):
    print(c1)
elif len(c2) == min(len(c1), len(c2), len(c3)):
    print(c2)
elif len(c3) == min(len(c1), len(c2), len(c3)):
    print(c3)

if len(c1) == max(len(c1), len(c2), len(c3)):
    print(c1)
elif len(c2) == max(len(c1), len(c2), len(c3)):
    print(c2)
elif len(c3) == max(len(c1), len(c2), len(c3)):
    print(c3)
