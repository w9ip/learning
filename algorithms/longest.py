def longest(a1, a2):
    # your code
    return ''.join(sorted(set(a1) | set(a2)))


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))
