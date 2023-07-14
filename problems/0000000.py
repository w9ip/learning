from sys import stdin

gener = (e.rstrip() for e in stdin.readlines())
next(gener)
res = []
while True:
    try:
        f = next(gener)
        print(f)
        if ('5' in f) or ('4' in f):
            res.append(f)
    except StopIteration:
        print()
        print(*res, sep='\n')
        break
