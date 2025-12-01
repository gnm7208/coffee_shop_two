class Order:
    _all = []

    def __init__(self, customer, coffee, price: float):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order._all.append(self)

    @classmethod
    def all(cls):
        return list(cls._all)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, value):
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("customer must be a Customer instance.")
        self._customer = value

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        self._coffee = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)):
            raise TypeError("price must be a number.")
        value = float(value)
        if not (1.0 <= value <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")
        self._price = value

    