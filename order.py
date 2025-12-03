class Order:
    _all = []
    
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order._all.append(self)
    
    @classmethod
    def all(cls):
        return list(cls._all)