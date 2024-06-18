def chunked(s, n):
    result = []
    for i in range(0, len(s), n):
        result.append(s[i:n + i])
    return result


s, n = input().split(), int(input())
print(chunked(s, n))
