from decimal import Decimal


class Account:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance = Decimal("0.00")

    @property
    def balance(self) -> Decimal:
        return self._balance

    def deposit(self, amount: Decimal) -> None:
        if amount <= Decimal("0.00"):
            raise ValueError("Deposit amount must be positive")
        if amount.quantize(Decimal("0.01")) != amount:
            raise ValueError("Deposit amount must have at most two decimal places")

        self._balance += amount

    def withdraw(self, amount: Decimal) -> None:
        if amount < Decimal("0.01"):
            raise ValueError("Withdraw amount isn't valid")
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount.quantize(Decimal("0.00"))
