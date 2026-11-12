from uuid import uuid4

import pytest

from bank_system.account import Account
from bank_system.exceptions import AccountNotFoundError
from bank_system.repository import InMemoryAccountRepository


def test_getting_a_count_in_memory():
    bd = InMemoryAccountRepository()
    account = Account("Pedro")

    bd.save(account)

    assert bd.get(account.id) == account


def test_unknowing_id_raises_error():
    bd = InMemoryAccountRepository()
    account = Account("Pedro")

    bd.save(account)

    with pytest.raises(AccountNotFoundError):
        bd.get(uuid4())
