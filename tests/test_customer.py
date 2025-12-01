import pytest
from customer import Customer
from coffee import Coffee
from order import Order

def setup_function():
    # Clear orders before each test
    Order._all.clear()

def test_customer_name_validation():
    with pytest.raises(ValueError):
        Customer("")  # too short
    with pytest.raises(ValueError):
        Customer("x" * 16)  # too long
    with pytest.raises(TypeError):
        Customer(123)  # not a string

def test_customer_orders_and_coffees():
    c = Customer("Alice")
    latte = Coffee("Latte")
    espresso = Coffee("Espresso")
    c.create_order(latte, 5.0)
    c.create_order(espresso, 3.5)

    assert len(c.orders()) == 2
    assert set([cof.name for cof in c.coffees()]) == {"Latte", "Espresso"}

def test_most_aficionado():
    a = Customer("Ann")
    b = Customer("Ben")
    latte = Coffee("Latte")
    a.create_order(latte, 5.0)
    b.create_order(latte, 6.0)
    b.create_order(latte, 4.0)

    assert Customer.most_aficionado(latte) is b
