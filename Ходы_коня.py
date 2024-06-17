cols = 'abcdefgh'
pos = input()


for i in range(8, 0, -1):
    for j in range(8):
        if cols[j]+(str(i)) == pos:
            print('N', end=' ')
        elif abs((i-int(pos[-1])) * ((j+1)-(cols.index(pos[0])+1))) == 2:
          print('*', end=' ')
        else:
          print('.', end=' ')
    print()