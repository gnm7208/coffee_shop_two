from customer import Customer

# Valid
c = Customer("Alice")
print(c.name)   

# Invalid
try:
    Customer("")  
except ValueError as e:
    print("Caught:", e)

try:
    Customer("ThisNameIsWayTooLong")
except ValueError as e:
    print("Caught:", e)
