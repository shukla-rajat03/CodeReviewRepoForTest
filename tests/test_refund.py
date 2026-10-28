import unittest
from decimal import Decimal

from review_demo.audit import AuditLog
from review_demo.models import PaymentRecord
from review_demo.refund_service import RefundService
from review_demo.repository import PaymentRepository


class RefundServiceTest(unittest.TestCase):
    def test_rejects_refund_larger_than_payment(self):
        repository = PaymentRepository()
        repository.save(
            PaymentRecord("pay-1", "acct-1", Decimal("10"), "USD", "AUTHORIZED")
        )
        service = RefundService(repository, AuditLog())
        self.assertFalse(service.refund("pay-1", Decimal("11"), "USD"))


if __name__ == "__main__":
    unittest.main()

