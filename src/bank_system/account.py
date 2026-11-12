from decimal import Decimal
from uuid import UUID, uuid4

from bank_system.exceptions import (
    InsufficientFundsError,
    SameAccountTransferError,
    ZeroAmountError,
)
from bank_system.money import Money


class Account:
    def __init__(self, owner: str, id: UUID | None = None) -> None:
        self.owner = owner
        self._balance = Money(Decimal("0.00"))
        if id is not None:
            self._id = id
        else:
            self._id = uuid4()

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def balance(self) -> Money:
        return self._balance

    def deposit(self, amount: Money) -> None:
        if amount < Money(Decimal("0.01")):
            raise ZeroAmountError("Amount must be greater than zero")
        self._balance += amount

    def withdraw(self, amount: Money) -> None:
        if amount < Money(Decimal("0.01")):
            raise ZeroAmountError("Amount must be greater than zero")
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds")

        self._balance -= amount

    def transfer_to(self, destination: Account, amount: Money) -> None:
        if destination == self:
            raise SameAccountTransferError("Cannot transfer to the same account")

        self.withdraw(amount)
        destination.deposit(amount)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Account):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash(self.id)

    def __repr__(self) -> str:
        return f'Account(owner="{self.owner}", balance={self.balance}, id="{self.id}")'
