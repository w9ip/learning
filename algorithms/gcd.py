def gcd(p: int, q: int):
    if q == 0: return p
    r = p % q
    return gcd(q, r)

if __name__ == '__main__':
    print(gcd(36, 64))  # 4
    print(gcd(231, 546))  # 21
