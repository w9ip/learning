from itertools import permutations

s = 'ТОДЕЛ'
perm_set = permutations(s)
for val in perm_set:
    print(''.join(val))
