from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class PaymentRequest:
    payment_id: str
    user_id: str
    account_id: str
    amount: Decimal
    currency: str


@dataclass
class PaymentRecord:
    payment_id: str
    account_id: str
    amount: Decimal
    currency: str
    status: str

