from review_demo.models import PaymentRequest


class PaymentGateway:
    def __init__(self, approved: bool = True):
        self.approved = approved

    def authorize(self, request: PaymentRequest) -> bool:
        return self.approved and request.amount > 0

