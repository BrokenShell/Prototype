from Fortuna import smart_clamp


class Resource:

    def __init__(self, amount: int):
        self.current = amount
        self.total = amount

    def __str__(self):
        return f"{self.current}/{self.total}"

    def sub(self, amount):
        self.current = smart_clamp(0, self.total, self.current - amount)

    def add(self, amount):
        self.current = smart_clamp(0, self.total,  self.current + amount)

    def __bool__(self):
        return self.current > 0
