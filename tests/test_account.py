from decimal import Decimal

import pytest

from bank_system.account import Account


def test_new_account_starts_with_zero_balance():
    account = Account("Ana")

    assert account.balance == Decimal("0.00")


def test_cannot_deposit_negative_amount():
    account = Account("Ana")

    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(Decimal("-10.00"))


def test_deposit_sums_amount_to_balance():
    account = Account("Ana")

    account.deposit(Decimal("200.00"))

    assert account.balance == Decimal("200.00")


def test_deposit_one_cent_to_account():
    account = Account("Ana")

    account.deposit(Decimal("0.01"))

    assert account.balance == Decimal("0.01")


def test_deposit_zero_raises_value_error():
    account = Account("Ana")

    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(Decimal("0.00"))


def test_withdraw_subtract_value_from_balance():
    account = Account("Ana")

    account.deposit(Decimal("100.00"))
    account.withdraw(Decimal("75.00"))

    assert account.balance == Decimal("25.00")


def test_withdraw_more_than_balance_raises_value_error():
    account = Account("Ana")

    account.deposit(Decimal("10.00"))
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(Decimal("20.00"))


def test_withdraw_negative_amount_raises_value_error():
    account = Account("Ana")

    with pytest.raises(ValueError, match="Withdraw amount isn't valid"):
        account.withdraw(Decimal("-10.00"))


def test_deposit_ten_cents_then_twenty_cents_does_not_break_balance():
    account = Account("Ana")

    account.deposit(Decimal("0.10"))
    account.deposit(Decimal("0.20"))

    assert account.balance == Decimal("0.30")


def test_fail_withdraws_dont_subtract_value_from_account():
    account = Account("Ana")

    account.deposit(Decimal("20.00"))

    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(Decimal("30.00"))

    assert account.balance == Decimal("20.00")


def test_cannot_deposit_values_with_more_then_two_decimal_places():
    account = Account("Ana")

    with pytest.raises(
        ValueError, match="Deposit amount must have at most two decimal places"
    ):
        account.deposit(Decimal("10.001"))
