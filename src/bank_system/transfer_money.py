from decimal import Decimal
from uuid import UUID

from bank_system.money import Money
from bank_system.repository import InMemoryAccountRepository


class TransferMoney:
    def __init__(self, accounts: InMemoryAccountRepository) -> None:
        self._accounts = accounts

    def execute(self, source_id: UUID, destination_id: UUID, amount: Decimal) -> None:
        source_account = self._accounts.get(source_id)
        destination_account = self._accounts.get(destination_id)

        source_account.transfer_to(destination_account, Money(amount))
