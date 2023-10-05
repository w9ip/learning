alphabet = 'abcdefghijklmnopqrstuvwxyz'

s = "The quick brown fox jumps over the lazy dog"

print(all(e in s for e in alphabet))