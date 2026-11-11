from decimal import Decimal

from bank_system.account import Account
from bank_system.money import Money

a = Account("Pedro")
b = Account("Kathleen")

a.deposit(Money(Decimal("10.00")))
a.transfer_to(b, Money(Decimal("0.00")))
