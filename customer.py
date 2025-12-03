class Customer:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value
    
    def orders(self):
        from order import Order
        return [o for o in Order.all() if o.customer is self]
    
    def coffees(self):
        return list({o.coffee for o in self.orders()})
    
    def create_order(self, coffee, price):
        from order import Order
        return Order(self, coffee, price)
    
    @classmethod
    def most_aficionado(cls, coffee):
        from order import Order
        totals = {}
        for o in Order.all():
            if o.coffee is coffee:
                totals[o.customer] = totals.get(o.customer, 0) + o.price
        if not totals:
            return None
        return max(totals.items(), key=lambda kv: kv[1])[0]