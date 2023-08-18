# Использование partial позволяет вызывать функцию с двумя аргументами там,
# где требуется вызываемый объект с одним аргументом
from operator import mul
from functools import partial

triple = partial(mul, 3)
print(triple(7))

print(list(map(triple, range(1, 10))))