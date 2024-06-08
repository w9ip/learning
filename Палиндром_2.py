def is_palindrome(text):
    text = text.replace(' ', '').replace(',', '').replace('.', '').replace('!', '').replace('?', '').replace('-', '')
    if text[::-1].lower() == text.lower():
        return True
    else:
        return False
print(is_palindrome('А роза упала на лапу Азора.'))
print(is_palindrome('Gabler Ruby - burrel bag!'))
print(is_palindrome('BEEGEEK'))