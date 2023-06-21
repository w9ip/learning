class Number:
    def __init__(self, start) -> None:
        self.data = start
    def __sub__(self, other):
        return Number(self.data - other)
    
