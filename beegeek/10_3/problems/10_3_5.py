s = [e.lower().strip('.,!?:;-') for e in input().split()]
result = {}

for word in s:
    result[word] = result.get(word, 0) + 1

min_word = min(e for e in result if result[e] == min(result.values()))
print(min_word)
