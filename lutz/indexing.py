class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int):
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)

class IndexSetter:
    def __init__(self, data) -> None:
        self.data = data
    def __setitem__(self, index, value):
        self.data[index] = value

class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]
    
x = StepperIndex()
x.data = 'SPAM'

for i in x:
    print(i, end=' ')
