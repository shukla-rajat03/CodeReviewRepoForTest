from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class PaymentCompletedEvent:
    payment_id: str
    total_amount: Decimal
    currency: str

