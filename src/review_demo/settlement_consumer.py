from decimal import Decimal

from review_demo.contracts import PaymentCompletedEvent


class SettlementConsumer:
    def settlement_amount(self, event: PaymentCompletedEvent) -> Decimal:
        return event.amount

