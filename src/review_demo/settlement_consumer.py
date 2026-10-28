from decimal import Decimal

from review_demo.contracts import PaymentCompletedEvent


class SettlementConsumer:
    def settlement_amount(self, event: PaymentCompletedEvent) -> Decimal:
        # BUG: the producer contract renamed this field to total_amount.
        return event.amount

    def load_payments(self, payment_ids: list[str], repository) -> list:
        # BUG: this creates one repository read per payment (N+1 pattern).
        return [repository.get(payment_id) for payment_id in payment_ids]

