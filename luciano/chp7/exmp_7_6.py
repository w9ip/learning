from functools import reduce
from operator import add

if __name__ == '__main__':
    print(reduce(add, range(100)))
    print(sum(range(100)))
