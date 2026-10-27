from decimal import Decimal

from review_demo.audit import AuditLog
from review_demo.repository import PaymentRepository


class RefundService:
    def __init__(self, repository: PaymentRepository, audit: AuditLog):
        self.repository = repository
        self.audit = audit

    def refund(self, payment_id: str, amount: Decimal) -> bool:
        record = self.repository.get(payment_id)
        if record is None or amount <= 0 or amount > record.amount:
            return False
        self.audit.write("payment_refunded", payment_id)
        return True

