import pytest
from pizza_order import pizza_price, order_discount, delivery_status


# Pizza price: size and topping branches

def test_valid_pizza_sizes():
    assert pizza_price("small", 0, False) == 200
    assert pizza_price("medium", 0, False) == 350
    assert pizza_price("large", 0, False) == 500


def test_invalid_size():
    with pytest.raises(ValueError):
        pizza_price("extra-large", 0, False)


def test_negative_toppings():
    with pytest.raises(ValueError):
        pizza_price("medium", -1, False)


def test_three_or_fewer_toppings():
    assert pizza_price("medium", 3, False) == 470


def test_more_than_three_toppings():
    assert pizza_price("large", 5, False) == 680


# Cheese burst: both branches

def test_cheese_burst_available():
    assert pizza_price("medium", 1, True) == 490


def test_cheese_burst_unavailable():
    with pytest.raises(ValueError):
        pizza_price("small", 1, True)


# Order discount: all decision branches

def test_order_below_300():
    assert order_discount(250, "monday", False) == 0


def test_tuesday_discount():
    assert order_discount(500, "tuesday", False) == 250


def test_weekend_discount():
    assert order_discount(500, "saturday", False) == 0
    assert order_discount(500, "sunday", False) == 0


def test_regular_day_discount():
    assert order_discount(500, "monday", False) == 50


def test_student_discount():
    assert order_discount(500, "monday", True) == 100


def test_tuesday_student_discount():
    assert order_discount(500, "tuesday", True) == 300


# Delivery status: all decision branches

def test_distance_not_deliverable():
    assert delivery_status(20, 12) == "not deliverable"


def test_delivery_on_time():
    assert delivery_status(30, 5) == "on time"


def test_delivery_late():
    assert delivery_status(40, 5) == "late"


def test_delivery_free_pizza():
    assert delivery_status(50, 5) == "free pizza"
