def run_test_func(inp_q, out_q):
    lst = []

    with open('tests.txt', 'r', encoding='UTF8') as tests:
        for string in tests:
            print(repr(string))
            lst += string.split()
    print(lst)
    for i in range(0, len(lst), inp_q + out_q + 1):
        print(
            f'Номер теста: {lst[i]}, Входные данные: {lst[i + 1:i + inp_q + 1]}, Выходные данные: {lst[i + inp_q + 1:i + inp_q + out_q + 1]}'
        )


if __name__ == '__main__':
    run_test_func(1, 1)
