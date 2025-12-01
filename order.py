class Order:
    """Represents an order linking a customer to a coffee with a price."""
    _all = []  # Class variable to store all order instances

    def __init__(self, customer, coffee, price: float):
        """Initialize an Order with customer, coffee, and price (1.0-10.0)."""
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order._all.append(self)  # Add to class registry

    @classmethod
    def all(cls):
        """Return list of all order instances."""
        return list(cls._all)

    @property
    def customer(self):
        """Get the customer for this order."""
        return self._customer

    @customer.setter
    def customer(self, value):
        """Set the customer with validation."""
        from customer import Customer
        if not isinstance(value, Customer):
            raise TypeError("customer must be a Customer instance.")
        self._customer = value

    @property
    def coffee(self):
        """Get the coffee for this order."""
        return self._coffee

    @coffee.setter
    def coffee(self, value):
        """Set the coffee with validation."""
        from coffee import Coffee
        if not isinstance(value, Coffee):
            raise TypeError("coffee must be a Coffee instance.")
        self._coffee = value

    @property
    def price(self):
        """Get the price for this order."""
        return self._price

    @price.setter
    def price(self, value: float):
        """Set the price with validation (must be between 1.0 and 10.0)."""
        if not isinstance(value, (int, float)):
            raise TypeError("price must be a number.")
        value = float(value)
        if not (1.0 <= value <= 10.0):
            raise ValueError("price must be between 1.0 and 10.0")
        self._price = value

    