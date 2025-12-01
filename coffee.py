from order import Order

class Coffee:
    """Represents a coffee item with a name."""

    def __init__(self, name: str):
        """Initialize a Coffee instance with a name (minimum 3 characters)."""
        self.name = name

    @property
    def name(self) -> str:
        """Get the coffee name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the coffee name with validation."""
        # Validate type
        if not isinstance(value, str):
            raise TypeError("Coffee name must be a string.")
        # Validate minimum length (3+ chars)
        if len(value) < 3:
            raise ValueError("Coffee name must be at least 3 characters.")
        self._name = value
     
    def orders(self):
        """Return all orders for this coffee."""
        return [o for o in Order.all() if o.coffee is self]

    def customers(self):
        """Return unique list of customers who ordered this coffee."""
        return list({o.customer for o in self.orders()})

    def num_orders(self):
        """Return total number of orders for this coffee."""
        return len(self.orders())

    def average_price(self):
        """Return average price of all orders for this coffee."""
        orders = self.orders()
        if not orders:
            return 0.0
        return sum(o.price for o in orders) / len(orders)