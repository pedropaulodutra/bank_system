from decimal import Decimal
from uuid import uuid4

import pytest

from bank_system.application.transfer_money import TransferMoney
from bank_system.domain.account import Account
from bank_system.domain.exceptions import AccountNotFoundError, InsufficientFundsError
from bank_system.domain.money import Money
from bank_system.infrastructure.repository import InMemoryAccountRepository


def test_transfer_money_subtract_from_one_and_add_in_another_one():
    repo = InMemoryAccountRepository()

    account = Account("Pedro")
    second_account = Account("Kathleen")

    account.deposit(Money(Decimal("10.00")))

    repo.save(account)
    repo.save(second_account)

    transfer = TransferMoney(repo)

    transfer.execute(account.id, second_account.id, Decimal("7.00"))

    assert repo.get(account.id).balance == Money(Decimal("3.00"))
    assert repo.get(second_account.id).balance == Money(Decimal("7.00"))


def test_non_exists_accounts_raise_error():
    repo = InMemoryAccountRepository()
    transfer = TransferMoney(repo)

    with pytest.raises(AccountNotFoundError):
        transfer.execute(uuid4(), uuid4(), Decimal("7.00"))


def test_transfer_more_than_balance_raises_error():
    repo = InMemoryAccountRepository()

    account = Account("Pedro")
    second_account = Account("Kathleen")

    account.deposit(Money(Decimal("10.00")))

    repo.save(account)
    repo.save(second_account)

    transfer = TransferMoney(repo)

    with pytest.raises(InsufficientFundsError):
        transfer.execute(account.id, second_account.id, Decimal("12.00"))

    assert repo.get(account.id).balance == Money(Decimal("10.00"))
    assert repo.get(second_account.id).balance == Money(Decimal("0.00"))
