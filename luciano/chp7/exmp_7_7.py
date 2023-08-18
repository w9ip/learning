from exmp_7_4 import fruits

if __name__ == '__main__':
    print(sorted(fruits, key=lambda word: word[::-1]))