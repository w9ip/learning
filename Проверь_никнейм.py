s = input()
if s.startswith('@') and 5 <= len(s) <= 15 and s == s.lower() and s[1:].isalnum():
    print('Correct')
else:
    print('Incorrect')
