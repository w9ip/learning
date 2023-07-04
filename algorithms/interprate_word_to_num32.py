def base32(w):
    val = 0
    for ch in w.lower():  # Преобразуем буквы строки в строчные.
        next_digit = ord(ch) - ord('a')  # Вычислим значение очередной цифры.
        val = 32 * val + next_digit  # Припишем цифру в конец результата.
    return val



print(base32('привет'))