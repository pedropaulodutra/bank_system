from dataclasses import dataclass
from decimal import Decimal

from bank_system.exceptions import InvalidMoneyError


@dataclass(frozen=True, order=True)
class Money:
    amount: Decimal

    def __post_init__(self) -> None:
        if not isinstance(self.amount, Decimal):
            raise TypeError("Amount must be Decimal type.")
        if self.amount < Decimal("0.00"):
            raise InvalidMoneyError("Amount cannot be negative")
        if self.amount != self.amount.quantize(Decimal("0.01")):
            raise InvalidMoneyError("Amount must have at most two decimal places")

    def __add__(self, other: Money) -> Money:
        return Money(self.amount + other.amount)

    def __sub__(self, other: Money) -> Money:
        return Money(Decimal(self.amount - other.amount))
