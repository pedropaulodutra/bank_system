from decimal import Decimal

import pytest

from bank_system.money import Money


def test_create_money():
    money = Money(Decimal("10.00"))

    assert money.amount == Decimal("10.00")


def test_create_money_with_no_value():
    money = Money(Decimal("0.00"))

    assert money.amount == Decimal("0.00")


def test_create_money_with_three_places_is_accept_when_the_third_place_is_zero():
    money = Money(Decimal("0.010"))

    assert money.amount == Decimal("0.01")


def test_cannot_create_negative_money():
    with pytest.raises(ValueError, match="Amount cannot be negative"):
        Money(Decimal("-10.00"))


def test_create_money_with_three_places_raises_value_error():
    with pytest.raises(ValueError, match="Amount must have at most two decimal places"):
        Money(Decimal("10.001"))


def test_create_money_with_float_type_raises_type_error():
    with pytest.raises(TypeError, match="Amount must be Decimal type"):
        Money(10.00)


def test_change_money_value_after_create_raises_attribute_error():
    money = Money(Decimal("10.00"))
    with pytest.raises(AttributeError):
        money.amount = Decimal("-500.00")


def test_moneys_with_same_values_are_equal():
    money_1 = Money(Decimal("10.00"))
    money_2 = Money(Decimal("10.00"))

    assert money_1 == money_2


def test_moneys_with_different_values_are_not_equal():
    money_1 = Money(Decimal("10.00"))
    money_2 = Money(Decimal("20.00"))

    assert money_1 != money_2


def test_sum_one_cent_with_two_cents_return_three_cents():
    money_1 = Money(Decimal("0.01"))
    money_2 = Money(Decimal("0.02"))

    assert money_1 + money_2 == Money(Decimal("0.03"))


def test_subtract_values():
    money = Money(Decimal("10.00"))

    assert money - Money(Decimal("5.00")) == Money(Decimal("5.00"))


def test_money_cannot_be_negative():
    money = Money(Decimal("2.00"))

    with pytest.raises(ValueError, match="Amount cannot be negative"):
        money_2 = money - Money(Decimal("3.00"))


def test_two_is_bigger_than_one():
    money = Money(Decimal("2.00"))

    assert money > Money(Decimal("1.00"))
