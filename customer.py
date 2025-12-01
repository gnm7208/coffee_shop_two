from order import Order
class Customer:
    def __init__(self, name: str):
        self.name = name  # triggers setter validation

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        # Validate type
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        # Validate length (1-15 chars)
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        return [o for o in Order.all() if o.customer is self]

    def coffees(self):
        return list({o.coffee for o in self.orders()})

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        totals = {}
        for o in Order.all():
            if o.coffee is coffee:
                totals[o.customer] = totals.get(o.customer, 0) + o.price
        if not totals:
            return None
        return max(totals.items(), key=lambda kv: kv[1])[0]
