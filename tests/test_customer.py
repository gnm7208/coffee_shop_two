"""Test cases for Customer class functionality."""
import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    """Clear orders before each test to ensure clean state."""
    Order._all.clear()

def test_customer_name_validation():
    """Test that customer name validation works correctly."""
    # Test name too short (empty string)
    with pytest.raises(ValueError):
        Customer("")  
    # Test name too long (over 15 characters)
    with pytest.raises(ValueError):
        Customer("x" * 16)  
    # Test invalid type (not a string)
    with pytest.raises(TypeError):
        Customer(123)  

def test_customer_orders_and_coffees():
    """Test customer order creation and coffee relationship methods."""
    c = Customer("Alice")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    # Create orders for different coffees
    c.create_order(latte, 5.0)
    c.create_order(espresso, 3.5)

    # Verify order count and unique coffee list
    assert len(c.orders()) == 2
    assert set([cof.name for cof in c.coffees()]) == {"Latte", "Espresso"}

def test_most_aficionado():
    """Test that most_aficionado returns customer who spent most on a coffee."""
    a = Customer("Ann")
    b = Customer("Ben")
    latte = Coffee("Latte")
    # Ann spends $5, Ben spends $10 total ($6 + $4)
    a.create_order(latte, 5.0)
    b.create_order(latte, 6.0)
    b.create_order(latte, 4.0)

    # Ben should be the biggest spender
    assert Customer.most_aficionado(latte) is b
