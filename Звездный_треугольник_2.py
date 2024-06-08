def draw_triangle():
    total = 1
    for i in range(1, 9):
        print(' ' * (8 - i) + '*' * total)
        total += 2


draw_triangle()
