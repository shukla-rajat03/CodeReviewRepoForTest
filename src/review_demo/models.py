from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class PaymentRequest:
    payment_id: str
    user_id: str
    account_id: str
    amount: Decimal


@dataclass
class PaymentRecord:
    payment_id: str
    account_id: str
    amount: Decimal
    status: str

