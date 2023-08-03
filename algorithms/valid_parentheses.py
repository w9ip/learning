def is_valid(s):
    d = {
        '}': '{',
        ']': '[',
        ')': '(',
         }
    s = []
    for i in s:
        if i in '[{(':
            s.append(i)
        else:
            if d[i] == s[-1]:
                s.pop()
    print(s)


is_valid('(){}{}[]')
