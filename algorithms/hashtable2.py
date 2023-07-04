class Entry:
    def __init__(self, k, v):
        self.key = k
        self.value = v


class Hashtable:
    def __init__(self, M=10):
        self.table = [None] * M
        self.M, self.N = M, 0
        

    def get(self, k):
        hc = hash(k) % self.M
        while self.table[hc]:
            if self.table[hc].key == k:
                return self.table[hc].value
            hc = (hc + 1) % self.M
        return None
    
    def put(self, k, v):
        hc = hash(k) % self.M
        while self.table[hc]:
            if self.table[hc].key == k:
                self.table[hc].value = value
                return
            hc = (hc + 1) % self.M
            
        if self.N >= self.M - 1:
            raise RuntimeError('Table is full.')
            
        self.table[hc] = Entry(k, v)
        self.N += 1
    

table = Hashtable(1000)
table.put('Апрель', 30)
table.put('Май', 31)
table.put('Сентябрь', 30)
print(table.get('Август'))  # Промах: должно быть выведено None
print(table.get('Сентябрь'))  # Попадание: должно быть выведено 30
        
