lst = []
negatives = []
zeros = []
positives = []
for i in range(int(input())):
    lst.append(int(input()))
for element in lst:
    if element < 0:
        negatives.append(element)
    elif element == 0:
        zeros.append(element)
    elif element > 0:
        positives.append(element)
print(*negatives, *zeros, *positives, sep='\n')