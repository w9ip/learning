# Построение вспомогательной функции нормализации
# Unicode-строк с помощью partial.
import functools
import unicodedata

nfc = functools.partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'

print(s1, s2)

print(s1 == s2)

print(nfc(s1) == nfc(s2))
