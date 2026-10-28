from decimal import Decimal

from review_demo.models import PaymentRequest
from review_demo.payment_service import PaymentService


class PaymentApi:
    def __init__(self, service: PaymentService):
        self.service = service

    def create_payment(self, payload: dict[str, str]):
        # BUG: user_id is trusted from caller-controlled payload rather than auth context.
        request = PaymentRequest(
            payment_id=payload["payment_id"],
            user_id=payload["user_id"],
            account_id=payload["account_id"],
            amount=Decimal(payload["amount"]),
            currency=payload.get("currency", "USD"),
        )
        return self.service.process(request)

