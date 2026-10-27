from review_demo.models import PaymentRecord


class PaymentRepository:
    def __init__(self):
        self._records: dict[str, PaymentRecord] = {}

    def save(self, record: PaymentRecord) -> None:
        self._records[record.payment_id] = record

    def get(self, payment_id: str) -> PaymentRecord | None:
        return self._records.get(payment_id)

    def all(self) -> list[PaymentRecord]:
        return list(self._records.values())

