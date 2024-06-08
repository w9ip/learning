def is_correct_bracket(text):
    stack = []
    for c in text:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return True if not stack else False


print(is_correct_bracket('())((((())))'))