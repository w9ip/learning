lst = []
for i in range(int(input())):
    lst.append(input())
queries = []
for i in range(int(input())):
    queries.append(input())
counter = 0
for elem in lst:
    for query in queries:
        if query.lower() in elem.lower():
            counter += 1
        if counter == len(queries):
            print(elem)
            counter = 0
    counter = 0
