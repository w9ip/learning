# Класс Sentence реализованный с помощью паттерна Итератор


import re
import reprlib

RE_WORD = re.compile(r'\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f"Sentence({[reprlib.repr(self.text)]})"

    def __iter__(self):
        """
        Метод __iter__ – единственное дополнение к предыдущей реализации Sentence.
        В этой версии нет метода __getitem__, тем самым мы хотим доказать, что класс является итерируемым,
        потому что реализует __iter__.

        __iter__ выполняет требования протокола итерируемого объекта – создает и возвращает итератор.
        """
        return SentenceIterator(self.words)


class SentenceIterator:

    def __init__(self, words):
        self.words = words  # SentenceIterator хранит ссылку на список слов.
        self.index = 0  # self.index используется для определения следующего слова.

    def __next__(self):
        try:
            word = self.words[self.index]  # Получить слово с индексом self.index.
        except IndexError:
            raise StopIteration()  # Если слова с индексом self.index не существует, возбудить исключение StopIteration.
        self.index += 1  # Увеличить self.index.
        return word  # Вернуть слово.

    def __iter__(self):
        return self  # Реализовать метод self.__iter__.
