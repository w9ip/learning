import time


def func1(x: int) -> None:
    print(x ** 2)
    time.sleep(3)
    print('func1 завершена')


def func2(x: int) -> None:
    print(x ** 0.5)
    time.sleep(3)
    print('func2 завершена')


def main():
    func1(4)
    func2(4)


print(time.strftime('%X'))

main()

print(time.strftime('%X'))
