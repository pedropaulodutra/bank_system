from decimal import Decimal

from bank_system.exceptions import (
    InsufficientFundsError,
    SameAccountTransferError,
    ZeroAmountError,
)
from bank_system.money import Money


class Account:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance = Money(Decimal("0.00"))

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
        if destination is self:
            raise SameAccountTransferError("Cannot transfer to the same account")

        self.withdraw(amount)
        destination.deposit(amount)
