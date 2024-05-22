from math import tan, pi
n, a = float(input()), float(input())

S = (n*a**2)/(4 * tan(pi/n))
print(S)

