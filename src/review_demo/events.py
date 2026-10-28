from review_demo.contracts import PaymentCompletedEvent
from review_demo.models import PaymentRecord


def payment_completed(record: PaymentRecord) -> PaymentCompletedEvent:
    return PaymentCompletedEvent(
        payment_id=record.payment_id,
        total_amount=record.amount,
        currency=record.currency,
    )

