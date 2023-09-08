from sys import stdin

(
    n,  # море
    m,  # деревня
    k,  # горы
    x,  # деревня + море
    y,  # деревня + горы
    z,  # писали ДВИ
) = map(int, stdin.readlines())
# кол-во учеников в школе
print(
    n + m - x + k - y + z
)
