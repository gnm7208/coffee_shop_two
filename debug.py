from customer import Customer
from coffee import Coffee
from order import Order

Order._all.clear()

alice = Customer("Alice")
latte = Coffee("Latte")

# Test order creation
o1 = alice.create_order(latte, 5.0)
assert o1.customer is alice
assert o1.coffee is latte
assert o1.price == 5.0

# Test relationships
assert alice.orders() == [o1]
assert alice.coffees() == [latte]
assert latte.num_orders() == 1
assert latte.average_price() == 5.0

# Test aficionado
bob = Customer("Bob")
bob.create_order(latte, 6.0)
assert Customer.most_aficionado(latte) is bob




