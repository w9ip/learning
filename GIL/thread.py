import threading

x = 2


def f(n):
    global x
    x += n
    print(x)


def j(n):
    global x
    x *= n
    print(x)


if __name__ == '__main__':
    t1 = threading.Thread(target=f, args=(2,), daemon=True)
    t2 = threading.Thread(target=j, args=(2,), daemon=True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
