text = input().split()
result = [[text[0]]]
for i in range(1, len(text)):
    if text[i] in result[-1]:
        result[-1].append(text[i])
    else:
        result.append([text[i]])
print(result)
