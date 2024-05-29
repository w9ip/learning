s = input()
one = s.find('h')
two = s.rfind('h')
print(s[:one] + s[two:one:-1] + s[two:])
