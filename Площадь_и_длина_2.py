from math import pi


def get_circle(R):
    S = pi * R ** 2
    C = 2 * pi * R
    return C, S

print(get_circle(1))
print(get_circle(1.5))