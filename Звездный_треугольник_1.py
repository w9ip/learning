def draw_triangle(fill, base):
    for i in range(1, (base // 2) + 1):
        print(i * fill)
    for i in range((base // 2) + 1, -1, -1):
        print(i * fill)


draw_triangle(input(), int(input()))
