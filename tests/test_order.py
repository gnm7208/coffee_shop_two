import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    Order._all.clear()

def test_order_validation():
    c = Customer("Zed")
    cof = Coffee("Mocha")

    with pytest.raises(TypeError):
        Order("Zed", cof, 5.0)
    with pytest.raises(TypeError):
        Order(c, "Mocha", 5.0)
    with pytest.raises(TypeError):
        Order(c, cof, "cheap")
    with pytest.raises(ValueError):
        Order(c, cof, 0.5)
    with pytest.raises(ValueError):
        Order(c, cof, 10.5)

def test_order_registry_and_properties():
    c = Customer("Zed")
    cof = Coffee("Mocha")
    o1 = Order(c, cof, 5.0)
    o2 = Order(c, cof, 6.0)

    assert len(Order.all()) == 2
    assert o1.customer is c
    assert o1.coffee is cof
    assert o1.price == 5.0