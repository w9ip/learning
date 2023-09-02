def is_valid(b):
    d = {
        '}': '{',
        ']': '[',
        ')': '(',
         }
    s = []
    for i in b:
        if i in '[{(':
            s.append(i)
        else:
            if s and (d[i] == s[-1]):
                s.pop()
            else:
                return False
    return True if not s else False



assert is_valid('(){}{}[]') == True
is_valid('((){}{}[])')
is_valid('({[]})')
is_valid('({[]{}[{}]})')
print(is_valid('()'))
print(is_valid("()[]{}"))
print(is_valid("]"))
