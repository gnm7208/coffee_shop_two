from customer import Customer
from coffee import Coffee

# # Valid
# c = Customer("Alice")
# print(c.name)   

# # Invalid
# try:
#     Customer("")  
# except ValueError as e:
#     print("Caught:", e)

# try:
#     Customer("ThisNameIsWayTooLong")
# except ValueError as e:
#     print("Caught:", e)

latte = Coffee("Latte")
print(latte.name)  

try:
    Coffee("Yo")   
except ValueError as e:
    print("Caught:", e)


