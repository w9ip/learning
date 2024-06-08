def is_pangram(text):
  alphabet = [chr(e) for e in range(ord('a'), ord('a') + 26)]
  for c in alphabet:
    if c not in text.lower():
      return False
  return True
  
# считываем данные
print(is_pangram('Jackdaws love my big sphinx of quartz'))
print(is_pangram('The jay pig fox zebra and my wolves quack'))
print(is_pangram('Hello world'))