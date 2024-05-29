lst = []
for i in range(int(input())):
    lst.append(input())
query = input()
for elem in lst:
    if query.lower() in elem.lower():
        print(elem)
