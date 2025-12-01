from order import Order

class Customer:
    """Represents a customer who can place orders for coffee."""
    
    def __init__(self, name: str):
        """Initialize a Customer with a name (1-15 characters)."""
        self.name = name  # triggers setter validation

    @property
    def name(self) -> str:
        """Get the customer's name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """Set the customer's name with validation."""
        # Validate type
        if not isinstance(value, str):
            raise TypeError("Customer name must be a string.")
        # Validate length (1-15 chars)
        if not (1 <= len(value) <= 15):
            raise ValueError("Customer name must be between 1 and 15 characters.")
        self._name = value

    def orders(self):
        """Return all orders placed by this customer."""
        return [o for o in Order.all() if o.customer is self]

    def coffees(self):
        """Return unique list of coffees ordered by this customer."""
        return list({o.coffee for o in self.orders()})

    def create_order(self, coffee, price):
        """Create a new order for this customer with given coffee and price."""
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        """Return the customer who spent the most on the given coffee."""
        totals = {}
        # Calculate total spending per customer for this coffee
        for o in Order.all():
            if o.coffee is coffee:
                totals[o.customer] = totals.get(o.customer, 0) + o.price
        # Return None if no customers found
        if not totals:
            return None
        # Return customer with highest total spending
        return max(totals.items(), key=lambda kv: kv[1])[0]
