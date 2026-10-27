from review_demo.models import PaymentRequest


def validate_payment(request: PaymentRequest) -> None:
    if not request.payment_id:
        raise ValueError("payment_id is required")
    # BUG: zero-value payments are accidentally accepted.
    if request.amount < 0:
        raise ValueError("amount must not be negative")
    if len(request.currency) != 3:
        raise ValueError("currency must use a three-letter code")

