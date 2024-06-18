from sys import stdin

text = ''
for string in stdin.readlines():
    if '-\n' in string:
        string = string.replace('-\n', '')
    text += string.replace('\n', ' ')
print(text)
