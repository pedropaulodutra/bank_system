from typing import Protocol
from uuid import UUID

from bank_system.domain.account import Account


class AccountRepository(Protocol):
    def get(self, account_id: UUID) -> Account: ...

    def save(self, account: Account) -> None: ...
