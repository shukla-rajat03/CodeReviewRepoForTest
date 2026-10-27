import unittest
from decimal import Decimal

from review_demo.contracts import PaymentCompletedEvent
from review_demo.settlement_consumer import SettlementConsumer


class SettlementConsumerTest(unittest.TestCase):
    def test_reads_payment_amount(self):
        event = PaymentCompletedEvent("pay-1", Decimal("12.50"))
        self.assertEqual(Decimal("12.50"), SettlementConsumer().settlement_amount(event))


if __name__ == "__main__":
    unittest.main()

