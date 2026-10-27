from review_demo.models import PaymentRequest


def validate_payment(request: PaymentRequest) -> None:
    if not request.payment_id:
        raise ValueError("payment_id is required")
    if request.amount <= 0:
        raise ValueError("amount must be positive")

