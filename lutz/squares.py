class Squares:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.value = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value == self.stop - 1:
            raise StopIteration
        self.value += 1
        return self.value

if __name__ == '__main__':
    for i in Squares(1, 5):
        print(i)