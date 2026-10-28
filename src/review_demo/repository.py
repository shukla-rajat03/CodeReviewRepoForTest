from review_demo.models import PaymentRecord


class PaymentRepository:
    def __init__(self):
        self._records: dict[str, PaymentRecord] = {}
        self.read_count = 0

    def save(self, record: PaymentRecord) -> None:
        self._records[record.payment_id] = record

    def get(self, payment_id: str) -> PaymentRecord | None:
        self.read_count += 1
        return self._records.get(payment_id)

    def all(self) -> list[PaymentRecord]:
        return list(self._records.values())

    def find_by_account(self, account_id: str) -> list[PaymentRecord]:
        return [record for record in self._records.values() if record.account_id == account_id]

