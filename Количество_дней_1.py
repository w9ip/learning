def get_days(n):
    if n == 2:
        return 28
    elif n == 1 or n == 3 or n == 5 or n == 7 or n == 8 or n == 10 or n == 12:
        return 31
    else:
        return 30
