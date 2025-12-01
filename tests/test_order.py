import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    """Clear order registry before each test to ensure clean state"""
    Order._all.clear()

def test_order_validation():
    """Test that Order constructor validates input parameters correctly"""
    c = Customer("Zed")
    cof = Coffee("Mocha")

    # Test customer parameter validation - must be Customer instance
    with pytest.raises(TypeError):
        Order("Zed", cof, 5.0)   # invalid customer
    
    # Test coffee parameter validation - must be Coffee instance
    with pytest.raises(TypeError):
        Order(c, "Mocha", 5.0)   # invalid coffee
    
    # Test price type validation - must be numeric
    with pytest.raises(TypeError):
        Order(c, cof, "cheap")   # invalid price type
    
    # Test price range validation - must be between 1.0 and 10.0
    with pytest.raises(ValueError):
        Order(c, cof, 0.5)       # too low
    with pytest.raises(ValueError):
        Order(c, cof, 10.5)      # too high

def test_order_registry_and_properties():
    """Test that orders are properly registered and properties are accessible"""
    c = Customer("Zed")
    cof = Coffee("Mocha")
    o1 = Order(c, cof, 5.0)
    o2 = Order(c, cof, 6.0)

    # Verify orders are added to class registry
    assert len(Order.all()) == 2
    
    # Verify order properties are correctly set
    assert o1.customer is c
    assert o1.coffee is cof
    assert o1.price == 5.0
