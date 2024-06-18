word = input() + ' запретил букву'
ru_alphabet = [chr(e) for e in range(ord('а'), ord('а') + 32)]
for i in range(len(ru_alphabet)):
    if ru_alphabet[i] in word:
        print(word.strip(), ru_alphabet[i])
        word = word.replace(ru_alphabet[i], '').replace('  ', ' ')
