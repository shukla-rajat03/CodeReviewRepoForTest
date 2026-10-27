import unittest
from decimal import Decimal

from review_demo.models import PaymentRequest
from review_demo.validation import validate_payment


class PaymentApiValidationTest(unittest.TestCase):
    def test_zero_amount_is_rejected(self):
        request = PaymentRequest("pay-3", "user-1", "acct-1", Decimal("0"))
        with self.assertRaises(ValueError):
            validate_payment(request)


if __name__ == "__main__":
    unittest.main()

