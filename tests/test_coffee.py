import pytest
from coffee import Coffee
from customer import Customer
from order import Order

def setup_function():
    Order._all.clear()

def test_coffee_name_validation():
    with pytest.raises(ValueError):
        Coffee("Yo")
    with pytest.raises(TypeError):
        Coffee(123)

def test_orders_and_customers():
    c1 = Customer("Amy")
    c2 = Customer("Bob")
    latte = Coffee("Latte")
    c1.create_order(latte, 5.0)
    c2.create_order(latte, 6.0)

    assert latte.num_orders() == 2
    assert set([c.name for c in latte.customers()]) == {"Amy", "Bob"}

def test_average_price():
    c = Customer("Jane")
    mocha = Coffee("Mocha")
    c.create_order(mocha, 5.0)
    c.create_order(mocha, 7.0)

    assert mocha.average_price() == 6.0

def test_average_price_no_orders():
    cappuccino = Coffee("Cappuccino")
    assert cappuccino.average_price() == 0.0