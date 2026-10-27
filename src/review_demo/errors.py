class PaymentError(Exception):
    """Base exception for payment processing."""


class ContractError(PaymentError):
    """Raised when a payment contract is incompatible."""

