from Fortuna import smart_clamp


class Resource:
    """ Point total that can go up and down based on combat """

    def __init__(self, amount: int):
        self.current = amount
        self.total = amount

    def __str__(self):
        return f"{self.current}/{self.total}"

    def sub(self, amount):
        self.current -= smart_clamp(0, self.current, amount)

    def add(self, amount):
        # Todo: FIX IT
        self.current += smart_clamp(0, self.current, amount)


r = Resource(10)
r.add(1)
print(r)
