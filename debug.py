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
# print(latte.name)  

# Test coffee validation
# try:
#     Coffee("Yo")   
# except ValueError as e:
#     print("Caught:", e)

# Valid order creation
o1 = Order(alice, latte, 5.0)
print(o1.customer.name)   
print(o1.coffee.name)     
print(o1.price)          

# Test order price validation
try:
    Order(alice, latte, 0.5) 
except ValueError as e:
    print("Caught:", e)


