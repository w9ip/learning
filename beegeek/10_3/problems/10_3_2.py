text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'

result = {}

for s in text:
    result[s] = result.get(s, 0) + 1

print(result)