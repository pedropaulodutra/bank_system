from decimal import Decimal
from uuid import uuid4

import pytest

from bank_system.account import Account
from bank_system.exceptions import (
    DomainError,
    InsufficientFundsError,
    SameAccountTransferError,
    ZeroAmountError,
)
from bank_system.money import Money


def test_new_account_starts_with_zero_balance():
    account = Account("Ana")

    assert account.balance == Money(Decimal("0.00"))


def test_deposit_sums_amount_to_balance():
    account = Account("Ana")

    account.deposit(Money(Decimal("200.00")))

    assert account.balance == Money(Decimal("200.00"))


def test_deposit_zero_raises_error():
    account = Account("Ana")

    with pytest.raises(ZeroAmountError):
        account.deposit(Money(Decimal("0.00")))


def test_withdraw_more_than_balance_raises_error():
    account = Account("Ana")

    account.deposit(Money(Decimal("10.00")))
    with pytest.raises(InsufficientFundsError):
        account.withdraw(Money(Decimal("20.00")))


def test_fail_withdraws_does_not_subtract_value_from_account():
    account = Account("Ana")

    account.deposit(Money(Decimal("20.00")))

    with pytest.raises(InsufficientFundsError):
        account.withdraw(Money(Decimal("30.00")))

    assert account.balance == Money(Decimal("20.00"))


def test_withdraw_subtract_from_account():
    account = Account("Ana")

    account.deposit(Money(Decimal("10.00")))
    account.withdraw(Money(Decimal("7.50")))

    assert account.balance == Money(Decimal("2.50"))


def test_cannot_withdraw_zero():
    account = Account("Ana")

    with pytest.raises(ZeroAmountError):
        account.withdraw(Money(Decimal("0.00")))


def test_deposit_one_cent_to_account():
    account = Account("Ana")

    account.deposit(Money(Decimal("0.01")))

    assert account.balance == Money(Decimal("0.01"))


def test_transfer_moves_money_between_accounts():
    a = Account("Pedro")
    b = Account("Kathleen")

    a.deposit(Money(Decimal("100.00")))

    a.transfer_to(b, Money(Decimal("50.00")))

    assert a.balance == Money(Decimal("50.00"))
    assert b.balance == Money(Decimal("50.00"))


def test_transfer_more_than_account_balance_raises_error():
    a = Account("Pedro")
    b = Account("Kathleen")

    a.deposit(Money(Decimal("100.00")))

    with pytest.raises(InsufficientFundsError):
        a.transfer_to(b, Money(Decimal("150.00")))

    assert a.balance == Money(Decimal("100.00"))
    assert b.balance == Money(Decimal("0.00"))


def test_transfer_to_the_same_account_raises_error():
    a = Account("Pedro")

    a.deposit(Money(Decimal("100.00")))

    with pytest.raises(SameAccountTransferError):
        a.transfer_to(a, Money(Decimal("50.00")))


def test_insufficient_funds_error_is_also_captured_by_domain_error():
    a = Account("Pedro")
    b = Account("Kathleen")

    with pytest.raises(DomainError):
        a.transfer_to(b, Money(Decimal("10.00")))


def test_two_accounts_have_different_ids():
    a = Account("Pedro")
    b = Account("Pedro")

    assert a.id != b.id


def test_account_created_with_id_mantain_id():
    id = uuid4()
    a = Account("Pedro", id)

    assert a.id == id


def test_account_id_cannot_be_changed():
    a = Account("Pedro")
    id = uuid4()

    with pytest.raises(AttributeError):
        a.id = id


def test_account_is_the_same_when_id_is_provided():
    a = Account("Pedro")
    b = Account("Pedro", a.id)

    assert a == b


def test_set_eliminate_the_same_account():
    a = Account("Pedro")
    b = Account("Pedro", a.id)

    accounts = {a, b}

    assert len(accounts) == 1


def test_transfer_to_another_object_with_same_id():
    a = Account("Pedro")

    a.deposit(Money(Decimal("20.00")))

    with pytest.raises(SameAccountTransferError):
        a.transfer_to(Account("Pedro", a.id), Money(Decimal("10.00")))
