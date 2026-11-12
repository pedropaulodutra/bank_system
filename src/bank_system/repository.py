from uuid import UUID

from bank_system.account import Account
from bank_system.exceptions import AccountNotFoundError


class InMemoryAccountRepository:
    def __init__(self) -> None:
        self._accounts: dict[UUID, Account] = {}

    @property
    def accounts(self) -> dict[UUID, Account]:
        return self._accounts

    def save(self, account: Account) -> None:
        self._accounts[account.id] = account

    def get(self, account_id: UUID) -> Account:
        try:
            return self._accounts[account_id]
        except KeyError:
            raise AccountNotFoundError("Account does not exist")
