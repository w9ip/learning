def convert_to_python_case(text):
    text = list(text)
    text[0] = text[0].lower()
    total = 0
    for c in text:
        if c.isupper():
            total += 1
    for i in range(1, len(text) + total):
        if text[i].isupper():
            text[i] = text[i].lower()
            text.insert(i, '_')
    return ''.join(text)


print(convert_to_python_case('IsHeFreeToGo'))
print(convert_to_python_case('IsPrimeNumber'))
