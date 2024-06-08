text = input()
counter = 0
for word in text.split():
    for article in 'a A an An the The'.split():
        if word == article:
            counter += 1
print(f'Общее количество артиклей: {counter}')