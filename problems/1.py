def repeat(N):
    def wrapper(func):
        for i in range(N):
            try:
                func()
            except Exception as e:
                print(e)

    return wrapper


@repeat(2)
def zero_divide():
    return 1 / 0



