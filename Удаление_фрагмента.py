s = input()
first = s.find('h')
last = s.rfind('h')
print(s[:first]+s[last+1:])
