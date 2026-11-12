from decimal import Decimal
from uuid import UUID

from bank_system.application.account_repository import AccountRepository
from bank_system.domain.money import Money


class TransferMoney:
    def __init__(self, accounts: AccountRepository) -> None:
        self._accounts = accounts

    def execute(self, source_id: UUID, destination_id: UUID, amount: Decimal) -> None:
        source_account = self._accounts.get(source_id)
        destination_account = self._accounts.get(destination_id)

        source_account.transfer_to(destination_account, Money(amount))

        self._accounts.save(source_account)
        self._accounts.save(destination_account)
