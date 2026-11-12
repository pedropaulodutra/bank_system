from decimal import Decimal
from uuid import uuid4

import pytest

from bank_system.account import Account
from bank_system.exceptions import AccountNotFoundError, InsufficientFundsError
from bank_system.money import Money
from bank_system.repository import InMemoryAccountRepository
from bank_system.transfer_money import TransferMoney


def test_transfer_money_subtract_from_one_and_add_in_another_one():
    bd = InMemoryAccountRepository()

    account = Account("Pedro")
    second_account = Account("Kathleen")

    account.deposit(Money(Decimal("10.00")))

    bd.save(account)
    bd.save(second_account)

    use_case = TransferMoney(bd)

    use_case.execute(account.id, second_account.id, Decimal("7.00"))

    assert account.balance == Money(Decimal("3.00"))
    assert second_account.balance == Money(Decimal("7.00"))


def test_non_exists_accounts_raise_error():
    bd = InMemoryAccountRepository()
    use_case = TransferMoney(bd)

    with pytest.raises(AccountNotFoundError):
        use_case.execute(uuid4(), uuid4(), Decimal("7.00"))


def transfer_more_than_balance_raises_error():
    bd = InMemoryAccountRepository()

    account = Account("Pedro")
    second_account = Account("Kathleen")

    account.deposit(Money(Decimal("10.00")))

    bd.save(account)
    bd.save(second_account)

    use_case = TransferMoney(bd)

    with pytest.raises(InsufficientFundsError):
        use_case.execute(account.id, second_account.id, Decimal("12.00"))

    assert account.balance == Money(Decimal("10.00"))
    assert second_account.balance == Money(Decimal("0.00"))
