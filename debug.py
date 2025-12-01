from customer import Customer
from coffee import Coffee
from order import Order

# Valid customer creation
alice = Customer("Alice")
# print(c.name)   

# Test customer validation
# try:
#     Customer("")  
# except ValueError as e:
#     print("Caught:", e)

# try:
#     Customer("ThisNameIsWayTooLong")
# except ValueError as e:
#     print("Caught:", e)

# Valid coffee creation
latte = Coffee("Latte")
bob = Customer("Bob")
espresso = Coffee("Espresso")
# print(latte.name)  

# Test coffee validation
# try:
#     Coffee("Yo")   
# except ValueError as e:
#     print("Caught:", e)

# Valid order creation
alice.create_order(espresso, 3.5)
bob.create_order(latte, 6.0)

print("Alice orders:", alice.orders())          
print("Alice coffees:", [c.name for c in alice.coffees()])  
print("Latte customers:", [c.name for c in latte.customers()])  
print("Latte num_orders:", latte.num_orders())  
print("Latte avg price:", latte.average_price()) 

aficionado = Customer.most_aficionado(latte)
print("Most aficionado for Latte:", aficionado.name)  



