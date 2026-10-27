import unittest
from decimal import Decimal

from review_demo.audit import AuditLog
from review_demo.auth import AuthorizationService
from review_demo.event_bus import EventBus
from review_demo.gateway import PaymentGateway
from review_demo.idempotency import IdempotencyStore
from review_demo.models import PaymentRequest
from review_demo.payment_service import PaymentService
from review_demo.repository import PaymentRepository


class PaymentServiceTest(unittest.TestCase):
    def setUp(self):
        self.repository = PaymentRepository()
        self.service = PaymentService(
            auth=AuthorizationService({"acct-1": "user-1"}),
            gateway=PaymentGateway(approved=True),
            repository=self.repository,
            event_bus=EventBus(),
            audit=AuditLog(),
            idempotency=IdempotencyStore(),
        )

    def test_authorized_payment_is_saved(self):
        request = PaymentRequest(
            "pay-1", "user-1", "acct-1", Decimal("12.50"), "USD"
        )
        record = self.service.process(request)
        self.assertEqual("AUTHORIZED", record.status)
        self.assertIsNotNone(self.repository.get("pay-1"))

    def test_unauthorized_payment_is_not_saved(self):
        request = PaymentRequest(
            "pay-2", "user-2", "acct-1", Decimal("12.50"), "USD"
        )
        with self.assertRaises(PermissionError):
            self.service.process(request)
        self.assertIsNone(self.repository.get("pay-2"))


if __name__ == "__main__":
    unittest.main()

