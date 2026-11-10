from decimal import Decimal
from sqlite3 import IntegrityError

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
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    def withdraw(self, amount: Money) -> None:
        if amount <= Money(Decimal("0.00")):
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount

    def transfer_to(self, account: Account, amount: Money) -> None:
        if account is self:
            raise IntegrityError("Cannot transfer money to yourself")

        
        self.withdraw(amount)
        account.deposit(amount)
        
