"""Test cases for Coffee class functionality."""
import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def setup_function():
    """Clear orders before each test to ensure clean state."""
    Order._all.clear()

def test_coffee_name_validation():
    """Test that coffee name validation works correctly."""
    # Test name too short (less than 3 characters)
    with pytest.raises(ValueError):
        Coffee("Yo")  
    # Test invalid type (not a string)
    with pytest.raises(TypeError):
        Coffee(123)   

def test_orders_and_customers():
    """Test coffee order tracking and customer relationship methods."""
    # Create customers and coffee
    c1 = Customer("Amy")
    c2 = Customer("Bob")
    latte = Coffee("Latte")
    # Create orders from different customers
    c1.create_order(latte, 5.0)
    c2.create_order(latte, 6.0)

    # Test order count and unique customer list
    assert latte.num_orders() == 2
    assert set([c.name for c in latte.customers()]) == {"Amy", "Bob"}

def test_average_price():
    """Test average price calculation for coffee orders."""
    # Create customer and coffee
    c = Customer("Jane")
    mocha = Coffee("Mocha")
    # Create orders with different prices ($5 + $7 = $12, avg = $6)
    c.create_order(mocha, 5.0)
    c.create_order(mocha, 7.0)

    # Test average calculation
    assert mocha.average_price() == 6.0

def test_average_price_no_orders():
    """Test average price returns 0.0 when no orders exist."""
    cappuccino = Coffee("Cappuccino")
    assert cappuccino.average_price() == 0.0
