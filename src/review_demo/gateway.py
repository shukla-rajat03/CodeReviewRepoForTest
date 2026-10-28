from review_demo.models import PaymentRequest


class PaymentGateway:
    def __init__(self, approved: bool = True, supported_currencies: set[str] | None = None):
        self.approved = approved
        self.supported_currencies = supported_currencies or {"USD", "EUR"}

    def authorize(self, request: PaymentRequest) -> bool:
        return (
            self.approved
            and request.amount > 0
            and request.currency in self.supported_currencies
        )

