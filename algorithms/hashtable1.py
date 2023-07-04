class Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        
class Hashtable:
    def __init__(self, M=10):
        self.table = [None] * M  # Заводим массив на М объектов.
        self.M = M
        
    def get(self, k):
        """
        Определяет номер ячейки по ключу k, для которого вычисляется хеш, 
        и возвращает значение, если оно есть.
        """
        hc = hash(k) % self.M
        return self.table[hc].value if self.table[hc] else None
    
    def put(self, k, v):
        """
        Определяет номер ячейки по ключу, для которого вычисляется хеш,
        и перезаписывает хранящееся там значение - или записывает новое,
        если ячейка была пуста.
        """
        hc = hash(k) % self.M
        entry = self.table[hc]
        if entry:
            if entry.key == k:
                entry.value = v
            else:
                """
                Если хеш двух различных ключей приводит к одной и той же ячейке,
                то это коллизия, происходит исключение.
                """
                raise RuntimeError(f'Key Collision: {k} and {entry.key}')
        else:
            self.table[hc] = Entry(k, v)

table = Hashtable(1000)
table.put('Апрель', 30)
table.put('Май', 31)
table.put('Сентябрь', 30)
print(table.get('Август'))  # Промах: должно быть выведено None
print(table.get('Сентябрь'))  # Попадание: должно быть выведено 30
        