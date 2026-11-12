from decimal import Decimal

from bank_system.account import Account
from bank_system.money import Money
from bank_system.repository import InMemoryAccountRepository
from bank_system.transfer_money import TransferMoney

bd = InMemoryAccountRepository()

account = Account("Pedro")
second_account = Account("Kathleen")

account.deposit(Money(Decimal("10.00")))

bd.save(account)
bd.save(second_account)

use_case = TransferMoney(bd)

use_case.execute(account.id, second_account.id, Decimal("7.00"))

print(second_account.balance)
print(account.balance)
