# Coffee Shop Domain Model

A Python application modeling a Coffee Shop domain using object-oriented programming principles.

## Overview

This project implements a domain model for a Coffee Shop with three main entities:
- **Customer**: Represents customers who place orders
- **Coffee**: Represents coffee items available for order  
- **Order**: Represents individual orders linking customers and coffees

## Relationships

- A Customer can place many Orders
- A Coffee can have many Orders
- An Order belongs to one Customer and one Coffee
- Customer and Coffee have a many-to-many relationship through Order

## Project Structure

```
coffee_shop_two/
├── customer.py     # Customer class implementation
├── coffee.py       # Coffee class implementation
├── order.py        # Order class implementation
├── debug.py        # Testing and debugging script
└── README.md       # This file
```

## Classes

### Customer (`customer.py`)
- **Attributes**: `name` (string, 1-15 characters)
- **Methods**:
  - `orders()`: Returns list of all orders for this customer
  - `coffees()`: Returns unique list of coffees ordered by this customer
  - `create_order(coffee, price)`: Creates new order for this customer
  - `most_aficionado(coffee)`: Class method returning customer who spent most on given coffee

### Coffee (`coffee.py`)
- **Attributes**: `name` (string, minimum 3 characters)
- **Methods**:
  - `orders()`: Returns list of all orders for this coffee
  - `customers()`: Returns unique list of customers who ordered this coffee
  - `num_orders()`: Returns total number of orders for this coffee
  - `average_price()`: Returns average price of orders for this coffee

### Order (`order.py`)
- **Attributes**: 
  - `customer`: Customer instance
  - `coffee`: Coffee instance
  - `price`: Float between 1.0 and 10.0
- **Methods**:
  - `all()`: Class method returning all order instances

## Validation

All classes include input validation:
- Customer names must be strings between 1-15 characters
- Coffee names must be strings with minimum 3 characters
- Order prices must be floats between 1.0 and 10.0
- Invalid inputs raise appropriate TypeError or ValueError exceptions

## Usage Example

```python
from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
alice = Customer("Alice")
latte = Coffee("Latte")

# Create order
order = alice.create_order(latte, 5.0)

# Access relationships
print(alice.orders())        # [order]
print(alice.coffees())       # [latte]
print(latte.customers())     # [alice]
print(latte.num_orders())    # 1
print(latte.average_price()) # 5.0
```

## Testing

Run the debug script to test functionality:
```bash
python debug.py
```

## Features

- Object-oriented design with proper encapsulation
- Input validation with custom exceptions
- Relationship management between entities
- Aggregate methods for data analysis
- Class methods for advanced queries