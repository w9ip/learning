k = int(input())  # Ключ (сдвиг)
text = input()  # Зашифрованный текст.

for c in text:
    if ord(c) - k < 97:
        print(chr((ord(c) - k) + 26), end='')
    else:
        print(chr(ord(c) - k), end='')
