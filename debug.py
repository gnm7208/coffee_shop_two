"""Debug script to test Coffee Shop domain model functionality."""
from customer import Customer
from coffee import Coffee
from order import Order

# Clear any existing orders for clean testing
Order._all.clear()

# Create test instances
alice = Customer("Alice")
latte = Coffee("Latte")

# Test order creation and properties
o1 = alice.create_order(latte, 5.0)
assert o1.customer is alice
assert o1.coffee is latte
assert o1.price == 5.0

# Test relationship methods
assert alice.orders() == [o1]
assert alice.coffees() == [latte]
assert latte.num_orders() == 1
assert latte.average_price() == 5.0

# Test most_aficionado class method
bob = Customer("Bob")
bob.create_order(latte, 6.0)  # Bob spends more
assert Customer.most_aficionado(latte) is bob

print("All tests passed! Coffee Shop domain model is working correctly.")




