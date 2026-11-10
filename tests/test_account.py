from decimal import Decimal

import pytest

from bank_system.account import Account
from bank_system.money import Money


def test_new_account_starts_with_zero_balance():
    account = Account("Ana")

    assert account.balance == Money(Decimal("0.00"))


def test_deposit_sums_amount_to_balance():
    account = Account("Ana")

    account.deposit(Money(Decimal("200.00")))

    assert account.balance == Money(Decimal("200.00"))


def test_deposit_zero_raises_value_error():
    account = Account("Ana")

    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        account.deposit(Money(Decimal("0.00")))


def test_withdraw_more_than_balance_raises_value_error():
    account = Account("Ana")

    account.deposit(Money(Decimal("10.00")))
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(Money(Decimal("20.00")))


def test_fail_withdraws_does_not_subtract_value_from_account():
    account = Account("Ana")

    account.deposit(Money(Decimal("20.00")))

    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(Money(Decimal("30.00")))

    assert account.balance == Money(Decimal("20.00"))
