from review_demo.contracts import PaymentCompletedEvent


class EventBus:
    def __init__(self):
        self.published: list[PaymentCompletedEvent] = []

    def publish(self, event: PaymentCompletedEvent) -> None:
        self.published.append(event)

