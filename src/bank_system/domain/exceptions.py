class DomainError(Exception):
    pass


class InvalidMoneyError(DomainError):
    pass


class ZeroAmountError(DomainError):
    pass


class InsufficientFundsError(DomainError):
    pass


class SameAccountTransferError(DomainError):
    pass


class AccountNotFoundError(DomainError):
    pass
