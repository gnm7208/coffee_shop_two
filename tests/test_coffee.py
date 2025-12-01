import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def setup_function():
    # Clear orders before each test
    Order._all.clear()

def test_coffee_name_validation():
    # Test name too short
    with pytest.raises(ValueError):
        Coffee("Yo")  # too short
    # Test invalid type
    with pytest.raises(TypeError):
        Coffee(123)   # not a string

def test_orders_and_customers():
    # Create customers and coffee
    c1 = Customer("Amy")
    c2 = Customer("Bob")
    latte = Coffee("Latte")
    # Create orders
    c1.create_order(latte, 5.0)
    c2.create_order(latte, 6.0)

    # Test order count and customer list
    assert latte.num_orders() == 2
    assert set([c.name for c in latte.customers()]) == {"Amy", "Bob"}

def test_average_price():
    # Create customer and coffee
    c = Customer("Jane")
    mocha = Coffee("Mocha")
    # Create orders with different prices
    c.create_order(mocha, 5.0)
    c.create_order(mocha, 7.0)

    # Test average calculation
    assert mocha.average_price() == 6.0

def test_average_price_no_orders():
    # Test average price with no orders
    cappuccino = Coffee("Cappuccino")
    assert cappuccino.average_price() == 0.0
